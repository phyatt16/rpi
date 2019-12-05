import gpiozero
import numpy as np
import time
import curses
import cv2

cam = cv2.VideoCapture(0)
cv2.namedWindow('RaspberryPi')

screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)

if __name__=="__main__":

    pinNumber1 = 17
    pinNumber2 = 27
    
    initialAngle = 0
    minAngle = -90
    maxAngle = 90
    min_pulse_width = 500/1e6
    max_pulse_width = 2400/1e6
    servo1 = gpiozero.AngularServo(pinNumber1,
                                  initialAngle,
                                  minAngle,
                                  maxAngle,
                                  min_pulse_width,
                                  max_pulse_width)

    servo2 = gpiozero.AngularServo(pinNumber2,
                                  initialAngle,
                                  minAngle,
                                  maxAngle,
                                  min_pulse_width,
                                  max_pulse_width)
    


    def get_jacobian(q):
        l1 = 1
        l2 = 1
        jac = np.array([[-l1*np.sin(q[0])-l2*np.sin(q[0]+q[1]), -l2*np.sin(q[0]+q[1])],
                        [l1*np.cos(q[0])+l2*np.cos(q[0]+q[1]), l2*np.cos(q[0]+q[1])]])

        jac = np.reshape(jac,[2,2])
        
        return jac

    def get_fk(q):
        l1 = 1
        l2 = 1

        x = np.array([[l1*np.cos(q[0]) + l2*np.cos(q[0]+q[1])],
                      [l1*np.sin(q[0]) + l2*np.sin(q[0]+q[1])]])

        x = np.reshape(x,[2,1])
                      
        return x

    
    def do_inv_kinematics(x_goal,q_cur):

        q = np.reshape(q_cur,[2,1])
        x = get_fk(q)
        count = 0
        while np.linalg.norm(x_goal-x) >.01 and count < 100:
            J = get_jacobian(q)
            J_inv = np.linalg.pinv(J+np.eye(2)*0.1)
            xdot = (x_goal-x)*.1
            qdot = np.matmul(J_inv,xdot)
            q = q + qdot*.001
            x = get_fk(q)
            count += 1

        q = np.reshape(q,[2,1])

        return q
    

    def command_jangles(q):
        try:
            servo1.angle = q[0,0]*180.0/np.pi
            servo2.angle = -q[1,0]*180.0/np.pi
        except:
            print "Commanded joint angle outside of limits: ",q

    q = np.array([[np.pi/4],
                  [-np.pi/4]])
    x = get_fk(q)    
    command_jangles(q)

    delta_x = .1
    while True:

        ret,frame = cam.read()
        frame = cv2.resize(frame,(50,50))
        cv2.imshow('RaspberryPi',frame)
        k = cv2.waitKey(1)
        
        char = screen.getch()
        if char == ord('q'):
            break
        elif char == curses.KEY_RIGHT:
            x_goal = x + delta_x*np.array([[1],
                                       [0]])
        elif char == curses.KEY_LEFT:
            x_goal = x + delta_x*np.array([[-1],
                                       [0]])
            
        elif char == curses.KEY_UP:
            x_goal = x + delta_x*np.array([[0],
                                       [1]])

        elif char == curses.KEY_DOWN:
            x_goal = x + delta_x*np.array([[0],
                                       [-1]])
        else:            
            x_goal = x


        # Do IK
        q = do_inv_kinematics(x_goal,q)
        x = get_fk(q)

        # Don't
        # J = get_jacobian(q)
        # J_inv = np.linalg.pinv(J+np.eye(2)*0.0001)
        # xdot = (x_goal-x)
        # qdot = np.matmul(J_inv,xdot)
        # q = q + qdot*.1

        print_q = 180.0/np.pi*q.flatten()

        print "q: ",print_q.tolist()

        command_jangles(q)

    curses.endwin()
        

