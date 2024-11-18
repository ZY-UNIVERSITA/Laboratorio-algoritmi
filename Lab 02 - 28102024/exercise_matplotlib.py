import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import math

x = np.arange(1, 10, 0.1)

functions = [
    lambda x: x,
    lambda x: x**2,
    lambda x: x**3,
    lambda x: math.log(x),
    lambda x: x*math.log2(x),
    lambda x: x**x,
    lambda x: math.gamma(x)
]

label = [
    [ "x", 10, 10 ], [ "x^2", 10, 101 ], [ "x^3", 4.5, 101 ], [ "loge(x)", 10, 2 ], [ "x*log2(x)", 10, 32.5 ], [ "x^x", 3.5, 101 ], [ "x!", 5.75, 101 ]
]

fig, axes = plt.subplots()
numero = 0

for function in functions:
    y = list(map(function, x))
    axes.plot(x, y, label=label[numero][0])
    axes.text(x=label[numero][1], y=label[numero][2], s=label[numero][0])
    numero += 1

axes.set_ylim(0, 100)
axes.set_xlabel("n")
axes.set_ylabel("f(n)")
axes.set_title("Funzioni")
axes.legend()

plt.ylim(0, 1)
plt.show()