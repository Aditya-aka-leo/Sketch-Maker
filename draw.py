import cv2
import over_lapper as lp

img_path =input('Please Enter The Pic Path : ')
img = cv2.imread(img_path)
gray_scale = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  #convering the pic in to black and white so that we can have a sketch 
img_inv = cv2.bitwise_not(gray_scale) #to seperate the bright to low and low to bright 
img_smoothing = cv2.GaussianBlur(img_inv,(21,21),sigmaX=0,sigmaY=0) #smooting the inverted image using gaussian BLUR
output = lp.merger(gray_scale,img_smoothing)     #over lapping the images to get sketch effect just like a print from reel 
cv2.imwrite("sketch.jpg",output)






