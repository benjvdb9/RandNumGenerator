from RandToken import Rand

test = Rand()
f = open("Timing.txt", "a")

for i in range(100):
    time = test.exe_time()
    f.write(str(time) + '\n')

f.close()
