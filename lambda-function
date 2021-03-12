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


a=[1,3,6,2,1,6,3,9,11,42,14]                                            

type(a)                                                                 
list

map(lambda x: x * 2,a)                                                  
<map at 0x7f30ff799400>

list(a)                                                                 
[1, 3, 6, 2, 1, 6, 3, 9, 11, 42, 14]

a1=map(lambda x: x * 2,a)                                               

list(a1)                                                                
[2, 6, 12, 4, 2, 12, 6, 18, 22, 84, 28]

list(filter(lambda x: x % 2 == 0, a))                                   
[6, 2, 6, 42, 14]
