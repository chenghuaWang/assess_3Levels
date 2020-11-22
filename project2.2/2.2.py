# -*- coding:utf-8 -*-
"""
created on 2020/11/20 14:42
@author WangChenghua
"""
import numpy as np
import cv2


# function
# f(i+u,j+v) = (1-u)(1-v)f(i,j) + (1-u)vf(i,j+1) + u(1-v)f(i+1,j) + uvf(i+1,j+1)
def my_bilinear_interpolation(image_func, ori2aim):
    pic_h, pic_w, pic_channel = image_func.shape
    aim_h, aim_w = int(ori2aim[1]), int(ori2aim[0])
    # special judge
    if pic_h == aim_h and pic_w == aim_w:
        return image_func.copy()
    # init dtype=uint8 means 0~255
    aim_pic = np.zeros((aim_h, aim_w, pic_channel), dtype=np.uint8)
    rate_x, rate_y = float(pic_w) / aim_w, float(pic_h) / aim_h
    for aim_y in range(aim_h):
        for aim_x in range(aim_w):
            for i in range(pic_channel):
                # SrcX=(dstX+0.5)* (srcWidth/dstWidth) -0.5
                # SrcY=(dstY+0.5) * (srcHeight/dstHeight)-0.5
                # To center justification
                pic_x = (aim_x + 0.5) * rate_x - 0.5
                pic_y = (aim_y + 0.5) * rate_y - 0.5
                pic_x0 = int(np.floor(pic_x))
                pic_y0 = int(np.floor(pic_y))
                pic_x1 = min(pic_x0 + 1, pic_w - 1)
                pic_y1 = min(pic_y0 + 1, pic_h - 1)
                # caculate
                temp0 = (pic_x1 - pic_x) * img[pic_y0, pic_x0, i] + (pic_x - pic_x0) * img[pic_y0, pic_x1, i]
                temp1 = (pic_x1 - pic_x) * img[pic_y1, pic_x0, i] + (pic_x - pic_x0) * img[pic_y1, pic_x1, i]
                aim_pic[aim_y, aim_x, i] = int((pic_y1 - pic_y) * temp0 + (pic_y - pic_y0) * temp1)
        cv2.imshow('keduoli', aim_pic)
        key = cv2.waitKey(1)
    return aim_pic


img = cv2.imread("D:\AI_ML\pythonProject\project2.2\ke.jpg")
flag_out = True
while flag_out:
    print("you can just put in integer")
    out_times = int(input("Enter the rate(negative number is to shrink the picture,you cant enter 0):"))
    if out_times == 0:
        print("try again!")
    else:
        flag_out = False
if out_times < 0:
    out_times=-out_times
    print("running")
    print("After window displayed,you can press s to save the photo")
    cv2.namedWindow('keduoli', cv2.WINDOW_NORMAL)
    img2 = my_bilinear_interpolation(img, (img.shape[1]/out_times, img.shape[0]/out_times))
else:
    print("running")
    print("After window displayed,you can press s to save the photo")
    cv2.namedWindow('keduoli', cv2.WINDOW_NORMAL)
    img2 = my_bilinear_interpolation(img, (img.shape[1]*out_times, img.shape[0]*out_times))
print("success")
#cv2.namedWindow('keduoli', cv2.WINDOW_NORMAL)
cv2.imshow('keduoli', img2)
buffer = cv2.waitKey(0) & 0xFF
if buffer == 27:
    cv2.destroyWindow(img)
elif buffer == ord('s'):
    cv2.imwrite("D:\AI_ML\pythonProject\project2.2\mydke.jpg", img2)
    cv2.destroyWindow(img)
