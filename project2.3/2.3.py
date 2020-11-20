import cv2
import numpy as np

WIN_NAME = "Test show"


# function
# @pt1=[x0,y0],pt2=[x1,y1]
# @color=[r,g,b]
def my_rectangle(image, pt1, pt2, color):
    for i in range(min(pt1[1], pt2[1]), max(pt1[1], pt2[1])):
        for j in range(0, 2):
            image[pt2[0], i, j] = color[j]
            image[pt1[0], i, j] = color[j]
    for i in range(min(pt1[0], pt2[0]), max(pt1[0], pt2[0])):
        for j in range(0, 2):
            image[i, pt1[1], j] = color[j]
            image[i, pt2[1], j] = color[j]


class pipin:
    judge_down = False
    copy_image = np.zeros((512, 512, 3), dtype=np.uint8)
    show_image = np.zeros((512, 512, 3), dtype=np.uint8)
    start_pt = (0, 0)


def on_mouse_draw(event, x, y, flags, param):
    pipin.judge_down = False
    if event == cv2.EVENT_LBUTTONDOWN and pipin.judge_down == False:
        pipin.start_pt = (y, x)
        print("START:Y={0},X={1}".format(y, x))
        pipin.judge_down = True
    if (event == cv2.EVENT_MOUSEMOVE) and (pipin.judge_down == True):
        pipin.show_image = pipin.copy_image
        end_pt = (y, x)
        my_rectangle(pipin.show_image, pipin.start_pt, end_pt, (0, 255, 0))
    if event == cv2.EVENT_LBUTTONUP:
        pipin.judge_down = False
        print("END:Y={0},X={1}".format(y, x))
        end_pt = (y, x)
        my_rectangle(pipin.show_image, pipin.start_pt, end_pt, (0, 255, 0))


if __name__ == '__main__':
    img = np.zeros((512, 512, 3), dtype=np.uint8)
    img_reverse = img.copy()
    cv2.namedWindow(WIN_NAME, 0)
    cv2.setMouseCallback(WIN_NAME, on_mouse_draw)
    while True:
        cv2.imshow(WIN_NAME, pipin.show_image)
        key = cv2.waitKey(30)
        if key == 27:  # ESC
            break
    cv2.destroyAllWindows()
