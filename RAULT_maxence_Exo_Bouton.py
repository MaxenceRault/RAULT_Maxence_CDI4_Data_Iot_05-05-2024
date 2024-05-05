from machine import Pin # importe dans le code la lib qui permet de gerer les Pin de sortie et d'entré
import utime # importe dans le code la lib qui permet de gerer le temps

pin_button = Pin(14, mode=Pin.IN, pull=Pin.PULL_UP) # declaration d'une variable de type pin ici la 14 
value=1                                                   #et on prescise que c'est une pine d'entré de courant (IN)
led = Pin(17, mode=Pin.OUT)


while True: # boucle infini
    
    
    if pin_button.value()==value:
        led.off()
        value=1
    else:
        led.on()
        value=0
    print(value) # on envoie la valeur du bouton
    utime.sleep(0.1)            # on attend 0.1 seconde