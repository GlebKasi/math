import main as m

wight = 2
M = 10
time = 2
T = 100
zero = m.Arr([(i*wight/M >= wight/2)*2 for i in range(M)])
zero.value.append(0)
y = zero
count = 0
while (count != T):
    print(count)
    y_show = y.value
    x_show = [i * wight/M for i in range(M + 1)]
    y_real = [m.ans(i * wight/M, count * time/T, wight) for i in range(M+1)]
    m.plt.plot(x_show, y_show, "r", label = "решение")
    m.plt.plot(x_show, y_real, "b", label = "реальное решение")
    m.plt.legend()
    m.plt.grid()
    m.plt.xlabel('$x$')
    m.plt.ylabel('$y$')
    m.plt.show()
    y = m.next_y(y, time/T, wight/M, 1)
    count += 1
