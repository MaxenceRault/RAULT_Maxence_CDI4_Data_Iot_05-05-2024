import network   #import des fonction lier au wifi
import urequests    #import des fonction lier au requetes http
import utime    #import des fonction lier au temps
import ujson    #import des fonction lier aà la convertion en Json
from machine import Pin, PWM # importe dans le code la lib qui permet de gerer les Pin de sortie et de modulation du signal
import time


pwm_bleu = PWM(Pin(19,mode=Pin.OUT)) # on prescise au programme que la pin 15 est une sortie de type PWN
pwm_bleu.freq(1_000) # dont la frequence est de 1000 (default)
pwm_bleu.duty_u16(0) # on lui donne une valeur comprise entre 0  et 65535 qui est converti entre 0 et 3.3v
pwm_vert = PWM(Pin(18,mode=Pin.OUT)) # on prescise au programme que la pin 15 est une sortie de type PWN
pwm_vert.freq(1_000) # dont la frequence est de 1000 (default)
pwm_vert.duty_u16(0) # 
pwm_rouge = PWM(Pin(17,mode=Pin.OUT)) # on prescise au programme que la pin 15 est une sortie de type PWN
pwm_rouge.freq(1_000) # dont la frequence est de 1000 (default)
pwm_rouge.duty_u16(0)


wlan = network.WLAN(network.STA_IF) # met la raspi en mode client wifi
wlan.active(True) # active le mode client wifi

ssid = 'SFR_BB00'
password = 'hdeq2ydt55pryc8tia33'
wlan.connect(ssid, password) # connecte la raspi au réseau
url = "https://hp-api.lainocs.fr/characters/cedric-diggory"

dico = {"Gryffindor":[7500,0,0],
        "Slytherin":[0,7500,0],
        "Hufflepuff":[12000,4000,0],
        "Ravenclaw":[0,0,7500]}


while not wlan.isconnected():
    print("pas co")
    utime.sleep(1)
    pass

while(True):
    try:
        print("GET")
        r = urequests.get(url) # lance une requete sur l'url
        print(r.json()["name"])
        print(r.json()["house"])
        # creer une variable stocker house
        maison=r.json()["lastHouseVisited"]
        pwm_rouge.duty_u16(dico[maison][0])
        pwm_vert.duty_u16(dico[maison][1])
        pwm_bleu.duty_u16(dico[maison][2])
        # led1.duty dico variable 0
        #led2
        #led3

        r.close() # ferme la demande
        utime.sleep(1)
    except Exception as e:
        print(e)