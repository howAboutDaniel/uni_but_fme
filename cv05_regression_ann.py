import numpy as np
import matplotlib.pyplot as plt


# fc = @(x) 2*sin(x*5+8);
def fx(x: np.ndarray):
    return 2*np.sin(x*5+8)

N = 140
x = np.linspace(-2, 3, 1000)
xt = np.linspace(-2, 3, N)
yt = fx(x) + (randn(N)/2.5)


plt.plot(x, fx(x), 'b-', xt, yt, 'ro')
plt.show