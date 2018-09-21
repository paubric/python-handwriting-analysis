import matplotlib.pyplot as plt
import numpy as np

x = []
y = []
data = []

file = open('data.txt')
lines = file.readlines()

for line in lines:
    line = line.split()
    long_len = int(line[0])
    short_len = int(line[1])
    x.append(long_len)
    y.append(short_len)
    data.append([long_len, short_len])

heatmap = np.zeros((max(x) + 1, max(y) + 1))

print(len(x))

average_ratio = np.sum([y[i] / x[i] for i in range(len(x))]) / len(x)
print(average_ratio)

average_short_len = np.sum([y[i] for i in range(len(x))]) / len(x)
print(average_short_len)

average_long_len = np.sum([x[i] for i in range(len(x))]) / len(x)
print(average_long_len)

for point in data:
    heatmap[point[0], point[1]] += 1

plt.title('Original to Abbreviation Length')
axes = plt.gca()
axes.set_aspect('equal', 'box')
axes.set_xlim([1,max(x)])
axes.set_ylim([1,max(y)])
plt.ylabel('Abbreviation Length')
plt.xlabel('Original Length')
plt.plot(np.unique(x), np.poly1d(np.polyfit(x, y, 1))(np.unique(x)))
plt.imshow(heatmap.T, interpolation='bicubic')
plt.show()
