
//General constants
#define MUXDELAY 10

//Pin mappings for the digits
#define DIGIT_1 1
#define DIGIT_2 2
#define DIGIT_3 3
#define DIGIT_4 4
#define DIGIT_5 5
#define DIGIT_6 6
#define DIGIT_7 7
#define DIGIT_8 8

//Pin mappings for the 74hc164 multiplexer (7 Segment + point multiplexing)
#define DATA 9
#define CLOCK 10

/*
Segment numbering:
       1
    --------
   |        |
 3 |        | 2
   |    4   |
    --------
   |        |
 6 |        | 5
   |        |
    --------   . 8
       7
 
 To display a one "1", you need to light up segments 2,5 => in binary: 0b01001000
 */

//8bit Demo String
byte eight_bit[8] = {
  0b11111110,
  0b00111110,
  0b00000100,
  0b00110100
};


byte display_buffer[8];
byte digit_pins[] = {
  DIGIT_1,DIGIT_2,DIGIT_3,DIGIT_4,DIGIT_5,DIGIT_6,DIGIT_7,DIGIT_8};

void setup() {                
  pinMode(CLOCK, OUTPUT);
  pinMode(DATA , OUTPUT);
  for(int n=0; n<8;++n){
    pinMode(digit_pins[n],OUTPUT);
    digitalWrite(digit_pins[n],LOW);
  }
}

// the loop runs over and over again forever:
void loop() {
  for(byte n=0; n<8;++n){
    shiftOut(DATA, CLOCK, LSBFIRST, display_buffer[n]);
    digitalWrite(digit_pins[n],HIGH);
    delay(MUXDELAY);
    digitalWrite(digit_pins[n],LOW);
  }

}



