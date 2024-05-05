from machine import Pin, ADC , PWM # importe dans le code la lib qui permet de gerer les Pin de sortie et de reception de signaux analogique
import time # importe dans le code la lib qui permet de gerer le temps

pwm_led = PWM(Pin(17,mode=Pin.OUT))
adc = ADC(Pin(27, mode=Pin.IN)) # on prescise au programme que la pin 26 est une entré de type ADC
pwm_led.duty_u16(13000)

while True:# boucle infini
    val = adc.read_u16() # elle lit la valeur converti entre 0 et 65535 
    val = val * (10 / 65535) # produit en crois pour retrouver le voltage
    
    print(int(val)) # ecrire la valeur de val en arrondisant à l'entier
    time.sleep_ms(100) # attendre 100ms => 0.1 seconde
    """
    if int(val)==0:
        pwm_led.duty_u16(0)
        
    if int(val)==1:
        pwm_led.duty_u16(2000)
    
    if int(val)==2:
        pwm_led.duty_u16(4000)
        
    if int(val)==3:
        pwm_led.duty_u16(6000)
        
    if int(val)==4:
        pwm_led.duty_u16(8000)
        
    if int(val)==5:
        pwm_led.duty_u16(10000)
        
    if int(val)==6:
        pwm_led.duty_u16(12000)
        
    if int(val)==7:
        pwm_led.duty_u16(14000)
        
    if int(val)==8:
        pwm_led.duty_u16(16000)
        
    if int(val)==9:
        pwm_led.duty_u16(18000)
        
    if int(val)==10:
        pwm_led.duty_u16(20000)"""
    
    
    pwm_led.duty_u16(int(val) * 2000)

        
        
    
    