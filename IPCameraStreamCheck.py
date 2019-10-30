import cv2

#video_capture = cv2.VideoCapture('IP of your camera')
def camera(ip):


	video_capture = cv2.VideoCapture(ip)
	while True:
		ret, frame = video_capture.read()
		
		cv2.imshow('frame', frame)
		if cv2.waitKey(1) == 27:

			print('Esc pressed exiting .....')
			cv2.destroyAllWindows()
			break


if __name__ == '__main__':

	import sys
	ip = sys.argv[1]
	if (len(ip) <= 2):
		ip = int(ip)
	else:
		ip = str(ip)
	camera(ip)