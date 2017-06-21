import numpy as np

one = np.ones((4, 5))
zero = np.zeros(5)
zero[0]= 1
print(one)
print(zero)

num = (one * zero)
print(num)
one[1][2] = 10
print(one)

two = one * 2
print(two)
print(one.sum())
print(one.sum(axis=1))
print(one.sum(axis=0))
