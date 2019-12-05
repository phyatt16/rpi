import gpiozero
import time

pinMS1 = gpiozero.DigitalOutputDevice(12)
pinMS2 = gpiozero.DigitalOutputDevice(16)
pinStep_y = gpiozero.DigitalOutputDevice(19)
pinDir_y =  gpiozero.DigitalOutputDevice(26)
pinStep_x = gpiozero.DigitalOutputDevice(21)
pinDir_x =  gpiozero.DigitalOutputDevice(20)

start = time.time()

pinMS1.on()
pinMS2.on()

def take_x_step(direction):
    if(direction<0):
        pinDir_x.value = 0
    else:
        pinDir_x.value = 1
        
    pinStep_x.on()
    time.sleep(.0005)
    pinStep_x.off()
    return

def take_y_step(direction):
    if(direction<0):
        pinDir_y.value = 0
    else:
        pinDir_y.value = 1
    pinStep_y.on()
    time.sleep(.0005)
    pinStep_y.off()
    return


def take_y_steps(direction=1,steps = 10):
    for i in xrange(0,steps):
        take_y_step(direction)
    return

def take_x_steps(direction=1,steps = 10):
    for i in xrange(0,steps):
        take_x_step(direction)
    return
    

if __name__=="__main__":

    # take_steps(1,8000)
    # take_steps(-1,8000)
    # take_steps(1,7000)
    # take_steps(-1,7000)
    # take_steps(1,6000)
    # take_steps(-1,6000)
    # take_steps(1,5000)
    # take_steps(-1,5000)
    # take_steps(1,4000)
    # take_steps(-1,4000)
    # take_steps(1,3000)
    # take_steps(-1,3000)

    sizes = [900, 800, 700, 600, 400, 300, 200, 100]

    for n in sizes:


        for i in xrange(n):
            take_x_steps(1,1)
            take_y_steps(1,1)
        for i in xrange(n):
            take_x_steps(-1,1)
            take_y_steps(1,1)
        for i in xrange(n):
            take_x_steps(-1,1)
            take_y_steps(-1,1)
        for i in xrange(n):
            take_x_steps(1,1)
            take_y_steps(-1,1)

    
        for i in xrange(n):
            take_x_steps(1,1)
            take_y_steps(1,1)
        for i in xrange(n):
            take_x_steps(1,1)
            take_y_steps(-1,1)
        for i in xrange(n):
            take_x_steps(-1,1)
            take_y_steps(-1,1)
        for i in xrange(n):
            take_x_steps(-1,1)
            take_y_steps(1,1)
            
    
        for i in xrange(n):
            take_x_steps(-1,1)
            take_y_steps(-1,1)
        for i in xrange(n):
            take_x_steps(1,1)
            take_y_steps(-1,1)
        for i in xrange(n):
            take_x_steps(1,1)
            take_y_steps(1,1)
        for i in xrange(n):
            take_x_steps(-1,1)
            take_y_steps(1,1)

    
        for i in xrange(n):
            take_x_steps(-1,1)
            take_y_steps(-1,1)
        for i in xrange(n):
            take_x_steps(-1,1)
            take_y_steps(1,1)
        for i in xrange(n):
            take_x_steps(1,1)
            take_y_steps(1,1)
        for i in xrange(n):
            take_x_steps(1,1)
            take_y_steps(-1,1)
        
        take_y_steps(1,n)
        take_x_steps(-1,n)    
        take_y_steps(-1,n)
        take_x_steps(1,n)
        
        take_y_steps(-1,n)
        take_x_steps(-1,n)    
        take_y_steps(1,n)
        take_x_steps(1,n)
        
        take_y_steps(1,n)
        take_x_steps(1,n)    
        take_y_steps(-1,n)
        take_x_steps(-1,n)
        
        take_y_steps(-1,n)
        take_x_steps(1,n)    
        take_y_steps(1,n)
        take_x_steps(-1,n)
