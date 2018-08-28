import cv2
import numpy as np
img=np.zeros((512,512,3),np.uint8)


pts1=np.array([[10,500],[55,250],[140,500]],np.int32)


cv2.polylines(img,[pts1],True,(0,255,0),3)



cv2.imshow('polygone',img)

cv2.waitKey(0)
cv2.destroyAllWindows()
