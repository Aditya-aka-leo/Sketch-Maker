import cv2
def merger(x,y):
    return cv2.divide(x,255-y,scale=256)

