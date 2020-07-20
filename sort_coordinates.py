import cv2
import numpy as np
import imutils
import time
from imutils import contours
import sys

cv2.namedWindow("Sort",cv2.WINDOW_NORMAL)

img = cv2.imread("Test/"+sys.argv[1])

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5,5), 0)
canny = cv2.Canny(gray,100,220)

# thresh = cv2.threshold(gray, 110, 255,cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]

cnts = cv2.findContours(canny.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
out = img.copy()

print(len(cnts))
cnts,_ = contours.sort_contours(cnts)
ind=1
for (i,c) in enumerate(cnts):
	if cv2.contourArea(c)>55:
		box = cv2.minAreaRect(c)
		box = cv2.cv.BoxPoints(box) if imutils.is_cv2() else cv2.boxPoints(box)
		box = np.array(box, dtype="int")
		print(box)
		cv2.putText(out, "Object #{}".format(ind),(box[0][0],box[0][1]),cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.6, (0,0, 255),1)
		cv2.drawContours(out, [box], -1, (0, 255, 0), 2)
		ind+=1

    # cv2.drawContours(out, [c], -1, (0,255,0), 0)

cv2.imshow("Sort",out)
cv2.imwrite("Results/result_"+sys.argv[1],out)

cv2.waitKey(0)
cv2.destroyAllWindows()
