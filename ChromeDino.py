import sys
import os
import pyautogui
import time
import math


def main():
    # Get the value pixels in the image
    def getDims(Image,x, y):
        img = Image.load()
        return img[x, y]
    
    
    # Screen Dims
    top_dim, left_dim, width_dim, height_dim = 293, 0, 1920, 465
    
    # Keeping track of time
    last = 0
    total_time = 0
    
    y_search1, x_search1, x_search2 = 350, 435, 450 # Cactus Check
    y_search2 = 275 # Bird Check (Only vertical checking)
    
    
    # Counter for game starting
    i = 5
    while(i > 0):
        print("Game is starting in ",i)
        time.sleep(1)
        i -= 1
    
    while True:
        t1 = time.time()
    
        # manage the acceleration as the game progresses
        if math.floor(total_time) != last:
            x_search2 += 4
            if x_search2 >= width_dim:
                x_search2 = width_dim
            last = math.floor(total_time)
    
        # Take a screen shot
        screenshot = pyautogui.screenshot(region=(left_dim,top_dim, width_dim, height_dim))
        
        # Get the color of the background
        bgColor = getDims(screenshot, 440, 30)            
    
        for i in reversed(range(x_search1, x_search2)):
            # Check for the obstacle
            if getDims(screenshot,i,y_search1) != bgColor\
                    or getDims(screenshot,i,y_search2) != bgColor:
                pyautogui.keyDown(' ')
                break
    
        t2 = time.time()-t1                       
        total_time += t2
    
        # Verifying the coordinates
        print(x_search2)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)