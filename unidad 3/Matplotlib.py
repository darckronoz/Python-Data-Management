import numpy as np
import matplotlib.pyplot as plt

temperatures = np.linspace(13.6, 18.2, 20)
time_points = range(1, 21)

plt.plot(time_points, temperatures, )
plt.title('sample xd')
plt.ylabel('temp')
plt.xlabel('time')
plt.show()

