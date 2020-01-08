def bubblesort(nlist):
    for passnum in range(len(nlist)-1,0,-1):
        for i in range(passnum):
            if nlist[i]>nlist[i+1]:
                temp = nlist[i]
                nlist[i] = nlist[i+1]
                nlist [i+1] = temp

import random

random_nlist = [random.randint(-10, 10) for c in range(30)]

print ('sebelum: ', random_nlist)
bubblesort(random_nlist)
print ('sesudah : ', random_nlist)