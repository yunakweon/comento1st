import cv2 as cv

img1 = cv.imread('IU1.jpg')
img2 = cv.imread('IU2.jpeg')

ORB = cv.ORB_create()

kp1, des1 = ORB.detectAndCompute(img1, None)
kp2, des2 = ORB.detectAndCompute(img2, None)

#FLANN_INDEX_KDTREE = 1
#index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
#search_params = dict(checks=50)
#matcher = cv.FlannBasedMatcher(index_params)

FLANN_INDEX_LSH = 6
index_params = dict(algorithm=FLANN_INDEX_LSH, table_number=6, key_size=12, multi_probe_level=1)
search_params = dict(checks=50)
matcher = cv.FlannBasedMatcher(index_params, search_params)  # search_params 추가

matches = matcher.match(des1, des2)
matches = sorted(matches, key=lambda x:x.distance)
good_matches = matches[:30]

img3 = cv.drawMatches(img1, kp1, img2, kp2, good_matches, None, flags=2)
img3 = cv.resize(img3, dsize=(0,0), fx=0.3, fy=0.3, interpolation=cv.INTER_LINEAR)
cv.imshow("Matching result", img3)
cv.waitKey(0)
cv.destroyAllWindows()