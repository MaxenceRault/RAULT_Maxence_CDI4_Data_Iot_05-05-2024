import network
import urequests
import ujson
import utime
from machine import Pin, PWM

wlan = network.WLAN(network.STA_IF)
wlan.active(True)

ssid = 'SFR_BB00'
password = 'hdeq2ydt55pryc8tia33'
wlan.connect(ssid, password)

maisons = {
    
    "Gryffindor": [35000,0,0],
    "Slytherin": [0, 35000,0],
    "Hufflepuff": [35000,35000,0],
    "Ravenclaw":[0,0,35000]
    }
pwm_ledR = PWM(Pin(17, mode=Pin.OUT))
pwm_ledG = PWM(Pin(18, mode=Pin.OUT))
pwm_ledB = PWM(Pin(19, mode=Pin.OUT))
pwm_ledR.freq(1_000)
pwm_ledG.freq(1_000)
pwm_ledB.freq(1_000)

while not wlan.isconnected():
    print("not connected")
    utime.sleep(1)
    
while True:
    
    print("GET")
    url= "http://192.168.1.50:3000	"
    print(url)
    response = urequests.get(url)
    print(response)
    
    house = response.json()["lastHouseVisited"]
    response.close()
    
    print(house)
    utime.sleep(1)
    
    pwm_ledR.duty_u16(maisons[house][0])
    pwm_ledG.duty_u16(maisons[house][1])
    pwm_ledB.duty_u16(maisons[house][2])