    pinMode(3, OUTPUT);
    digitalWrite(2, true);
}

int t = 10000;
bool PreButton = false;

void loop() {
  // put your main code here, to run repeatedly:
  
    bool Button = !digitalRead(2);
    
    if (PreButton == false && Button == true && t > 500)
    {
      t = 0;
    }

    if (t<5) digitalWrite(3, true);
    else digitalWrite(3, false);
    if (t<10000) t++;
    PreButton = Button;
    delay(1);
}

