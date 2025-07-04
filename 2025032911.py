import cv2 as cv

img = cv.imread('./nature.jpg')

# Sobel을 한 번에 적용 (dx=1, dy=1)
Sobel = cv.Sobel(img, cv.CV_64F, 1, 1, ksize=3)
Sobel = cv.convertScaleAbs(Sobel)

cv.imshow('Original', img)
cv.imshow('Sobel', Sobel)

cv.waitKey(0)
cv.destroyAllWindows()
