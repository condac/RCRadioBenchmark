# RCRadioBenchmark
Arduino project to benchmark real actual delay from steering input to servo signal. 


## Connections

GND connect to - or gnd on both radio and reciever. 

Pin 2 connect to steering channel on reciever.

Pin 13 connect to the middle wire in the potensiometer in the radio. Make sure it is a 3 wire potensiometer with 5v on one pin and gnd on the other with a variable signal on the middle. Some radios have a cable with lots of pins for trim buttons and steering. Use cation not to damage your radio! And don't do anything you dont know what you are doing. Also be avare som radios have 3.3V systems. In that case you need to create a voltage divider for the Pin 13 output not to send 5V to the 3.3V system. 

You might have to reverse the steering in your model settings. 

The potensiometer don't have to be disconnected it can run paralell, your choise depending on what is most easy on the radio model. . 
