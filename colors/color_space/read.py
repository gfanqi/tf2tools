from pprint import pprint

import cv2
import numpy as np
from collections import Counter

image = "2.png"
img = cv2.imread(image)
img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
img = (img * np.array([[2, 1 / 2.55, 1 / 2.55]])).astype(np.int)
img = list(np.reshape(img, [-1, 3]))
img_tuple = [tuple(item) for item in img]

pprint(Counter(img_tuple))
