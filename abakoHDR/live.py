import cv2
from cement import * 
from time import sleep

cv2.namedWindow("preview", cv2.WINDOW_NORMAL)
vc = cv2.VideoCapture(0)
rval, frame = vc.read()
cv2.imshow("preview",frame)

counter = 0
while True:
	if frame is not None:   
		rval, frame_new = vc.read()
		frame = cement_squares(frame, frame_new) 
		cv2.imshow("preview", frame)
	if cv2.waitKey(1) & 0xFF == ord('r'):
		cv2.imwrite(str(counter) + '.png', frame)
		rval, frame = vc.read()
		counter += 1
