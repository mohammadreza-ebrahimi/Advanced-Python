
# Created on Fri Dec 25 10:56:21 2020
# @Author: Mohammadreza Ebrahimi
#%%

import matplotlib.pyplot as plt
import numpy as np


# %%
def diff(f, x, h=1E-5):
    return (f(x + h) - f(x)) / h
#%%

def f(x, y):
    while x > y:
        yield x ** 2 + x * np.sin(2 * y)
        y += 1


for i in f(10, 1):
    print(i)

# %% Class
class Person:
    count = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.count = Person.count + 1

    def birthday(self):
        self.age = self.age + 1
        print('happy birthday %s' % self.name)

    def get_info(self):
        print('Name is %s and age is %i' % (self.name, self.age))

    def life(self, age):
        return 75 - self.age

    def return_count(self):
        return (Person.count)


# %%
reza = Person('reza', 25)
reza.age, reza.name
reza.get_info()
reza.birthday()
reza.age

print('I have %i person' % reza.return_count())


# %%
class Computer:
    count = 0

    def __init__(self, ram, hard, cpu, graphic):
        Computer.count += 1
        self.ram = ram
        self.hard = hard
        self.cpu = cpu
        self.graphic = graphic

    def value(self):
        return self.ram + self.hard + self.graphic + self.cpu

    def __del__(self):
        Computer.count -= 1


# %%

pc1 = Computer(16, 1, 4, 4)
pc1.ram
pc1.value()



# %%
class Laptop(Computer):
    def value(self):
        return self.ram + self.hard + self.graphic + self.cpu + self.size


# %%

laptop1 = Laptop(2, 2, 2, 1)
laptop1.size = 13
laptop1.value()
#%%
del pc1
#%%
pc1.ram
#%% Some Physical Examples
# %%
class Y:
    def __init__(self, v0):
        self.v0 = v0
        self.g = 9.81

    def f(self, t):
        return self.v0 * t - 0.5 * self.g * t ** 2


# %%
x = Y(3)
x.g
x.v0
x.f(0.1)
diff(x.f, 0.1)


# %%
class Y1:
    def __init__(self, v0, t):
        self.v0 = v0
        self.g = 9.81
        self.t = t

    def f1(self):
        return self.v0 * self.t - 0.5 * self.g * self.t ** 2


# %%
x = Y1(t=3, v0=0.1)
x.g
x.v0
x.f1()
# %%
x = Y1(0.1, 3)
x.g
x.v0
x.f1()
# %%
x = Y1(v0=3, t=0.1)
x.g
x.v0
x.f1()
# %%
import numpy as np


class circle:
    def __init__(self, x0, y0, R):
        self.x0, self.y0, self.R = x0, y0, R

    def area(self):
        return np.pi * self.R ** 2

    def circumfrence(self):
        return 2 * np.pi * self.R


# %%
c1 = circle(x0=0, y0=0, R=2.5)
c1.area()
c1.circumfrence()


# %%
class GB:
    def __init__(self, a, l, M, Q):
        self.a = a
        self.l = l
        self.M = M
        self.Q = Q

    def laps(self, r):
        return 1 + r ** 2 / (2 * self.a) * (1 - (1 + 4 * self.a * (-1 / self.l ** 2
                                                                   + 2 * self.M / r ** 3 - self.Q ** 2 / r ** 4)) ** 1 / 2)


# %%
G1 = GB(a=0.2, l=9, M=1, Q=0.5)
G1.M
G1.Q
G1.a
G1.laps(0.3)
G1.laps(1)
diff(G1.laps, 1)
diff(G1.laps, 0.3)
G1.laps(2)


# %%
class GB1:
    def __init__(self, a, l, M, Q):
        self.a = a
        self.l = l
        self.M = M
        self.Q = Q

    def __call__(self, r):
        return 1 + r ** 2 / (2 * self.a) * (1 - (1 + 4 * self.a * (-1 / self.l ** 2
                                                                   + 2 * self.M / r ** 3 - self.Q ** 2 / r ** 4)) ** 1 / 2)


# %%
G2 = GB1(0.2, 9, 1, 0.5)
G2(2)
# %%
import numpy as np


class vec2D:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __add__(self, i):  # (self, others)
        return vec2D(self.x + i.x, self.y + i.y)

    def __sub__(self, i):
        return vec2D(self.x - i.x, self.y - i.y)

    def __mul__(self, i):
        return self.x * i.x + self.y * i.y

    def __abs__(self):
        return np.sqrt(self.x ** 2 + self.y ** 2)

    def __eq__(self, i):
        return self.x == i.x and self.y == i.y

    def __str__(self):
        return '(%g, %g)' % (self.x, self.y)

    def __ne__(self, i):
        return not self.__eq__(i)


# %%
a = vec2D(1, 1)
b = vec2D(2, 3)
c = vec2D(-2, 4)
b1 = vec2D(2, 3)
b.x  # i.x
a.x  # self.x
print(a + b)
print(a * b)
print(b + c)
print(b == c)
print(b1 == b)
c1 = a + b
c1.__abs__()
a.__abs__()
print(a.__add__(b))
print(a.__eq__(b))
print(a.__ne__(b))
print(a.__str__())
#%%
