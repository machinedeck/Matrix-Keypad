// from https://docs.arduino.cc/language-reference/en/functions/communication/serial/read/
// int incomingByte = 0;
int x = 0;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(57600);

}

void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available() > 0) {
    String incomingstring = Serial.readStringUntil("\n");
    int incomingint = incomingstring.toInt();
    // incomingByte = Serial.parseInt();

    if ((incomingint >= 4770) && (incomingint <= 4780)) {
      x = 1;
    }

    else if ((incomingint >= 2437) && (incomingint <= 2447)) {
      x = 2;
    }

    else if ((incomingint >= 1636) && (incomingint <= 1645)) {
      x = 3;
    }

    else if ((incomingint >= 1230) && (incomingint <= 1240)) {
      x = 4;
    }

    else if ((incomingint >= 4566) && (incomingint <= 4575)) {
      x = 5;
    }

    else if ((incomingint >= 2383) && (incomingint <= 2392)) {
      x = 6;
    }

    else if ((incomingint >= 1611) && (incomingint <= 1621)) {
      x = 7;
    }

    else if ((incomingint >= 1216) && (incomingint <= 1226)) {
      x = 8;
    }

    else if ((incomingint >= 4378) && (incomingint <= 4388)) {
      x = 9;
    }

    else if ((incomingint >= 2330) && (incomingint <= 2340)) {
      x = 10;
    }

    else if ((incomingint >= 1587) && (incomingint <= 1596)) {
      x = 11;
    }

    else if ((incomingint >= 1202) && (incomingint <= 1212)) {
      x = 12;
    }

    else if ((incomingint >= 4205) && (incomingint <= 4215)) {
      x = 13;
    }

    else if ((incomingint >= 2280) && (incomingint <= 2290)) {
      x = 14;
    }

    else if ((incomingint >= 1563) && (incomingint <= 1573)) {
      x = 15;
    }

    else if ((incomingint >= 1189) && (incomingint <= 1198)) {
      x = 16;
    }
    Serial.println(x);
  }
}
