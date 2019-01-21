import glob
import numpy as np
import cv2

image = cv2.imread('ss/ss1.png')
image = cv2.resize(image  , (480 , 256))
for img in glob.glob('ss/*.png'):
	img = cv2.imread(img)
	img = cv2.resize(img  , (480 , 256))
	w = img.shape[0]
        h = img.shape[1]
        for x in range(0,w-1):
		for y in range(0,h-1):
			if abs(image[x,y][0]-img[x,y][0])>=10:
				image[x,y][0] = 0;
			if abs(image[x,y][1]-img[x,y][1])>=10:
				image[x,y][1] = 0;
			if abs(image[x,y][2]-img[x,y][2])>=10:
				image[x,y][2] = 0;
cv2.imwrite("ss/croped/ss_crop_SC9.png",image)
