import gpiozero
import time

if __name__=="__main__":

    pinMS1 = gpiozero.DigitalOutputDevice(12)
    pinMS2 = gpiozero.DigitalOutputDevice(16)
    # pinStep = gpiozero.DigitalOutputDevice(17)
    pinStep = gpiozero.DigitalOutputDevice(21)
    pinDir1 =  gpiozero.DigitalOutputDevice(20)
    pinDir2 =  gpiozero.DigitalOutputDevice(4)

    start = time.time()


    pinMS1.off()
    pinMS2.on()
    down=False
    left=False
    time.sleep(1)
    pinStep.frequency = 500
    pinStep.value = .5    
    while time.time()-start<100:
        if pinStep.frequency > 8000:
            down = True
        if pinStep.frequency <= 1000:
            down = False
        if time.time()-start>.3:
            left= not left
            start = time.time()

        if left:
            pinDir2.on()
        else:
            pinDir2.off()

        if down==False:
            pinStep.frequency = pinStep.frequency+50
        else:
            pinStep.frequency = pinStep.frequency-50
        print pinStep.frequency
        
        time.sleep(.1)
