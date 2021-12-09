import cv2
import numpy
import math

side_features = []
def select_point(event, x, y, flags, param):
	# grab references to the global variables
	global side_features
	# if the left mouse button was clicked, record the starting
	# (x, y) coordinates and indicate that cropping is being
	# performed
	if event == cv2.EVENT_LBUTTONDOWN:
	    side_features.append((x,y))

def main():
    img = cv2.imread("Riely_front.png")
    cv2.imshow("image",img)
    cv2.setMouseCallback('image',select_point)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
   

    return

if __name__ == "__main__":
    main()