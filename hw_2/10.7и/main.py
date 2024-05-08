import math as ma
import matplotlib.pyplot as plt
import numpy as np
from scipy import optimize

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
    def norm(self):
        return max(self.value)

def mat(x):
    res = []
    for i in range(len(x.value)):
        if(i == 0):
            res.append(2*x.value[i] -5*x.value[i+1] +4*x.value[i+2] -1*x.value[i+3])
        else:
            if(i == len(x.value)-1):
                res.append(2*x.value[i] -5*x.value[i-1] +4*x.value[i-2] -1*x.value[i-3])
            else:
                res.append(x.value[i - 1] - 2*x.value[i] + x.value[i + 1])
    return Arr(res);

def fi_1(k):
    match (k % 4):
        case 0:
            return 0
        case 1:
            return 4/(k*ma.pi)
        case 2:
            return -8/(k*ma.pi)
        case 3:
            return 4/(k*ma.pi)

class Funtion:
    dt = 0
    dx = 0
    a = []
    k = 0
    y = []
    fun = 0
    N = 0
    ki = []

    def __init__(self, dt, dx, a, k, y, f, n, ki):
        self.dt = dt
        self.dx = dx
        self.a = a
        self.k = k
        self.y = y
        self.fun = f
        self.N = n
        self.ki = ki

    def f(self, x_):
        res = Arr([0 for i in range(len(x_))])
        x = Arr(x_)
        for i in range(self.N):
            if (i == self.N - 1):
                res = res + x * self.a[self.N][i]
            else:
                res = res + self.ki[i] * self.a[self.N][i]
        res = self.fun(self.y + res * self.dt) * self.k / self.dx**2 - x
        return res.value

def next_y(y, dt, dx, k):
    res_1 = Arr([0 for j in range(len(y.value))])
    c = [1/3, 1, 1]
    b = [3/4, -1/12, 1/3]
    a = [[1/3, 0, 0],
        [0, 1, 0],
        [3/4, -1/12, 1/3]]
    k_arr = []
    for j in range(3):
        fun = Funtion(dt, dx, a, k, y, mat, j, k_arr)
        k_arr.append(Arr(optimize.root(fun.f, y.value).x))
    for j in range(3):
        res_1 = res_1 + k_arr[j] * b[j]
    res_1 = y + res_1 * dt
    res_1.value[0] = 0
    res_1.value[len(res_1.value) - 1] = 0
    return res_1

def ans(x,t,wight):
    res = 0
    for i in range(100):
        res = res + fi_1(i)*ma.exp(-(ma.pi**2 * i**2 * t)/(wight**2))*ma.sin(ma.pi*i*x/wight)
    return res

