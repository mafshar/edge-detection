import numpy as np
import cv2
from PIL import Image, ImageDraw
import matplotlib.pyplot as plt

image = cv2.imread('corner.jpg')
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)


imgc = np.float32(gray)
edges = cv2.Canny(gray, 100,200)

plt.imshow(edges, 'Greys')
plt.show()

dst = cv2.cornerHarris(imgc,2,3,0.4)

dst = cv2.dilate(dst,None)


#######hough lines#############
minLine = 100
maxGap = 10


segs = cv2.HoughLinesP(edges,8,np.pi/180,100,minLine,maxGap,75)

print len(segs)
#plt.imshow(dst,'Greys')
#plt.show()

for x1,y1,x2,y2 in segs[0]:
	cv2.line(image,(x1,y1),(x2,y2),(255,0,0),2)

plt.imshow(image)
plt.show()