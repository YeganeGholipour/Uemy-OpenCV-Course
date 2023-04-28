import cv2
import numpy as np


###############
####VARIABLES##
###############

drawing = False # become true if the mouse is pressed down / False while mouse button is up

ix, iy = -1, -1

###############
####FUNCTION###
###############

def draw_rectangle(event, x, y, flags, params):
    
    global  ix, iy, drawing
    
    if event == cv2.EVENTLBUTTONDOWN: # this means you just started drawing the rectangle
        drawing = True
        ix, iy = x, y # keep track of where the mouse was located when we hit the left button down
        
    elif cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            cv2.rectangle(img,(ix,iy), (x,y), (0,255,0), -1)
            
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.rectangle(img,(ix,iy), (x,y), (0,255,0), -1)
        

################################
###SHOWING IMAGE WITH OPENCV####
################################

img = np.zeros((512,512,3),int32)

cv2.namedWindow(winname='my_drawing')

cv2.setMouseCallback('my_drawing', draw_rectangle)

while True:
    
    cv2.imshow('my_drawing', img)
    
    if cv2.waitKey(1) & 0xFF == 27:
        break
        
cv2.destroyAllWindows()