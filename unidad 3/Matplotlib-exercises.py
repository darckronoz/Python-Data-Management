import numpy as np
import matplotlib.pyplot as plt

#excercise randomize the graph with the temperatures.

ri = np.random.rand(20) #Ri generated with numpy numbers between 0 and 1
min = 13
max = 25
temperatures = min+(max-min)*ri #random temperatures with max min distribution.
print(temperatures)
time_points = range(1, 21)
print(len(time_points))

plt.plot(time_points, temperatures, )
plt.title('sample xd')
plt.ylabel('temp')
plt.xlabel('time')
plt.show()