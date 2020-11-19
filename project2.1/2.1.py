# -*- coding:utf-8 -*-
"""
created on 2020/11/18 14:45
@author WangChenghua
"""
import cv2
import numpy as np
import matplotlib


# function
def draw(img, x, y, x_b, y_b, r, g, b):
    x += int(x_b)
    y -= int(y_b)
    img[-y, x, 2] = r
    img[-y, x, 1] = g
    img[-y, x, 0] = b
    pass


def Brsenhamcircle(image, x_b, y_b, r_pixel, r, g, b):
    (x, y) = (r_pixel, 0)
    P_k = -2 * r_pixel + 3
    while x >= y:
        if P_k >= 0:
            P_k_next = P_k - 4 * x + 4 * y + 10
            (x_next, y_next) = (x - 1, y + 1)
        else:
            P_k_next = P_k + 4 * y + 6
            (x_next, y_next) = (x, y + 1)
        draw(image, x, y, x_b, y_b, r, g, b)
        draw(image, -x, y, x_b, y_b, r, g, b)
        draw(image, x, -y, x_b, y_b,r, g, b)
        draw(image, -x, -y, x_b, y_b, r, g, b)
        draw(image, y, x,x_b, y_b, r, g, b)
        draw(image, y, -x,x_b, y_b, r, g, b)
        draw(image, -y, x, x_b, y_b, r, g, b)
        draw(image, -y, -x, x_b, y_b, r, g, b)
        (x, y) = (int(x_next), int(y_next))
        P_k = P_k_next
    pass
    return image


def BresenhamLine(image_func, x1, y1, x2, y2, r, g, b):
    negative_y = False
    dx = x2 - x1
    if dx < 0:
        temp = x1
        x1 = x2
        x2 = temp
        temp = y2
        y2 = y1
        y1 = temp
        dx = x2 - x1
    dy = y2 - y1
    if dy < 0:
        negative_y = True
        dy = -dy
    x = x1
    y = y1
    if dx == 0:
        y = min(y1, y2)
        y_end = max(y1, y2)
        while y <= y_end:
            image_func[x, y, 2] = r
            image_func[x, y, 1] = g
            image_func[x, y, 0] = b
            y += 1
        return image_func
    elif dy == 0:
        while x <= x2:
            image_func[x, y, 2] = r
            image_func[x, y, 1] = g
            image_func[x, y, 0] = b
            x += 1
        return image_func
    else:
        k = dy / (1.0 * dx)
    if abs(k) <= 1:
        flag_k = True
        x_end = x2
    else:
        flag_k = False
        x_end = x1 + dy
        temp = dy
        dy = dx
        dx = temp
        k = dy / (1.0 * dx)
    e = 2 * dy - dx
    v = 2 * dy
    u = e - dx
    b = y1 - x1
    while x <= x_end:
        if flag_k:
            if negative_y:
                image_func[x, 2 * y1 - y, 2] = r
                image_func[x, 2 * y1 - y, 1] = g
                image_func[x, 2 * y1 - y, 0] = b
            else:
                image_func[x, y, 2] = r
                image_func[x, y, 1] = g
                image_func[x, y, 0] = b
        else:
            if negative_y:
                image_func[y - b, 2 * y1 - (x + b), 2] = r
                image_func[y - b, 2 * y1 - (x + b), 1] = g
                image_func[y - b, 2 * y1 - (x + b), 0] = b
            else:
                image_func[y - b, x + b, 2] = r
                image_func[y - b, x + b, 1] = g
                image_func[y - b, x + b, 0] = b
        if e > 0:
            y += 1
            e = e + u
        else:
            e = e + v
        x += 1
    return image_func


# function
img = cv2.imread("D:\AI_ML\pythonProject\project2.1\ke.jpg")
img_details = img.shape
print(img_details)
Putin_flag = True
x1_in = x2_in = y1_in = y2_in = 0
print("You can just print a line and a circle,press s can save this Picture")
while Putin_flag:
    print("to print a line")
    print("In this picture you can input max height{0},max weight{1}".format(img_details[0], img_details[1]))
    x1_in = int(input("X1:"))
    y1_in = int(input("Y1:"))
    x2_in = int(input("X2:"))
    y2_in = int(input("Y2:"))
    if x1_in > img_details[0] or y1_in > img_details[1] or x2_in > img_details[0] or y2_in > img_details[1]:
        print("Try again:")
        Putin_flag = True
    else:
        Putin_flag = False
Putin_flag2 = True
R = G = B = 0
while Putin_flag2:
    print("set color of this line")
    print("Enter a decimal number 0~255")
    R = int(input("RED:"))
    G = int(input("GREEN:"))
    B = int(input("BLUE:"))
    if R > 255 or G > 255 or B > 255:
        print("Try again:")
        Putin_flag2 = True
    else:
        Putin_flag2 = False
img = BresenhamLine(img, x1_in, y1_in, x2_in, y2_in, R, G, B)
line_flag = Putin_flag and Putin_flag2
Putin_flag = True
x3_in = y3_in = r_pixel = 0;
while Putin_flag:
    print("to print a circle")
    r_pixel = int(input("R_pixel:"))
    print("In this picture you can input max height{0},max weight{1}".format(img_details[0] - r_pixel,
                                                                             img_details[1] - r_pixel))
    x3_in = int(input("X:"))
    y3_in = int(input("Y:"))
    if x3_in > img_details[0] - r_pixel or y1_in > img_details[1] - r_pixel:
        print("Try again:")
        Putin_flag = True
    else:
        Putin_flag = False
Putin_flag2 = True
R = G = B = 0
while Putin_flag2:
    print("set color of this circle")
    print("Enter a decimal number 0~255")
    R = int(input("RED:"))
    G = int(input("GREEN:"))
    B = int(input("BLUE:"))
    if R > 255 or G > 255 or B > 255:
        print("Try again:")
        Putin_flag2 = True
    else:
        Putin_flag2 = False
circle_flag = Putin_flag and Putin_flag2
Brsenhamcircle(img, x3_in, y3_in, r_pixel, R, G, B)
if (not line_flag) and (not circle_flag):
    cv2.namedWindow('keduoli', cv2.WINDOW_NORMAL)
    cv2.imshow('keduoli', img)
    buffer = cv2.waitKey(0) & 0xFF
    if buffer == 27:
        cv2.destroyWindow(img)
    elif buffer == ord('s'):
        cv2.imwrite("D:\AI_ML\pythonProject\project2.1\myke.jpg", img)
        cv2.destroyWindow(img)
