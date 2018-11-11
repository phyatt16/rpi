import gpiozero
import time

if __name__=="__main__":

    pinNumber = 17
    initialAngle = 0
    minAngle = -90
    maxAngle = 90
    min_pulse_width = 500/1e6
    max_pulse_width = 2400/1e6
    servo = gpiozero.AngularServo(pinNumber,
                                  initialAngle,
                                  minAngle,
                                  maxAngle,
                                  min_pulse_width,
                                  max_pulse_width)

    servo.angle = -90

    # Show the range
    while servo.angle < 90:
        servo.angle += 1
        time.sleep(.01)

    while servo.angle > -90:
        servo.angle -= 1
        time.sleep(.01)

    while True:
        angle = input("Enter an angle between -90 and 90    ")

        servo.angle = angle
