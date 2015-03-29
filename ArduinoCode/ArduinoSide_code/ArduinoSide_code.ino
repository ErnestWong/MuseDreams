int LED3 = 3;
int stageNumber = 0;

void setup(){
     Serial.begin(9600);
     pinMode(LED3,OUTPUT);
}

void loop(){
  if(Serial.available()>0){
    switch (Serial.read()){
      //enter stage 1
      case '1':
        for(int i=255;i>=150;i--){
        analogWrite(LED3,i);
       delay(10); 
      }
      stageNumber = 1;
        break;
        
      //enter stage 2
      case '2':
        for(int i=150;i>=60;i--){
        analogWrite(LED3,i);
        delay(10); 
      }
      stageNumber = 2;
        break;
        
      //enter stage 3
      case '3':
        for(int i=60;i>=10;i--){
        analogWrite(LED3,i);
        delay(10);
        }
        stageNumber = 3;
        break;
        
      //enter final stage    
      case '4': 
        for(int i=10;i>=0;i--){
          analogWrite(LED3,i);
          delay(90);
        }
        stageNumber = 4;
        break;
        
      default:
        if(stageNumber == 1){
           for(int i=150;i<=255;i++){
            analogWrite(LED3,i);
            delay(10); 
           }     
        }
        if(stageNumber == 2){
           for(int i=60;i<=255;i++){
            analogWrite(LED3,i);
            delay(10); 
           }  
        }
        if(stageNumber == 3){
           for(int i=10;i<=255;i++){
            analogWrite(LED3,i);
            delay(10); 
           }
        }
        if(stageNumber == 4){
          for(int i=0;i<=255;i++){
            analogWrite(LED3,i);
            delay(90);
        }
        }
      
  }
  }
}
  
//attempt to implement FSM, did not do becuase of time constraints 
/*
void loop(){ 
     if(Serial.available()>0){ 
        
       //char stage = Serial.read();
       //Finite State Machine
       //Stage 1
       if(Serial.read() == '1'){
         analogWrite(LED3,255);
         Serial.println("stage 1 complete");
         //Stage 2 
         if(Serial.read() == '2'){
           analogWrite(LED3,180);
           Serial.println("stage 2 complete");
           //Stage 3
           if(Serial.read() == '3'){
             analogWrite(LED3,63);
             Serial.println("stage 4 complete");
               //Stage 4
               if(Serial.read() == '4'){
                 analogWrite(LED3,0);
                 Serial.println("stage 4 complete");
              }
           }  
         }  
       }

    }
} */
