from RandToken import Rand
import matplotlib.pyplot as plt

def testTime(rng):
    print("Testing for {}".format(rng))
    times = []
    test = Rand()
    for i in range(rng): 
        time = test.exe_time()
        times += [time]

    tot_time = sum(times)
##    f = open("Timing.txt", "a")
##    f.write("{} value(s): ".format(rng) + str(tot_time) + '\n')
##    f.close()
    return tot_time

times = []
amounts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 30, 40, 50, 100]
           #200, 300, 400, 500, 1000] 
for i in amounts:
    t = testTime(i)
    times += [t]

plt.plot(amounts, times)
plt.show()
