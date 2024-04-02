import math as ma
import matplotlib.pyplot as plt
import numpy as np

class Arr:
    value = []

    def __init__(self, x):
        self.value = x
    
    def __mul__(self, a):
        res = []
        for i in self.value:
            res.append(i * a)
        return Arr(res)

    def __truediv__(self, a):
        return self * (1/a)

    def __add__(self, y):
        res = []
        for i in range(len(self.value)):
            res.append(self.value[i] + y.value[i])
        return Arr(res)

    def __sub__(self, y):
        return self + y * (-1)

    def rang(self):
        res = 0
        for i in self.value:
            res = res + i * i
        return ma.sqrt(res)

def f(x, t):
    td = 24 * 60 * 60
    k_1 = pow(10, -2) * max(0, ma.sin(2*ma.pi*t/td))
    k_2 = pow(10, 5)
    k_3 = pow(10, -16)
    return Arr([k_1 * x.value[2] - k_2 * x.value[0],
                k_1 * x.value[2] - k_3 * x.value[1] * x.value[3],
                k_3 * x.value[1] * x.value[3] - k_1 * x.value[2],
                k_2 * x.value[0] - k_3 * x.value[1] * x.value[3]])

def next_y(i, y, dt):
    print(i * dt, " ",y[i].value[0]," ", y[i].value[1]," ", y[i].value[2]," ", y[i].value[3])
    return f(y[i], i*dt) * dt + y[i]

def solve(zero, dt, stop):
    result = [zero]
    i = 0
    while(dt * (i + 1) < stop):
        result.append(next_y(i, result, dt))
        if(result[i].value[0] == float('inf')):
            return 0
        i = i + 1
    return result

zero = Arr([0, 0, 5 * pow(10, 11), 8 * pow(10, 11)])   # краевые условия
T = 24 * 60 * 60
dt = 1              # шаг
result = solve(zero, dt, 1000*dt)
while(result == 0):
    dt = dt / 10
    result = solve(zero, dt, 1000*dt)
print(dt)
