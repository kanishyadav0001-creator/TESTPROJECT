import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1, 11, 1)

y = (6 * x**2) + x + 1

plt.plot(x, y, color='green', linestyle='-', linewidth=2, marker='s', label='y = 6x^2 + x + 1')

plt.title('Mathematical Equation')
plt.xlabel('x values (1 to 10)')
plt.ylabel('y values')
plt.legend()

plt.show()