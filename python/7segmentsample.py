#!/usr/bin/python

import time
import serial


ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
time.sleep(2)
data = [0x7f, 0x1f, 0x04, 0x07, 0x00, 0x1f, 0x77, 0x05]
padding = 2


def writeToDisplay(list):
    ser.write("".join(chr(i) for i in list))
    ser.flush()


def createString(list):
    if len(list) < 8:
        list.append(0x00)
        for i in range(8 - len(list)):
            list.append(data[i])
    return list


# MAIN Program-Loop

bar_bottom = 0x8
bar_middle = 0x1
bar_top = 64
list = [2, 4, 8, 16, 64, 32]
#for count in range(2):
#    for e in list:
#        output = []
#        for b in range(8):
#            output.append(e)
#        print output
#        writeToDisplay(output)
#        time.sleep(0.05)


frame_1 = [8, 0, 0, 0, 0, 0, 0, 0]
frame_2 = [0, 8, 0, 0, 0, 0, 0, 0]
frame_3 = [0, 0, 8, 0, 0, 0, 0, 0]
frame_4 = [0, 0, 0, 8, 0, 0, 0, 0]
frame_5 = [0, 0, 0, 0, 8, 0, 0, 0]
frame_6 = [0, 0, 0, 0, 0, 8, 0, 0]
frame_7 = [0, 0, 0, 0, 0, 0, 8, 0]
frame_8 = [0, 0, 0, 0, 0, 0, 0, 8]
frame_9 = [0, 0, 0, 0, 0, 0, 0, 64]
frame_10 = [0, 0, 0, 0, 0, 0, 64, 0]
frame_11 = [0, 0, 0, 0, 0, 64, 0, 0]
frame_12 = [0, 0, 0, 0, 64, 0, 0, 0]
frame_13 = [0, 0, 0, 64, 0, 0, 0, 0]
frame_14 = [0, 0, 64, 0, 0, 0, 0, 0]
frame_15 = [0, 64, 0, 0, 0, 0, 0, 0]
frame_16 = [64, 0, 0, 0, 0, 0, 0, 0]
frame_17 = [2, 0, 0, 0, 0, 0, 0, 0]
frame_18 = [4, 0, 0, 0, 0, 0, 0, 0]

circle_sequence = [frame_1, frame_2, frame_3, frame_4, frame_5, frame_6,
        frame_7, frame_8, frame_9, frame_10, frame_11, frame_12, frame_13,
        frame_14, frame_15, frame_16, frame_17, frame_18]

#Printing circle_sequence
#for f in range(10):
#    for frame in circle_sequence:
#        writeToDisplay(frame)
#        time.sleep(0.01)

while 1:
    writeToDisplay(data)
    for idx in range(len(data) + 1):
        newString = createString(data[idx:])
        print newString
        writeToDisplay(newString)
        time.sleep(0.2)

    print "finished"
