from time import time

times = []

for i in range(10):
    times += [time()]


delta = []
old = ""
for elem in times:
    print("Time:", elem)
    if old == "":
        res = "No delta"
    else:
        res = elem - old

    print("Delta:", res)
    old = elem
    
