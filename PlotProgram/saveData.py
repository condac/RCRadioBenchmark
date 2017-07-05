
import serial

ser = serial.Serial('/dev/ttyUSB0', 115200)
with open('data.txt', 'w') as the_file:

    for i in range(1000):
        try:
            the_file.write(ser.readline().decode("utf-8"))
        except Exception as e:
            print(".")
