int PWMpin = 3;
int B=50;

void setup ()
{
pinMode(PWMpin,OUTPUT);
pinMode(B,OUTPUT);
}


void loop()
{
  digitalWrite(B,HIGH);
   for (int i = 0, x = 1; i > -1; i = i + x)//x acts as ++ in this
   {
       analogWrite(PWMpin, i);
       delay(10);
//once the for loop reaches 255, the if condition says to start reducing
{//if (i == 255) 
   //   x = -1;             // x starts tp acts as -- 
    //delay(10);
   }
   }

}


