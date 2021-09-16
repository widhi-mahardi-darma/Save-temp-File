####### Using save file on temp ########

# install open CV : pip install opencv-python
# install temp : pip install temp


import tempfile
import cv2
import os
from tempfile import NamedTemporaryFile, SpooledTemporaryFile

# import image
img=cv2.imread('Image.tif')

# path temp
path = tempfile.gettempdir()
cv2.imwrite(os.path.join(path, 'Image_temp.jpg'), img)

# input image from temp
img = cv2.imread(os.path.join(path, 'Image_temp.jpg'))

# show image
cv2.imshow('Image temp', img)
cv2.waitKey()
cv2.destroyAllWindows()
