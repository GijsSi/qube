import time
import board
import neopixel
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN)
pixels = neopixel.NeoPixel(board.D21, 9)
ORDER = neopixel.RGB
r = 255

pattern = [[4], [3,4,5]]
color = [[0xff0000],[0xff0000 for c in range(3)]]

def turnoff_all():
    pixels.fill((0,0,0))

# wacht voor response
def wait (sec):
    sec *= 10
    for x in range (sec):
            time.sleep(0.1)
            if GPIO.input(18) == GPIO.HIGH:
                break

while True:
    if GPIO.input(18) == GPIO.HIGH:
        while GPIO.input(18) == GPIO.HIGH:
            for i in range(len(pattern)):
                for j in range(len(pattern[i])):
                    pixels[pattern[i][j]] = color[i][j] # vul patroon hier in
                if GPIO.input(18) == GPIO.LOW: # om patroon te interupten als niks gebeurd
                    turnoff_all() # haal deze lijn weg als je leds niet uit wil tijdens interupt
                    break
                time.sleep(60/200) # pas hier je delay aan
            turnoff_all()

    else:
        wait(5) # wacht 5 seconden voor interupt, anders stopt programma
        if GPIO.input(18) == GPIO.LOW:
            exit()