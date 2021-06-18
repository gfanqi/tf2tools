import pprint

import numpy as np
from scipy.optimize import curve_fit
from statsmodels.regression.linear_model import OLS
from statsmodels.tools import add_constant

import pandas as pd

# curve_fit
data = pd.read_excel("手镯价格标准_all.xlsx")
# print(data.columns)
data = data.astype(np.float64)
data = pd.DataFrame(data)
# data = (data - data.min()) / (data.max() - data.min())
print(data.describe())

data["种_exp"] = np.exp(-data["种"])
# print(data)
X = data[["等级", "比率", "种_exp"]]
Y = data[["真实表格"]]

X = X.values
# X3 = X**3
# X2 = X**2
X1 = X

X2 = []
for i in range(3):
    X2.append(X[:, i:] * X[:, i:i + 1])
# print(len(X2))
# X2 = X2[:-1]
# print(len(X2))
# input()
X2 = np.concatenate(X2, axis=-1)

X3 = []
for i in range(3):
    X3.append(X2 * X2[:, i:i + 1])
X3 = np.concatenate(X3, axis=-1)
X3 = pd.DataFrame(X3, columns=['a3', 'a2b', 'a2c', 'ab2', 'abc', 'ac2', 'a2b', 'ab2', 'abc', 'b3', 'b2c', 'bc2', 'a2c',
                               'abc', 'ac2', 'b2c', 'bc2', 'c3'])
X2 = X2[..., :-1]
# X3.to_excel("X3.xlsx")
# print(X3.columns)

# X3 = X3.drop_duplicates(subset=3).T
# print(X3.columns)
# print(X3["abc"])
# X3 = pd.read_excel("X3.xlsx")
# print(X3["bc2"])
# X3.to_excel("X3.xlsx",index=False)

X3.to_excel("a.xlsx", index=False)
X3 = pd.read_excel('a.xlsx')
X3 = X3[['a3', 'b3', 'a2b', 'a2c', 'ab2', 'b2c', 'abc']].values
# print(X3[['a2c', 'ac2', 'ab2', 'a2b', 'b2c', 'bc2', 'a3', 'c3', 'b3', 'abc']])

# input()

X = np.concatenate([X1, X2, X3], axis=-1)
print(X1.shape)
print(X2.shape)
print(X3.shape)
print(X.shape)
method = OLS(Y, add_constant(X))
fitting_result = method.fit()
print(fitting_result.summary())
print(fitting_result.params.tolist())

# X2 = np.concatenate([X[:, 0:] * X[:, 0:1], X[:, 1:] * X[:, 1:2], X[:, 2:] * X[:, 2:3]], axis=-1)
# print(X2)
# print(X3.shape)


# a = data[["等级"]]
# print(a.__class__)

# def f_(x, A, B):
#     pass
#     return x
