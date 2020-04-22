import dlib
import cv2
from math import sqrt
predictor = dlib.shape_predictor('./shape_predictor_68_face_landmarks.dat')
detector = dlib.get_frontal_face_detector() #Load face detector

#Capture ảnh từ video 
vs = cv2.VideoCapture(0)

while True:
	#Lấy từng frame ảnh trong video thu được 
	check, frame = vs.read()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	dets = detector(gray, 0)  #Xác định vị trí khuôn mặt trong bức ảnh    
	
	#Vẽ khung detect khuôn mặt 
	for rect in dets:
		x = rect.left()
		y = rect.top()
		w = rect.right()
		h = rect.bottom()
		cv2.rectangle(frame, (x, y), (w, h), (0, 255, 0), 2)	
		landmark = predictor(gray, rect)

       # Xác định facial landmark trên khuôn mặt
		for idx,point in enumerate(landmark.parts()):
			#Đánh dấu các điểm neo 
			cv2.circle(frame,(point.x,point.y),1,(0,0,255),2)
			#Đánh dấu các điểm là mép mắt và đỉnh mũi 
			if idx==33 or idx==36 or idx==45:
				cv2.circle(frame,(point.x,point.y),1,(255,0,0),4)

	cv2.imshow('Face video', frame)
	key = cv2.waitKey(1)
	if key == ord('q'):
		break
cv2.destroyAllWindows
