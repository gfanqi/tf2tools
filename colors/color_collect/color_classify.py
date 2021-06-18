import numpy as np

x = np.arange(256)
y = np.arange(256)
z = np.arange(256)


def repeat(x):
    x = np.expand_dims(x, -1)
    x = np.tile(x, 10)
    x = x.flatten()
    return x


x = repeat(x)
y = repeat(y)
# b = repeat(b)
x, y = np.meshgrid(x, y)
x = np.expand_dims(x, axis=-1)
y = np.expand_dims(y, axis=-1)
# z = np.ones_like(x, ) * 127

print(x.shape, y.shape)
img = np.concatenate((x, z, y), axis=-1)

import cv2
cv2.imshow("",np.squeeze(img))
cv2.waitKey()
# cv2.imwrite('color.jpg', img)
