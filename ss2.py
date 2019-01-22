import glob
import numpy as np
import cv2

image = cv2.imread('ss/ss1.png')
image_original = cv2.imread('ss/ss1.png')
cv2.imwrite("ss/croped/ss_crop_SC8.png",image)
image = cv2.resize(image  , (480 , 256))
for img in glob.glob('ss/*.png'):
	img = cv2.imread(img)
	img = cv2.resize(img  , (480 , 256))
	h = img.shape[0]
        w = img.shape[1]
        for x in range(0,w-1):
		for y in range(0,h-1):
			if abs(image[y,x][0]-img[y,x][0])>=10:
				image[y,x][0] = 0;
			if abs(image[y,x][1]-img[y,x][1])>=10:
				image[y,x][1] = 0;
			if abs(image[y,x][2]-img[y,x][2])>=10:
				image[y,x][2] = 0;
cv2.imwrite("ss/croped/ss_crop_SC9.png",image)

h = image.shape[0]
w = image.shape[1]
print(w,h,"width and height")

cv2.rectangle(image, (1, 1), (w/2, h/2), (255,0,0), 2)
cv2.rectangle(image, (w/2+1, 1), (w, h/2), (0,255,0), 2)
cv2.rectangle(image, (1, h/2+1), (w/2, h), (0,0,255), 2)
cv2.rectangle(image, (w/2+1, h/2+1), (w, h), (0,255,255), 2)

cv2.imwrite("ss/croped/ss_crop_SC10.png",image)

TL = TR = BL = BR = 0
for x in range(0,w-1):
	for y in range(0,h-1):
		if x<w/2 and y<h/2:
			TL+=image[y,x][0]+image[y,x][1]+image[y,x][2]
		elif x<w/2 and y>=h/2:
			BL+=image[y,x][0]+image[y,x][1]+image[y,x][2]
		elif x>=w/2 and y<h/2:
			TR+=image[y,x][0]+image[y,x][1]+image[y,x][2]
		else:
			BR+=image[y,x][0]+image[y,x][1]+image[y,x][2]
Max_density = max([TL,TR,BL,BR])
print([TL,TR,BL,BR])
if Max_density == TL:
	cv2.imwrite("ss/croped/ss_crop_TL_X1.png",image_original[0:200, 0:200])
	print("Top Left")
elif Max_density == TR:
	cv2.imwrite("ss/croped/ss_crop_TR_X1.png",image_original[0:200, 1720:1920])
	print("Top Right")
elif Max_density == BL:
	cv2.imwrite("ss/croped/ss_crop_BL_X1.png",image_original[880:1080, 0:200])
	print("Bottom left")
else:
	cv2.imwrite("ss/croped/ss_crop_BR_X1.png",image_original[880:1080, 1720:1920])
	print("Bottom Right")
