# Lambda functions are used as a temporary function. it can be written everywhere instead of def() ..
f = lambda x: x ** 2
f(2)
# %%

a = [(1, 2), (8, 5), (4, 7), (0, 9), (3, 1)]
a.sort()
a
# %% Sort by second argument

a.sort(key=lambda x: x[1])
# a.sort(key=lambda x: x[0]) = sort() as default
a
# %% map can be apply a function to for example every elements of a list. e.g.
import numpy as np

list1 = [1, 3, 4, 6, 2, 6]

for i in range(0, len(list1)):
    l2 = map(lambda x: i + 3 * x, list1)

list(l2)
# %%
num_1 = [40, 50, 12, 4, 51, 23, 1, 4, 6, 9, 88, 20, 10]
print(list(map(lambda x: 'large' if x > 20 else 'small', num_1)))
