# -*- coding: utf-8 -*-

import cv2
import numpy as np

WIN_NAME = 'pick_points'


def onmouse_pick_points(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print('x = %d, y = %d' % (x, y))
        cv2.drawMarker(param, (x, y), (0, 255, 0))


if __name__ == '__main__':
    image = np.zeros((512, 512, 3), np.uint8)
    cv2.namedWindow(WIN_NAME, 0)
    cv2.setMouseCallback(WIN_NAME, onmouse_pick_points, image)
    while True:
        cv2.imshow(WIN_NAME, image)
        key = cv2.waitKey(30)
        if key == 27:  # ESC
            break
    cv2.destroyAllWindows()