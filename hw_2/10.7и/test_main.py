import main as m
import math

wight = 2
M = 5
time = 2
T = 25
y_show = []
x_show = []
for i in range(5):
    zero = m.Arr([(i*wight/M >= wight/2)*2 for i in range(M)])
    zero.value.append(0)
    y = zero
    count = 0
    res = 0
    while (count != T):
        y_real = [m.ans(j * wight/M, count * time/T, wight) for j in range(M + 1)]
        y_r = m.Arr(y_real)
        res_0 = y_r - y
        res += res_0.norm()/T
        y = m.next_y(y, time/T, wight/M, 1)
        count += 1
    y_show.append(math.log2(res))
    x_show.append(math.log2(M))
    M = M * 2
    T = T * 4
m.plt.plot(x_show, y_show, "r", label = "решение")
m.plt.legend()
m.plt.grid()
m.plt.xlabel('$x$')
m.plt.ylabel('$y$')
m.plt.show()

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

print((-1)*(k(x_show, y_show)))
