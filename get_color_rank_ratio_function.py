import matplotlib.pyplot as plt
import numpy
import numpy as np
from mayavi import mlab
from mayavi.tools.helper_functions import plot3d
from statsmodels.regression.linear_model import OLS
from statsmodels.tools import add_constant

import pandas as pd

mydata = pd.read_excel("手镯价格标准.xlsx", header=[0, 1], index_col=[0])

zhong = mydata.index.tolist()
rank = mydata


value = []
for column in mydata.columns:
    # pprint()
    data = mydata[column]
    # print(data)
    x = data.index.values
    y = data.values
    # y = np.exp(y)
    x = np.exp(-x)
    result = OLS(y,x)
    fit_result = result.fit()
    value.append(list(column)+fit_result.params.tolist())
    pass

print(value)
value_df = pd.DataFrame(value)

value_df.to_csv("./function.csv")

# my_array = np.stack([X, Y, Z], axis=-1)
# my_array = np.reshape(my_array,newshape=(-1,3))

# x = X.flatten()
# y = Y.flatten()
# z = Z.flatten()
# z = z / 1000
# print(my_array)
# print(X.shape, Y.shape, Z.shape)
# l = mlab.plot3d(Y, X, Z, representation='points', line_width=5.0)
# print(mlab.plot3d.__doc__)
# mlab.show()
# # fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# ax.wireframe(Y, X, Z,c=Z)
# wireframe
# plt.show()
# plt.imshow()

mydata = pd.read_csv("function.csv", index_col=[0])

x = mydata.index.values
y = np.array([1, 2, 3])

# np.polyfit()

plt.scatter(x,mydata["2"])
plt.show()



# input()
# input()

# y = y * 41-41
# print(np.max(x) - np.min(x))
# print(np.max(x) - np.min(x))
# input()
y, x = np.meshgrid(y, x)
z = mydata.values
x3 = x ** 3
x2y = x ** 2 * y
xy2 = x * y ** 2
y3 = y ** 3
# print(x.shape)
x2 = x ** 2
xy = x * y
y2 = y ** 2


def get_k(S_rank, ratio):
    # S_rank = S_rank*27
    # ratio = ratio*27
    # w = np.array([574334.4935520831,
    #               2.8060436531586435,
    #               -42.49682821730144,
    #               24502.003296781317,
    #               80501.80429399505,
    #               -23.74408781360745,
    #               -148754.8887563243,
    #               -294211.73274944414,
    #               231064.27533247884,
    #               145475.88732016546])
    w = np.array(
        [574334.4935520831, 2.8060436531586435, -42.49682821730144, 24502.003296781317, 80501.80429399505, -23.74408781360745, -148754.8887563243, -294211.73274944414, 231064.27533247884, 145475.88732016546])

    def exp(a, b):
        return ratio ** a * S_rank ** b

    array = np.array([
        1,
        exp(3, 0),
        exp(2, 1),
        exp(1, 2),
        exp(0, 3),

        exp(2, 0),
        exp(1, 1),
        exp(0, 2),
        exp(1, 0),
        exp(0, 1)
    ])

    # print(w.shape,array.shape)
    return np.matmul(w, array)


print(get_k(1, 0.8))

# input()
# data = [x3, x2y, xy2, y3, x2, xy, y2, x, y, ]
data = [x3, x2y, xy2, y3, x2, xy, y2, x, y, ]
data = [item.flatten() for item in data]
# print(data)
data = np.array(data).T
#
# for item in data:
#     print(item.shape)

data = pd.DataFrame(data, columns=["x3", "x2y", "xy2", "y3", 'x2', 'xy', 'y2', 'x', 'y'])

print(data.shape)

func = OLS(z.flatten(), add_constant(data.values))
fitting_result = func.fit()
print(fitting_result.summary())
print(fitting_result.params.tolist())
# print(x.shape, y.shape, z.shape)

# x = np.arange(-5, 5, 0.5)
# y = np.arange(-5, 5, 0.5)
# x, y = np.meshgrid(x, y)
# z = x**2 + y**2
# x = Y
# y = X
# z = Z
ax = plt.axes(projection='3d')
ax.plot_wireframe(-x, -y, z, cmap='jet', rcount=100, ccount=100)
ax.set_title('三维线框图', fontproperties='STSong')
ax.set_xlabel('X', fontsize=14)
ax.set_ylabel('Y', fontsize=14)
ax.set_zlabel('Z', fontsize=14)
plt.show()

func = np.frompyfunc(get_k, 2, 1)
# print(func(x, y))

# print(z)


# input()


# rainbow
# print(np.sum(func(x,y)-z))
#
print(x)
print(y)
y = np.linspace(1, 3, 5)
x = np.linspace(2, 85, 5)

y, x = np.meshgrid(y, x)
print(x)
print(y)

z = func(y, x)
ax.plot_wireframe(-x, -y, z, rcount=100, ccount=100, )
ax.set_title('三维线框图', fontproperties='STSong')
ax.set_xlabel('X', fontsize=14)
ax.set_ylabel('Y', fontsize=14)
ax.set_zlabel('Z', fontsize=14)
#
# plt.tight_layout()
plt.show()

w = [506100.45241679886, 2.8060436531559367, -1.036508005301044, 14.575849670898778, 2.627134732714016,
     -66.24091603096394, -2432.948345433112, -210.82401292420363, 106811.3898729364, -7.713855074383963]
