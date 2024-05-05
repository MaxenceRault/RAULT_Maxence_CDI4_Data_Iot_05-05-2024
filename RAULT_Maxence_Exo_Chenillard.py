from machine import Pin # importe dans le code la lib qui permet de gerer les Pins de sortie
import utime # importe dans le code la lib qui permet de gerer le temps

# declaration d'une variable pinNumber à 17
ledPin=[27,20,17]
leds=[]# declaration d'une variable de type pin ici la 17 
                                   #et on prescise que c'est une pin de sortie de courant (OUT)

for i in ledPin:
    leds.append(Pin(i,mode=Pin.OUT))
    
while True:
    for i in leds:
        i.on()
        utime.sleep(1)
        i.off()
     
    
    
    
    #led.on()        allume la led 
    #led.off()       eteind la led 