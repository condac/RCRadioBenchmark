
import serial
import sys

# get argument list using sys module
sys.argv
if (len(sys.argv)>1):
    print("arg true")
    dataPoints = int(sys.argv[1])
else:
    print("arg false")
    dataPoints = 1000

timeCollect = dataPoints /10
print("Collecting "+str(dataPoints)+" can take up to "+str(timeCollect)+" seconds...")

ser = serial.Serial('/dev/ttyUSB0', 115200)
with open('data.txt', 'w') as the_file:

    flippflopp = 0
    for i in range(dataPoints):
        flippflopp+=1
        if (flippflopp > 10):
            flippflopp = 0
            percent = (i/dataPoints)*100

            print('                               \r', end='', flush=True)
            print(str(percent)+'% \r', end='', flush=True)
        try:
            the_file.write(ser.readline().decode("utf-8"))
        except Exception as e:
            print(".")
