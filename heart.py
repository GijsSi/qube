import Adafruit_ADS1x15
import serial
import time
import board
import neopixel

pattern = [[58,68,57,62,67,61],[59,69,53,58,63,68,73,52,57,62,67,72,56,61,66,60,]]

def turnoff_all():
    pixels.fill((0,0,0))

# wacht voor response
def wait (sec):
    sec *= 10
    for x in range (sec):
            time.sleep(0.1)
            if read_pulse > 0:
                break


def read_pulse():
    firstBeat = True
    secondBeat = False
    sampleCounter = 0
    lastBeatTime = 0
    lastTime = int(time.time() * 1000)
    th = 525
    P = 512
    T = 512
    IBI = 600
    Pulse = False
    adc = Adafruit_ADS1x15.ADS1015()
    while True:

        Signal = adc.read_adc(0, gain=GAIN)
        curTime = int(time.time() * 1000)
        sampleCounter += curTime - lastTime
        lastTime = curTime
        N = sampleCounter - lastBeatTime

        if Signal > th and Signal > P:
            P = Signal

        if Signal < th and N > (IBI / 5.0) * 3.0:
            if Signal < T:
                T = Signal

        if N > 250:
            if (Signal > th) and (Pulse == False) and (N > (IBI / 5.0) * 3.0):
                Pulse = 1;
                IBI = sampleCounter - lastBeatTime
                lastBeatTime = sampleCounter

                if secondBeat:
                    secondBeat = False;
                    for i in range(0, 10):
                        rate[i] = IBI

                if firstBeat:
                    firstBeat = False
                    secondBeat = True
                    continue

                runningTotal = 0;
                for i in range(0, 9):
                    rate[i] = rate[i + 1]
                    runningTotal += rate[i]

                rate[9] = IBI;
                runningTotal += rate[9]
                runningTotal /= 10;
                BPM = 60000 / runningTotal
                return BPM

        if Signal < th and Pulse == 1:
            amp = P - T
            th = amp / 2 + T
            T = th
            P = th
            Pulse = 0

        if N > 2500:
            th = 512
            T = th
            P = th
            lastBeatTime = sampleCounter
            firstBeat = False
            secondBeat = False
            return 0


while True:
    if read_pulse() > 0:
        while read_pulse() > 0:
            for i in range(len(pattern)):
                for j in range(len(pattern[i])):
                    pixels[pattern[i][j]] = (255,0,0) # vul patroon hier in
                if read_pulse() == 0: # om patroon te interupten als niks gebeurd
                    turnoff_all() # haal deze lijn weg als je leds niet uit wil tijdens interupt
                    break
                time.sleep(60/read_pulse()) # pas hier je delay aan
            turnoff_all()

    else:
        wait(5) # wacht 5 seconden voor interupt, anders stopt programma
        if read_pulse() == 0:
            exit()
