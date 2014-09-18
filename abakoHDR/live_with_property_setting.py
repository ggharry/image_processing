import cv2
from cement import cement
from time import sleep

cv2.namedWindow("preview", cv2.WINDOW_NORMAL)
vc = cv2.VideoCapture(0)

rval, frame = vc.read()
cv2.imshow("preview",frame)
#sleep(5)

while True:
	if frame is not None:   
		rval, frame_new = vc.read()
		frame = cement(frame, frame_new) 
		cv2.imshow("preview", frame)
		cv2.imshow("preview", frame_new)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		#print vc.get(cv2.cv.CV_CAP_PROP_EXPOSURE)
		#print vc.VideoCapture.set(CV_CAP_PROP_EXPOSURE,30)
		#print vc.set(cv2.cv.CV_CAP_PROP_EXPOSURE,.1)
		break
