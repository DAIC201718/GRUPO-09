#!/usr/bin/python3

import time
import RPi.GPIO as GPIO
# Configurar el GPIO con convenio de numerado BCM
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
# trig (cable amarillo en el prototipo)
GPIO.setup(12, GPIO.OUT)
# echo (cable verde en el prototipo)
GPIO.setup(19, GPIO.IN)

def eco():
	#try:
   	
        	start = 0
	        end = 0
	        # Configura el sensor
	        GPIO.output(12, False)
        	time.sleep(2) # 2 segundos para hacer el programa usable
	        # Empezamos a medir
	        GPIO.output(12, True)
	        time.sleep(10*10**-6) #10 microsegundos
	        GPIO.output(12, False)

	        # Flanco de 0 a 1 = inicio 
       		while GPIO.input(19) == GPIO.LOW:
           		start = time.time()
       		# Flanco de 1 a 0 = fin
       	 	while GPIO.input(19) == GPIO.HIGH:
            	 	end = time.time()

       		# el tiempo que devuelve time() esta en segundos
       	 	distancia = (end-start) * 343 / 2
		
       
        
#except KeyboardInterrupt:
 #   print("\nFin del programa")
 #   GPIO.output(12, False)
 #   GPIO.cleanup()
		return distancia
