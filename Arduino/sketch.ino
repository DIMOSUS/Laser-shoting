void setup() {
    pinMode(3, OUTPUT);//LED
    pinMode(2, INPUT);//Button to ground
    digitalWrite(2, true);
}

int t = 10000;
bool PreButton = false;

void loop() {
    bool Button = !digitalRead(2);
    if (PreButton == false && Button == true && t > 500) t = 0;
    if (t<9) digitalWrite(3, true);
    else digitalWrite(3, false);
    if (t<10000) t++;
    PreButton = Button;
    delay(1);
}
