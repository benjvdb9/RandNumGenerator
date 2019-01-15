import matplotlib.pyplot as plt
import statistics as stat
from math import sqrt
from RandToken import Rand

points_x = []
points_y = []
distance = []
test = Rand()
for elem in range(100):
    x = test.range(100, -100)
    y = test.range(100, -100)
    #x = test.range()
    #y = test.range()
    points_x += [x]
    points_y += [y]
    distance += [sqrt(x ** 2 + y ** 2)]
    print("Coord: ({}, {})".format(x, y))

plt.subplot(2, 1, 1)
plt.axis([-100, 100, -100, 100])
plt.plot(points_x[:10], points_y[:10], 'ro')
plt.plot(points_x[10:20], points_y[10:20], 'go')
plt.plot(points_x[20:30], points_y[20:30], 'bo')
plt.plot(points_x[30:40], points_y[30:40], 'co')
plt.plot(points_x[40:50], points_y[40:50], 'mo')
plt.plot(points_x[50:60], points_y[50:60], 'yo')
plt.plot(points_x[60:], points_y[60:], 'ko')

for i in range(10):
    plt.annotate(i, (points_x[i], points_y[i]))

x = sum(points_x)
y = sum(points_y)
print("Center: ({}, {})".format(x, y))
plt.plot(x, y, 'm*')
plt.annotate('CENTER', (x, y))

plt.subplot(2, 1, 2)
plt.axis([-500, 500, -500, 500])
plt.plot(x, y, 'm*')
plt.annotate('CENTER', (x, y))
plt.plot(points_x, points_y, 'ko')

print("\n\nSTATISTICS\n=============\n")
mean1 = stat.mean(points_x)
mean2 = stat.mean(points_y)
median1 = stat.median(points_x)
median2 = stat.median(points_y)

try:
    mode1 = stat.mode(points_x)
except:
    mode1 = "No common mode"
try:
    mode2 = stat.mode(points_y)
except:
    mode2 = "No common mode"

stdev1 = stat.stdev(points_x)
stdev2 = stat.stdev(points_y)
print("Mean1: {} -------------- Mean2: {}".format(mean1, mean2))
print("Median1: {} ------------ Median2: {}".format(median1, median2))
print("Mode1: {} -------------- Mode2: {}".format(mode1, mode2))
print("Stdev1: {} ------------- Stdev2: {}".format(stdev1, stdev2))
plt.show()
