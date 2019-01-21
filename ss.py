import glob
import numpy as np
import cv2

image = cv2.imread('ss1.png')
i = 0
for img in glob.glob("ss/*.png"):
    i=i+1
    n= cv2.imread(img)

    crop = n[0:200, 0:200]
    cv2.imwrite("ss/croped/ss_crop_TL_{0}.png".format(i),crop)

    crop = n[0:200, 1720:1920]
    cv2.imwrite("ss/croped/ss_crop_TR_{0}.png".format(i),crop)

    crop = n[880:1080, 0:200]
    cv2.imwrite("ss/croped/ss_crop_BL_{0}.png".format(i),crop)

    crop = n[880:1080, 1720:1920]
    cv2.imwrite("ss/croped/ss_crop_BR_{0}.png".format(i),crop)
