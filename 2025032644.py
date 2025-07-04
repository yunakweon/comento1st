import cv2 as cv

img = cv.imread('./nature.jpg')

Sobel1 = cv.Sobel(img, cv.CV_64F, 1, 0, ksize=3)
Sobel2 = cv.Sobel(img, cv.CV_64F, 0, 1, ksize=3)

Sobel1 = cv.convertScaleAbs(Sobel1)
Sobel2 = cv.convertScaleAbs(Sobel2)

cv.imshow('Original', img)
cv.imshow('Sobel1', Sobel1)
cv.imshow('Sobel2', Sobel2)

cv.waitKey()
cv.destoryAllWindows()
