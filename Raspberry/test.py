#!/usr/bin/python

import sys
import cv2
import math
import subprocess

if __name__ == '__main__':

    #target in camera
    CenterX = 426.5
    CenterY = 190.5
    Radius = 40.0

    width = 800
    height = 640
    capture = cv2.VideoCapture(0)
    capture.set(3, width);
    capture.set(4, height);
    
    image = cv2.imread("target.jpg", cv2.CV_LOAD_IMAGE_COLOR)
    target_x = float(image.shape[0])*0.5
    target_y = float(image.shape[1])*0.5
    target_Radius = min(target_x,target_y)
    
    target = image.copy()
    cv2.namedWindow("Result", 1)
    cv2.imshow("Result", target)

    ShotCount = int();
    Scoore = 0;
    
    while 1:
        if cv2.waitKey(1) >= 0:
            break
        ret,frame = capture.read()
        grey_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        ret,grey_image = cv2.threshold(grey_image, 245, 255, cv2.THRESH_BINARY)
        
#        grey_image = cv2.erode(grey_image, None, iterations = 1)
#        grey_image = cv2.dilate(grey_image, None, 0)

        (contour, _) = cv2.findContours(grey_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        
        if contour:
            subprocess.Popen('aplay Shot.wav', shell = True)
            cntr = sorted(contour, key = cv2.contourArea, reverse = True)[0]
            (x,y), radius = cv2.minEnclosingCircle(cntr)
            center = (x, y)
            shot_x = (float(x) - CenterX)/Radius
            shot_y = (float(y) - CenterY)/Radius
            dist = math.sqrt(shot_x*shot_x+shot_y*shot_y)
            shot_x = target_x + shot_x*target_Radius
            shot_y = target_y + shot_y*target_Radius
            Shot = (int(shot_x), int(shot_y))
            cv2.circle(target, Shot, 5, (60,60,255),10)
            cv2.circle(target, Shot, 10, (120,120,120),1)
            cv2.imshow("Result", target)
            #calibrate
            #print (center, dist)
            print ("Shots", ShotCount+1)
            if dist < 1.0:
                Scoore += 1 - dist
            ShotCount += 1
            if ShotCount > 6:
                ShotCount = 0;
                Scoore = Scoore/7.0*100.0
                print("You Scoore: ", Scoore)
                Scoore = 0
                target = image.copy()
                cv2.waitKey(300)
                subprocess.Popen('aplay 924.wav', shell = True)
                cv2.waitKey(1000)
            cv2.waitKey(50)

    cv2.destroyAllWindows()
