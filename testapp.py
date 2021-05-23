#!/usr/bin/env python
from flask import Flask, render_template, Response
 
from imutils.video import VideoStream
import imutils
import time
import serial as serial
serport = '/dev/ttyUSB0'

j1min=130
j1max=650
j2min=130
j2max=650
j2=358
j1=370
stepsize=4
app = Flask(__name__)
flag=0

 
 
@app.route('/')
def index():
    return render_template('index.html')

 
def gen():
	# grab global references to the output frame and lock variables
	global outputFrame, lock
	# loop over frames from the output stream
	while True:
		# wait until the lock is acquired
		
		# check if the output frame is available, otherwise skip
		# the iteration of the loop
		
		
		# encode the frame in JPEG format
		 
		# ensure the frame was successfully encoded
		if not flag:
			continue
		# yield the output frame in the byte format
		yield(b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + 
			bytearray(encodedImage) + b'\r\n')
			
			
			

 
 
def convstr(n):
	if (n<100):
		return ('0'+str(n))
	else:
		return str(n)
 
	
	
@app.route('/left_side')
def left_side():
	global j1
	if (j1<j1max):
		j1 +=stepsize
	ser.write(bytearray('j01'+convstr(j1), 'utf8'))
	print(j1)
	print (ser.readline())
	return 'true'

@app.route('/right_side')
def right_side():
	global j1
	if (j1>j1min):
		j1 -=stepsize
	ser.write(bytearray('j01'+convstr(j1), 'utf8'))
	print(j1)
	print (ser.readline())
	return 'true'

	

@app.route('/up_side')
def up_side():
	global j2
	
	if (j2<j2max):
		j2 +=stepsize
	ser.write(bytearray('j02'+convstr(j2), 'utf8'))
	print(j2)
	print (ser.readline())
	return 'true'	

@app.route('/down_side')
def down_side():
	
	
	global j2
	if (j2>j2min):
		j2 -=stepsize
	ser.write(bytearray('j02'+convstr(j2), 'utf8'))
	print(j2)
	print (ser.readline())
	return 'true'
	
			
@app.route('/video_feed')
def video_feed():
    return Response(gen(),mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
	ser = serial.Serial()
	ser.port = serport
	ser.baudrate = 9600
	ser.timeout = 0
	# open port if not already open
	if ser.isOpen() == False:
		ser.open()
	app.run(host='192.168.1.20',port=5000, debug=True)
