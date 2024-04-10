# Importing all necessary libraries 
import cv2 
import os 
  
# Read the video from specified path 
cam = cv2.VideoCapture("hello.mp4") 
  
try: 
      
    # creating a folder named data 
    if not os.path.exists('data'): 
        os.makedirs('data') 
  
# if not created then raise error 
except OSError: 
    print ('Error: Creating directory of data') 
  
# frame 
currentframe = 0

i = 0

while(True): 
      
    # reading from frame 
    ret,frame = cam.read() 
  
    if ret: 
        # if video is still left continue creating images 
        name = './data/frame' + str(currentframe) + '.jpg'
        print ('Creating...' + name) 
        if i not in range(0,5):
        # writing the extracted images 
            cv2.imwrite(name, frame) 
            i = 0
            # increasing counter so that it will 
            # show how many frames are created 
            currentframe += 1
        i+=1

    else: 
        break
  
# Release all space and windows once done 
cam.release() 
cv2.destroyAllWindows()