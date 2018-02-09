# -*- coding: utf-8 -*-
import tkinter as tk
import sys
import glob
import serial as serial
import time
import tensorflow as tf
import cv2

RightLeftCounter = 370
j2=370
j1=300
j3=300
j4=300
j5=300
j6=300
j7=300
j14=600
j15=450
delay=0.5

j1min=130
j1max=650
j2min=130
j2max=650
j3min=130
j3max=650
j4min=130
j4max=650
j5min=130
j5max=650
j6min=130
j6max=650
j7min=130
j7max=650
j14min=130
j14max=650
j15min=200
j15max=650

j1av=450
j2av=310
j3av=450
j4av=450
j5av=600
j6av=370
j7av=470
j14av=610
j15av=486

j1=j1av
j2=j2av
j3=j3av
j4=j4av
j5=j5av
j6=j6av
j7=j7av
j14=j14av
j15=j15av



stepsize=4


class App:
  def __init__(self, master, ser):
 
    self.ser  = ser
    self.button = tk.Button(master, 
                         text="QUIT", fg="red",
                         command=quit)
    self.num = j1av
    self.button.grid(row=11, column=8, padx=0, pady=0, sticky="nw")

####LABELS
    self.label = tk.Label(master, 
                         text="J1", fg="red")
    self.label.grid(row=1, column=0, padx=0, pady=0, sticky="nw")
    
    self.label = tk.Label(master, 
                         text="J2", fg="red")
    self.label.grid(row=2, column=0, padx=0, pady=0, sticky="nw")

    self.label = tk.Label(master, 
                         text="J3", fg="red")
    self.label.grid(row=3, column=0, padx=0, pady=0, sticky="nw")
    self.label = tk.Label(master, 
                         text="J4", fg="red")
    self.label.grid(row=4, column=0, padx=0, pady=0, sticky="nw")
    self.label = tk.Label(master, 
                         text="J5", fg="red")
    self.label.grid(row=5, column=0, padx=0, pady=0, sticky="nw")
    self.label = tk.Label(master, 
                         text="J6", fg="red")
    self.label.grid(row=6, column=0, padx=0, pady=0, sticky="nw")
    self.label = tk.Label(master, 
                         text="Gripper", fg="red")
    self.label.grid(row=7, column=0, padx=0, pady=0, sticky="nw")
    self.label = tk.Label(master, 
                         text="PanCamera", fg="red")
    self.label.grid(row=9, column=0, padx=0, pady=0, sticky="nw")
    self.label = tk.Label(master, 
                         text="TiltCamera", fg="red")
    self.label.grid(row=10, column=0, padx=0, pady=0, sticky="nw")
###############################################


    self.entry = tk.Entry(master, 
                         text="0.5", fg="black")
    self.entry.grid(row=1, column=8, padx=0, pady=0, sticky="nw")
 
    self.slogan = tk.Button(master,
                         text="Reset",
                         command=self.writej1_reset)
    self.slogan.grid(row=1, column=4, padx=2, pady=0, sticky="nw")
 
    self.Left = tk.Button(master,
                         text="←",padx=10,
                         command=self.writej1_Left)
    self.Left.grid(row=1, column=1, padx=2, pady=0, sticky="nw")
 
    self.Right = tk.Button(master,
                         text="→",padx=10,
                         command=self.writej1_Right)
    self.Right.grid(row=1, column=6, padx=2, pady=0, sticky="nw")

###############################################


    self.button.grid(row=2, column=0, padx=0, pady=0, sticky="nw")
 
    self.slogan = tk.Button(master,
                         text="Reset",
                         command=self.writej2_reset)
    self.slogan.grid(row=2, column=4, padx=0, pady=0, sticky="nw")
 
    self.Left = tk.Button(master,
                         text="←",padx=10,
                         command=self.writej2_Left)
    self.Left.grid(row=2, column=1, padx=0, pady=0, sticky="nw")
 
    self.Right = tk.Button(master,
                         text="→",padx=10,
                         command=self.writej2_Right)
    self.Right.grid(row=2, column=6, padx=2, pady=0, sticky="nw")

###############################################


    self.button.grid(row=3, column=0, padx=0, pady=0, sticky="nw")
 
    self.slogan = tk.Button(master,
                         text="Reset",
                         command=self.writej3_reset)
    self.slogan.grid(row=3, column=4, padx=0, pady=0, sticky="nw")
 
    self.Left = tk.Button(master,
                         text="←",padx=10,
                         command=self.writej3_Left)
    self.Left.grid(row=3, column=1, padx=0, pady=0, sticky="nw")
 
    self.Right = tk.Button(master,
                         text="→",padx=10,
                         command=self.writej3_Right)
    self.Right.grid(row=3, column=6, padx=2, pady=0, sticky="nw")

###############################################


    self.button.grid(row=4, column=0, padx=0, pady=0, sticky="nw")
 
    self.slogan = tk.Button(master,
                         text="Reset",
                         command=self.writej4_reset)
    self.slogan.grid(row=4, column=4, padx=0, pady=0, sticky="nw")
 
    self.Left = tk.Button(master,
                         text="←",padx=10,
                         command=self.writej4_Left)
    self.Left.grid(row=4, column=1, padx=0, pady=0, sticky="nw")
 
    self.Right = tk.Button(master,
                         text="→",padx=10,
                         command=self.writej4_Right)
    self.Right.grid(row=4, column=6, padx=2, pady=0, sticky="nw")

###############################################


    self.button.grid(row=5, column=0, padx=0, pady=0, sticky="nw")
 
    self.slogan = tk.Button(master,
                         text="Reset",
                         command=self.writej5_reset)
    self.slogan.grid(row=5, column=4, padx=0, pady=0, sticky="nw")
 
    self.Left = tk.Button(master,
                         text="←",padx=10,
                         command=self.writej5_Left)
    self.Left.grid(row=5, column=1, padx=0, pady=0, sticky="nw")
 
    self.Right = tk.Button(master,
                         text="→",padx=10,
                         command=self.writej5_Right)
    self.Right.grid(row=5, column=6, padx=2, pady=0, sticky="nw")

###############################################


    self.button.grid(row=6, column=0, padx=0, pady=0, sticky="nw")
 
    self.slogan = tk.Button(master,
                         text="Reset",
                         command=self.writej6_reset)
    self.slogan.grid(row=6, column=4, padx=0, pady=0, sticky="nw")
 
    self.Left = tk.Button(master,
                         text="←",padx=10,
                         command=self.writej6_Left)
    self.Left.grid(row=6, column=1, padx=0, pady=0, sticky="nw")
 
    self.Right = tk.Button(master,
                         text="→",padx=10,
                         command=self.writej6_Right)
    self.Right.grid(row=6, column=6, padx=2, pady=0, sticky="nw")

###############################################


    self.button.grid(row=7, column=0, padx=0, pady=0, sticky="nw")
 
    self.slogan = tk.Button(master,
                         text="Reset",
                         command=self.writej7_reset)
    self.slogan.grid(row=7, column=4, padx=0, pady=0, sticky="nw")
 
    self.Left = tk.Button(master,
                         text="←",padx=10,
                         command=self.writej7_Left)
    self.Left.grid(row=7, column=1, padx=0, pady=0, sticky="nw")
 
    self.Right = tk.Button(master,
                         text="→",padx=10,
                         command=self.writej7_Right)
    self.Right.grid(row=7, column=6, padx=2, pady=0, sticky="nw")

###############################################


    self.button.grid(row=9, column=0, padx=0, pady=0, sticky="nw")
 
    self.slogan = tk.Button(master,
                         text="Reset",
                         command=self.writej14_reset)
    self.slogan.grid(row=9, column=4, padx=0, pady=0, sticky="nw")
 
    self.Left = tk.Button(master,
                         text="←",padx=10,
                         command=self.writej14_Left)
    self.Left.grid(row=9, column=1, padx=0, pady=0, sticky="nw")
 
    self.Right = tk.Button(master,
                         text="→",padx=10,
                         command=self.writej14_Right)
    self.Right.grid(row=9, column=6, padx=2, pady=0, sticky="nw")

###############################################


    self.button.grid(row=10, column=0, padx=0, pady=0, sticky="nw")
 
    self.slogan = tk.Button(master,
                         text="Reset",
                         command=self.writej15_reset)
    self.slogan.grid(row=10, column=4, padx=0, pady=0, sticky="nw")
 
    self.Left = tk.Button(master,
                         text="←",padx=10,
                         command=self.writej15_Left)
    self.Left.grid(row=10, column=1, padx=0, pady=0, sticky="nw")
 
    self.Right = tk.Button(master,
                         text="→",padx=10,
                         command=self.writej15_Right)
    self.Right.grid(row=10, column=6, padx=2, pady=0, sticky="nw")

###############################################
    self.button.grid(row=10, column=6, padx=0, pady=0, sticky="nw")
 
    self.slogan = tk.Button(master,
                         text="Open Loop Pick",
                         command=self.Oloop_pick)
    self.slogan.grid(row=10, column=8, padx=0, pady=0, sticky="nw")

###############################################
    
  def Oloop_pick(self):
    global j1
    global j2
    global j3
    global j4
    global j5
    global j6
    global j7

    if (j1>j1min):
      j2=310
      j7=580
      self.ser.write(bytearray('j02'+self.convstr(j2), 'utf8'))
      time.sleep(delay)
      
      j4=435
      j1=450
      j3=450
      
      self.ser.write(bytearray('j03'+self.convstr(j3), 'utf8'))
      time.sleep(delay)
      self.ser.write(bytearray('j07'+self.convstr(j7), 'utf8'))
      time.sleep(delay)
      self.ser.write(bytearray('j01'+self.convstr(j1), 'utf8'))
      time.sleep(delay)
      self.ser.write(bytearray('j04'+self.convstr(j4), 'utf8'))
      time.sleep(delay)


      j2=358
      self.ser.write(bytearray('j02'+self.convstr(j2), 'utf8'))
      time.sleep(delay)
      
      
     

     
      j2=286
      j7=458
      self.ser.write(bytearray('j07'+self.convstr(j7), 'utf8'))
      time.sleep(delay)
      self.ser.write(bytearray('j04'+self.convstr(j4), 'utf8'))
      time.sleep(delay)
      self.ser.write(bytearray('j02'+self.convstr(j2), 'utf8'))
      time.sleep(delay)

      
      j1=524
      j3=490
      j2=258
      self.ser.write(bytearray('j03'+self.convstr(j3), 'utf8'))
      time.sleep(delay)
      
      j7=500
      self.ser.write(bytearray('j02'+self.convstr(j2), 'utf8'))
      time.sleep(delay)
      self.ser.write(bytearray('j01'+self.convstr(j1), 'utf8'))
      time.sleep(delay)
      
      self.ser.write(bytearray('j07'+self.convstr(j7), 'utf8'))
      time.sleep(delay+3)
      j1=450
      j3=450
      self.ser.write(bytearray('j03'+self.convstr(j3), 'utf8'))
      time.sleep(delay)
      self.ser.write(bytearray('j01'+self.convstr(j1), 'utf8'))
      time.sleep(delay)


      
      
    print(j1)
    print (self.ser.readline())
 

    
  
    
  def write_Left(self):
    global RightLeftCounter
    if (RightLeftCounter>0):
      RightLeftCounter -=stepsize
    self.ser.write(bytearray(RightLeftCounter))
    print(RightLeftCounter)
    print (self.ser.readline())
 
  def write_Right(self):
    global RightLeftCounter
    if (RightLeftCounter<180):
      RightLeftCounter +=stepsize
    self.ser.write(bytearray(RightLeftCounter))
    print(RightLeftCounter)
    print (self.ser.readline())
  def write_reset(self):
    global RightLeftCounter
    RightLeftCounter = 90
    print(RightLeftCounter)
    self.ser.write(bytearray(RightLeftCounter))
    print (self.ser.readline())
 
  def write_sweep(self):
    global RightLeftCounter
    for RightLeftCounter in range(0,180):
      print(RightLeftCounter)
      self.ser.write(bytearray(RightLeftCounter))
      print (self.ser.readline())
      time.sleep(0.01) # delays for 1 seconds
    RightLeftCounter = 90
    self.ser.write(bytearray(RightLeftCounter))
    
####################################################
  def convstr(self,n):
    if (n<100):
      return ('0'+str(n))
    else:
      return str(n)

    
  def writej1_Left(self):
    global j1
    if (j1>j1min):
      j1 -=stepsize
    self.ser.write(bytearray('j01'+self.convstr(j1), 'utf8'))
    print(j1)
    print (self.ser.readline())
 
  def writej1_Right(self):
    global j1
    if (j1<j1max):
      j1 +=stepsize
    self.ser.write(bytearray('j01'+self.convstr(j1), 'utf8'))
    print(j1)
    print (self.ser.readline())
  def writej1_reset(self):
    global j1
    j1 = j1av
    self.ser.write(bytearray('j01'+self.convstr(j1), 'utf8'))
    print('j01'+self.convstr(j1))
    print (self.ser.readline())
 
  def writej1_sweep(self):
    global j1
    for j1 in range(0,180):
      print(j1)
      self.ser.write(bytearray('j01'+self.convstr(j1), 'utf8'))
      print (self.ser.readline())
      time.sleep(0.01) # delays for 1 seconds
    j1 = 90
    self.ser.write(bytearray('j01'+self.convstr(j1), 'utf8'))

    ####################################################

  def writej2_Left(self):
    global j2
    if (j2>j2min):
      j2 -=stepsize
    self.ser.write(bytearray('j02'+self.convstr(j2), 'utf8'))
    print(j2)
    print (self.ser.readline())
 
  def writej2_Right(self):
    global j2
    if (j2<j2max):
      j2 +=stepsize
    self.ser.write(bytearray('j02'+self.convstr(j2), 'utf8'))
    print(j2)
    print (self.ser.readline())
  def writej2_reset(self):
    global j2
    j2 = j2av
    self.ser.write(bytearray('j02'+self.convstr(j2), 'utf8'))
    print('j02'+self.convstr(j2))
    print (self.ser.readline())
 
  def writej2_sweep(self):
    global j2
    for j2 in range(0,280):
      print(j2)
      self.ser.write(bytearray('j02'+self.convstr(j2), 'utf8'))
      print (self.ser.readline())
      time.sleep(0.01) # delays for 1 seconds
    j1 = 90
    self.ser.write(bytearray('j02'+self.convstr(j2), 'utf8'))


    ####################################################

  def writej3_Left(self):
    global j3
    if (j3>j3min):
      j3 -=stepsize
    self.ser.write(bytearray('j03'+self.convstr(j3), 'utf8'))
    print(j3)
    print (self.ser.readline())
 
  def writej3_Right(self):
    global j3
    if (j3<j3max):
      j3 +=stepsize
    self.ser.write(bytearray('j03'+self.convstr(j3), 'utf8'))
    print(j3)
    print (self.ser.readline())
  def writej3_reset(self):
    global j3
    j3 = j3av
    self.ser.write(bytearray('j03'+self.convstr(j3), 'utf8'))
    print('j03'+self.convstr(j3))
    print (self.ser.readline())
 
  def writej3_sweep(self):
    global j3
    for j3 in range(0,380):
      print(j3)
      self.ser.write(bytearray('j03'+self.convstr(j3), 'utf8'))
      print (self.ser.readline())
      time.sleep(0.01) # delays for 1 seconds
    j1 = 90
    self.ser.write(bytearray('j03'+self.convstr(j3), 'utf8'))

    
    ####################################################

  def writej4_Left(self):
    global j4
    if (j4>j4min):
      j4 -=stepsize
    self.ser.write(bytearray('j04'+self.convstr(j4), 'utf8'))
    print(j4)
    print (self.ser.readline())
 
  def writej4_Right(self):
    global j4
    if (j4<j4max):
      j4 +=stepsize
    self.ser.write(bytearray('j04'+self.convstr(j4), 'utf8'))
    print(j4)
    print (self.ser.readline())
  def writej4_reset(self):
    global j4
    j4 = j4av
    self.ser.write(bytearray('j04'+self.convstr(j4), 'utf8'))
    print('j04'+self.convstr(j4))
    print (self.ser.readline())
 
  def writej4_sweep(self):
    global j4
    for j4 in range(0,480):
      print(j4)
      self.ser.write(bytearray('j04'+self.convstr(j4), 'utf8'))
      print (self.ser.readline())
      time.sleep(0.01) # delays for 1 seconds
    j1 = 90
    self.ser.write(bytearray('j04'+self.convstr(j4), 'utf8'))

    
    ####################################################

  def writej5_Left(self):
    global j5
    if (j5>j5min):
      j5 -=stepsize
    self.ser.write(bytearray('j05'+self.convstr(j5), 'utf8'))
    print(j5)
    print (self.ser.readline())
 
  def writej5_Right(self):
    global j5
    if (j5<j5max):
      j5 +=stepsize
    self.ser.write(bytearray('j05'+self.convstr(j5), 'utf8'))
    print(j5)
    print (self.ser.readline())
  def writej5_reset(self):
    global j5
    j5 = j5av
    self.ser.write(bytearray('j05'+self.convstr(j5), 'utf8'))
    print('j05'+self.convstr(j5))
    print (self.ser.readline())
 
  def writej5_sweep(self):
    global j5
    for j5 in range(0,580):
      print(j5)
      self.ser.write(bytearray('j05'+self.convstr(j5), 'utf8'))
      print (self.ser.readline())
      time.sleep(0.01) # delays for 1 seconds
    j1 = 90
    self.ser.write(bytearray('j05'+self.convstr(j5), 'utf8'))

####################################################

  def writej6_Left(self):
    global j6
    if (j6>j6min):
      j6 -=stepsize
    self.ser.write(bytearray('j06'+self.convstr(j6), 'utf8'))
    print(j6)
    print (self.ser.readline())
 
  def writej6_Right(self):
    global j6
    if (j6<j6max):
      j6 +=stepsize
    self.ser.write(bytearray('j06'+self.convstr(j6), 'utf8'))
    print(j6)
    print (self.ser.readline())
  def writej6_reset(self):
    global j6
    j6 = j6av
    self.ser.write(bytearray('j06'+self.convstr(j6), 'utf8'))
    print('j06'+self.convstr(j6))
    print (self.ser.readline())
 
  def writej6_sweep(self):
    global j6
    for j6 in range(0,680):
      print(j6)
      self.ser.write(bytearray('j06'+self.convstr(j6), 'utf8'))
      print (self.ser.readline())
      time.sleep(0.01) # delays for 1 seconds
    j1 = 90
    self.ser.write(bytearray('j06'+self.convstr(j6), 'utf8'))
    

    
    ####################################################

  def writej7_Left(self):
    global j7
    if (j7>j7min):
      j7 -=stepsize
    self.ser.write(bytearray('j07'+self.convstr(j7), 'utf8'))
    print(j7)
    print (self.ser.readline())
 
  def writej7_Right(self):
    global j7
    if (j7<j7max):
      j7 +=stepsize
    self.ser.write(bytearray('j07'+self.convstr(j7), 'utf8'))
    print(j7)
    print (self.ser.readline())
  def writej7_reset(self):
    global j7
    j7 = j7av
    self.ser.write(bytearray('j07'+self.convstr(j7), 'utf8'))
    print('j07'+self.convstr(j7))
    print (self.ser.readline())
 
  def writej7_sweep(self):
    global j7
    for j7 in range(0,780):
      print(j7)
      self.ser.write(bytearray('j07'+self.convstr(j7), 'utf8'))
      print (self.ser.readline())
      time.sleep(0.01) # delays for 1 seconds
    j1 = 90
    self.ser.write(bytearray('j07'+self.convstr(j7), 'utf8'))
    
    ####################################################

  def writej14_Left(self):
    global j14
    if (j14>j14min):
      j14 -=stepsize
    self.ser.write(bytearray('j14'+self.convstr(j14), 'utf8'))
    print(j14)
    print (self.ser.readline())
 
  def writej14_Right(self):
    global j14
    if (j14<j14max):
      j14 +=stepsize
    self.ser.write(bytearray('j14'+self.convstr(j14), 'utf8'))
    print(j14)
    print (self.ser.readline())
  def writej14_reset(self):
    global j14
    j14 = j14av
    self.ser.write(bytearray('j14'+self.convstr(j14), 'utf8'))
    print('j014'+self.convstr(j14))
    print (self.ser.readline())
 
  def writej14_sweep(self):
    global j14
    for j14 in range(0,1480):
      print(j14)
      self.ser.write(bytearray('j14'+self.convstr(j14), 'utf8'))
      print (self.ser.readline())
      time.sleep(0.01) # delays for 1 seconds
    j1 = 90
    self.ser.write(bytearray('j14'+self.convstr(j14), 'utf8'))
    

    ####################################################

  def writej15_Left(self):
    global j15
    if (j15>j15min):
      j15 -=stepsize
    self.ser.write(bytearray('j15'+self.convstr(j15), 'utf8'))
    print(j15)
    print (self.ser.readline())
 
  def writej15_Right(self):
    global j15
    if (j15<j15max):
      j15 +=stepsize
    self.ser.write(bytearray('j15'+self.convstr(j15), 'utf8'))
    print(j15)
    print (self.ser.readline())
  def writej15_reset(self):
    global j15
    j15 = j15av
    self.ser.write(bytearray('j15'+self.convstr(j15), 'utf8'))
    print('j015'+self.convstr(j15))
    print (self.ser.readline())
 
  def writej15_sweep(self):
    global j15
    for j15 in range(0,1580):
      print(j15)
      self.ser.write(bytearray('j15'+self.convstr(j15), 'utf8'))
      print (self.ser.readline())
      time.sleep(0.01) # delays for 1 seconds
    j1 = 90
    self.ser.write(bytearray('j15'+self.convstr(j15), 'utf8'))
    

    

    

def main():
  ser = serial.Serial()
  ser.port = 'COM5'
  ser.baudrate = 9600
  ser.timeout = 0
  # open port if not already open
  if ser.isOpen() == False:
    ser.open()
  root = tk.Tk()
  root.title("TEST")
  root.geometry("500x500+500+300")
  app = App(root,ser)
  
  root.mainloop()
 
if __name__ == '__main__':
  main()
