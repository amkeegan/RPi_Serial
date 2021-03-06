#!/usr/bin/env python
import time
import serial

counter = 0
             
ser = serial.Serial(
    port ='/dev/ttyACM0',
    baudrate=9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
    )

stringToSend = input("Enter string to send to Arduino: ")

while counter < 20:
    if(stringToSend == "EXIT"):
        break
    ser.write(stringToSend.encode())
    while(ser.inWaiting() < len(stringToSend)):
        pass
    stringReceived = ser.read(len(stringToSend))
    print ("String received from Arduino: ", stringReceived.decode("utf-8"), " "+str(counter))
    counter += 1
