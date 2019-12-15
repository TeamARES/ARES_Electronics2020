import motor_ibt2

fowrard_left_motor = motor_ibt2.motor1_ibt2(13,19)  #Parameters are input LPWM_and RPWM pin of IBT2
fowrard_left_motor.moveMotor(50)                 #Duticycle ranging from -100 to 100 [+ve means forward, -ve means backwards]



#Testing by printing
fowrard_left_motor.printMotor()