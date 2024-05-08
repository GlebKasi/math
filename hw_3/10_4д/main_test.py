import math as ma
import matplotlib.pyplot as plt
import numpy as np
from scipy import optimize

a = 0.5

def start(x):
    return ma.exp(a*x)
    
def start_1(x):
    return a*ma.exp(a*x)

def board0(t):
    return ma.exp(a*t)

def board1(t):
    return ma.exp(a*(t+1))

def ans(x,t):
    return ma.exp(a*(t+x))

def next_y(y0, y1, dx, dt, n):
    res = [0]
    if(n == 1):
        for i in range(1, len(y0) - 1):
            res.append((start_1(i*dx)/dt + (start((i+1)*dx) - 2 * start(i*dx) + start((i - 1)*dx))/(dx**2))*(dt**2) + start(i*dx))
        res[0] = board0(n*dt)
        res.append(board1(n*dt))
    else:
        for i in range(1, len(y0) - 1):
            res.append((y0[i + 1] - 2*y0[i] + y0[i - 1])*(dt**2)/(dx**2) + 2*y0[i] - y1[i])
        res[0] = board0(n*dt)
        res.append(board1(n*dt))
    return res

def norm(x,y):
    res = []
    for i in range(len(x)):
        res.append(abs(x[i] - y[i]))
    return max(res)

wight = 1
time = 1
M = 10
N = 10
y_show = []
x_show = []
for j in range(5):
    res = 0
    count = 0
    dx = wight/M
    dt = time/N
    y_1 = []
    y_2 = []
    y_3 = []
    y_1 = [start(i*dx) for i in range(M + 1)]
    y_2 = next_y(y_1, 0, dx, dt, 1)
    for i in range(2,N):
        y_real = [ans(i * wight/M, count * time/N) for i in range(M+1)]
        y_3 = next_y(y_2, y_1, dx, dt, i)
        count += 1
        res += norm(y_3,y_real)/N
        y_1 = y_2
        y_2 = y_3
    y_show.append(ma.log2(res))
    x_show.append(ma.log2(M))
    M = M * 2
    N = N * 2
plt.plot(x_show, y_show, "r", label = "решение")
plt.legend()
plt.grid()
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.show()

def aver(x):
    res = 0
    for i in x:
        res = res + i
    return res/len(x)

def k(x, y):
    a = 0
    b = 0
    for i in range(len(x)):
       a = a + (x[i] - aver(x)) * y[i]
       b = b + (x[i] - aver(x)) ** 2
    return a/b

print(((-1)*k(x_show, y_show)))
