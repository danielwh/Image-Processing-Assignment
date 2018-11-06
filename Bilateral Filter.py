import numpy as np
import cv2

#Define the window name
windowName = "Bilateral Filter"

#Read in the first test image
img1 = cv2.imread('.\test1.png',cv2.IMREAD_GRAYSCALE)

#Ensure the image has loaded properly
if not img1 is None:
    #Apply the bilateral filter
    filtered1 = cv2.bilateralFilter(img1,5,50,50)
    #Display the filtered image
    cv2.imshow(windowName,filtered1)
    #Close the window when the user presses any key
    cv2.waitKey(0)
    cv2.destroyWindow(windowName)
else:
    #Print an error message if the image hasn't loaded
    print("Test image 1 not found.")

#Read in the second test image
img2 =cv2.imread('.\test2.png',cv2.IMREAD_COLOR)

#Ensure the image has loaded properly
if not img2 is None:
    #Apply the bilateral filter
    filtered2 = cv2.bilateralFilter(img2,5,50,50)
    #Display the filtered image
    cv2.imshow(windowName,filtered2)
    #Close the window when the user presses any key
    cv2.waitKey(0)
    cv2.destroyWindow(windowName)
else:
    #Print an error message if the image hasn't loaded
    print("Test image 2 not found.")
