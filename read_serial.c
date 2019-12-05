void setup (){
	serial.begin(9600);
}
void loop(){
	serial.readString();
	delay(50);
}
