#!/usr/bin/env python
import time
import serial

stringList = []

ser = serial.Serial(
    port ='/dev/ttyACM0',
    baudrate=9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
    )

while 1:
    stringToSend = input("Enter string to send to Arduino: ")
    if(stringToSend == "EXIT"):
        break
    ser.write(stringToSend.encode())
    while(ser.inWaiting() < len(stringToSend)):
        pass
    stringReceived = ser.read(len(stringToSend))
    print ("String received from Arduino: ", stringReceived.decode("utf-8"))

    stringList.append(stringToSend)
    for string in stringList:
        print(string)
