import numpy as np
import cv2


def rotate_bound(image, angle):
    (h, w) = image.shape[:2]
    (cX, cY) = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D((cX, cY), -angle, 1.0)
    cos = np.abs(M[0, 0])
    sin = np.abs(M[0, 1])
    nW = int((h * sin) + (w * cos))
    nH = int((h * cos) + (w * sin))
    M[0, 2] += (nW / 2) - cX
    M[1, 2] += (nH / 2) - cY
    return cv2.warpAffine(image, M, (nW, nH))


img = cv2.imread("ke.jpg")
angle=int(input("enter tne angle:"))
dst = rotate_bound(img, angle)
cv2.namedWindow('image', cv2.WINDOW_AUTOSIZE)
cv2.imshow('image', dst)
buffer = cv2.waitKey(0) & 0xFF
if buffer == 27:
    cv2.destroyWindow(dst)
elif buffer == ord('q'):
    cv2.destroyWindow(dst)
