import serial
import sys
from pynput.keyboard import Key, Controller 
keyboard = Controller()
#temps = sys.argv[1]
sr = serial.Serial()
sr.baudrate = 9600
sr.bytesize = 8


#sr.port = temps
sr.port = 'COM7'
sr.close()
sr.open()
while 1:
    try:
        a = str(sr.readline().decode().strip('\r\n'))
        print(a)
        if (a.find('a') == 0):
            a = a[1:5]
            if(int(a) > 2000):
                print('q')
                keyboard.press('q')
            else:
                keyboard.release('q')
        if (a.find('b') == 0):
            a = a[1:5]
            if(int(a) > 1700):
                print('w')
                keyboard.press('w')
            else:
                keyboard.release('w')
        if (a.find('c') == 0):
            a = a[1:5]
            if(int(a) > 1700):
                print('w')
                keyboard.press('e')
            else:
                keyboard.release('e')
    except:
        continue
    
   
    

        
##    
##    if len(a) == 5:
##        print(a)
##        if(a[0] > 3000):
##            keyboard.press('q')
##        else:
##            keyboard.release('q')
##        if(a[1] > 2000):
##            keyboard.press('w')
##        else:
##            keyboard.release('w')
##        if(a[2] > 2000):
##            keyboard.press('e')
##        else:
##            keyboard.release('e')
##        if(a[3] > 3000):
##            keyboard.press('r')
##        else:
##            keyboard.release('r')
##        if(a[4] > 2000):
##            keyboard.press('t')
##        else:
##            keyboard.release('t')
        
