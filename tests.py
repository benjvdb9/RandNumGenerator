from RandToken import Rand
import matplotlib.pyplot as plt
import tracemalloc as tm

def testTime(rng):
    print("Testing for {}".format(rng))
    times = []
    test = Rand()
    for i in range(rng): 
        time = test.exe_time()
        times += [time]

    tot_time = sum(times)
    return tot_time

def testComplexity(rng):
    test = Rand()
    vals = []
    tm.start()
    for i in range(rng):
        v = test.range(35)
        vals += [v]
    scrn = tm.take_snapshot()
    top = scrn.statistics('lineno')
    memory_size = 0
    for elem in top:
        #print(elem)
        memory_size += elem.size

    return memory_size

times = []
amounts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 30, 40, 50, 100]
           #200, 300, 400, 500, 1000] 
for i in amounts:
    t = testTime(i)
    #t = testComplexity(i)
    times += [t]

plt.plot(amounts, times)
plt.show()
