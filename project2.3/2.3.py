import cv2
import numpy as np
import random
import copy

WIN_NAME = "Test show"


# function
# @pt1=[x0,y0],pt2=[x1,y1]
# @color=[r,g,b]
def my_rectangle(image, pt1, pt2, color):
    for i in range(min(pt1[1], pt2[1]), max(pt1[1], pt2[1])):
        for j in range(0, 3):
            image[pt2[0], i, j] = color[j]
            image[pt1[0], i, j] = color[j]
    for i in range(min(pt1[0], pt2[0]), max(pt1[0], pt2[0])):
        for j in range(0, 3):
            image[i, pt1[1], j] = color[j]
            image[i, pt2[1], j] = color[j]


def color_change():
    ret = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    return ret


class pipin(object):
    def __init__(self):
        self.judge_down = False
        self.copy_image = np.zeros((512, 512, 3), dtype=np.uint8)
        self.show_image = np.zeros((512, 512, 3), dtype=np.uint8)
        self.start_pt = (0, 0)
        self.mouse_move = False

    def reset_image(self):
        self.show_image = self.copy_image

    def set_image(self):
        self.copy_image = self.show_image


def on_mouse_draw(event, x, y, flags, param):
    if mypipin.mouse_move:
        mypipin.reset_image()
        mypipin.show_image = np.zeros((512, 512, 3), dtype=np.uint8)
    if event == cv2.EVENT_LBUTTONDOWN and mypipin.judge_down == False:
        mypipin.start_pt = (y, x)
        print("START:Y={0},X={1}".format(y, x))
        mypipin.judge_down = True
        mypipin.mouse_move = True
    if event == cv2.EVENT_MOUSEMOVE and mypipin.judge_down == True:
        end_pt = (y, x)
        my_rectangle(mypipin.show_image, mypipin.start_pt, end_pt, color_change())
    if event == cv2.EVENT_LBUTTONUP:
        mypipin.mouse_move = False
        mypipin.judge_down = False
        print("END:Y={0},X={1}".format(y, x))
        end_pt = (y, x)
        my_rectangle(mypipin.show_image, mypipin.start_pt, end_pt, color_change())
        mypipin.set_image()


if __name__ == '__main__':
    mypipin = pipin()
    # img = np.zeros((512, 512, 3), dtype=np.uint8)
    # img_reverse = img.copy()
    cv2.namedWindow(WIN_NAME, 0)
    cv2.setMouseCallback(WIN_NAME, on_mouse_draw)
    while True:
        cv2.imshow(WIN_NAME, mypipin.show_image)
        key = cv2.waitKey(30)
        if key == 27:  # ESC
            break
    cv2.destroyAllWindows()
