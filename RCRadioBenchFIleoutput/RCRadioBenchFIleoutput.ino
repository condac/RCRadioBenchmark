const byte ledPin = 13;
const byte interruptPin = 2;
volatile byte state = LOW;
unsigned long timer;
unsigned long lasttime;
unsigned long deltatime;
unsigned long starttime;
unsigned long stoptime;

unsigned long servo1;
unsigned long maxdelay;
unsigned long mindelay;
unsigned long totaltime;

int kaka;
bool running;
bool trigger;
int count;
unsigned long count10;
int updates;
unsigned long banan;

void setup() {
  pinMode(ledPin, OUTPUT);
  pinMode(interruptPin, INPUT_PULLUP);
  attachInterrupt(digitalPinToInterrupt(interruptPin), blink, CHANGE);
  Serial.begin(115200);
}

void loop() {

  //Serial.println("starting tests");
  tests();
}
void updatetest() {
  Serial.println(micros());
  starttime = micros() + 500000;
  running = true;
  updates = 0;
  banan = 0;
  stoptime = 0;
  while ( stoptime < starttime) {
    stoptime = micros();
    digitalWrite(ledPin, LOW);
    digitalWrite(ledPin, HIGH);
  }
  running = false;
  Serial.println(micros());

  
  Serial.print(banan);
  Serial.println(" updates per second");
}

void tests() {
  mindelay= 2000000UL;
    maxdelay= 0UL;
  for (int i=0; i<200; i++) {
    
    //Serial.print(servo1);
    //Serial.println(" servo1");
    count++;
    digitalWrite(ledPin, LOW);
    //delay(10);
    while(servo1 > 1100) {
      //Serial.print(servo1);
      //Serial.println(" waiting for zero");
    
      delay(4); // it takes about 4ms for the fastest radio to get new value
    }
  delayMicroseconds(random(30000));
  starttime = micros();
  digitalWrite(ledPin, HIGH);
  
  
  running = true;
  while (running) {
    if (servo1 >1200) {
      digitalWrite(ledPin, LOW);
      stoptime = timer;
      running = false;
      banan++;
      banan++;
      banan++;
      banan++;
      banan++;
      banan++;
      //Serial.print(servo1);
      //Serial.println(" servo1 stop");
    }
    else {
      banan++;
      banan++;
      banan++;
      banan++;
      banan++;
      banan++;
      }
  }
  
  //Serial.println("test done");
  totaltime = stoptime - starttime;
  if (totaltime >= maxdelay) {
    maxdelay = totaltime;
  }
  if (totaltime <= mindelay) {
    
    //Serial.print(totaltime);
    //Serial.print(" new min ");
    //Serial.println(mindelay);
    mindelay = totaltime;
  }
  //Serial.print(starttime);
  //Serial.println(" starttime");
  //Serial.print(stoptime);
  //Serial.println(" stoptime");
  Serial.println(totaltime);
  count10 = count10 + totaltime;
  //delay(random(100));
  
  }
  count10 / count;
  float avgout = (float)(count10)/count /1000;
  float minout = (float)mindelay/1000;
  float maxout = (float)maxdelay/1000;
  
  //Serial.print(avgout);
  //Serial.print(" avg ");
  //Serial.print(minout);
  //Serial.print(" min ");
  //Serial.print(maxout);
  //Serial.print(" max ");
  count = 0;
  count10 = 0;
  
  //Serial.println(" 200 tests done");
}

void blink() {
  timer = micros();
  deltatime = timer - lasttime;
  lasttime = timer;
  //Serial.println(deltatime);
  if (!digitalRead(interruptPin) ) {
  if (deltatime >800 && deltatime <2300) {
    servo1 = deltatime;
    //Serial.println(servo1);
    if (running) {
      if(deltatime > 1200) {
        digitalWrite(ledPin, LOW);
      }
    }
  }
  }
}
