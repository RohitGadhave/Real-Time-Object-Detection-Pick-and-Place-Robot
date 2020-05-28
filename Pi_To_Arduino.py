import serial
import time
usbCom =serial.Serial('/dev/ttyACM0',9600)
#usbCom.close()
#usbCom.open()
n=0
while n<1:
    usbCom.write(1)
    #time.sleep(5)
    n=n+1
    print(usbCom.readline())
    if usbCom.readline() == b'4\r\n':
        print("data recive")
    
