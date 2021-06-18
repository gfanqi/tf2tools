import cv2
import numpy as np

X = Y = Z = np.arange(0, 255, )
X, Y = np.meshgrid(X, Y)
# rgb_space = np.stack([X,Y,Z],axis=-1)
# transform = np.matmul(rgb_space,np.array([1,-1,1]))+255

# for i in range(254,0,-1):
#     img = rgb_space[i]
#     cv2.imshow("",img.astype(np.uint8))
#     cv2.waitKey(0)

# print(transform)
# print(transform.shape)

src = np.array([0,0],
               [0,255],
               [255,255],
               )
dst = np.array([[0,0,],
                [0, 255],
                [255, 255],
                ])


for i in range(-254, 255):
    # i = 510-i
    Z = i - X + Y
    rgb_space = np.stack([X, Y, Z], axis=-1)
    rgb_space[rgb_space[..., -1] > 255] = 0
    rgb_space[rgb_space[..., -1] < 0] = 0
    # print(rgb_space[:,:,-1])
    img = rgb_space.copy()
    img = img[ -i:255,0:i + 255 ]
    # print(rgb_space.shape)

    img = img.astype(np.uint8)
    img = cv2.resize(img, dsize=(255, 255))

    img = img[...,::-1]
    # cv2.imshow("{}", img)
    # cv2.waitKey(1)
    cv2.imwrite("{}.jpg".format(i+255),img)