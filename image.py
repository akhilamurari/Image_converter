#import numpy as np
#import cv2
#img=cv2.imread('img1.jpg',0)
#cv2.namedWindow('image')
#cv2.imshow('image',img)
#cv2.waitKey(0) & 0xFF
#cv2.destroyAllWindows()
#k==cv2.waitKey(0)
#if k==30:
#	 cv2.destroyAllWindows()
#else k==ord('s'):
#	cv2.imwrite('img2.jpg',img)
#	cv2.destroyAllWindows()
import numpy as np
import cv2
img = cv2.imread('img1.jpg',0)
cv2.imshow('image',img)
k = cv2.waitKey(0)
if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save and exit
    cv2.imwrite('messigray.jpg',img)
    cv2.destroyAllWindows()
