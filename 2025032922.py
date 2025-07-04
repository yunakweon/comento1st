import cv2 as cv

img = cv.imread('./nature.jpg')

# X 방향 미분
Sobel_x = cv.Sobel(img, cv.CV_64F, 1, 0, ksize=3)
Sobel_x = cv.convertScaleAbs(Sobel_x)

# Y 방향 미분
Sobel_y = cv.Sobel(img, cv.CV_64F, 0, 1, ksize=3)
Sobel_y = cv.convertScaleAbs(Sobel_y)

# X, Y 방향을 합침
Sobel = cv.addWeighted(Sobel_x, 0.5, Sobel_y, 0.5, 0)

cv.imshow('Original', img)
cv.imshow('Sobel X', Sobel_x)
cv.imshow('Sobel Y', Sobel_y)
cv.imshow('Sobel', Sobel)

cv.waitKey(0)
cv.destroyAllWindows()
