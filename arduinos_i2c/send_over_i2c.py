from smbus2 import SMBus

bus = SMBus(1) # indicates /dev/ic2-1
arduino1 = 5 # bus address
arduino2 = 6 # bus address

while(True):
    led1 = input("Arduino 1 on or off  ")
    bus.write_byte(arduino1, led1) # switch it on    
    led2 = input("Arduino 2 on or off  ")    
    bus.write_byte(arduino2, led2) # switch it on
    print("attempting to read...")
    try:
        print('From arduino 1: ',bus.read_byte(arduino1,0))        
        print('From arduino 2: ',bus.read_i2c_block_data(arduino2,0,3))
    except:
        pass
