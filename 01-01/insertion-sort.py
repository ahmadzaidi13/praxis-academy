def insertionsort(nlist):
    for index in range(1, len(nlist)):
        current = nlist[index]
        position = index

        while position > 0 and nlist[position-1] > current:
            print("Swapped {} for {}".format(nlist[position], nlist[position-1]))
            nlist[position] = nlist[position-1]
            print(nlist)
            position -= 1

        nlist[position] = current

    return nlist

import random

random_nlist = [random.randint(-10, 10) for c in range(10)]

print ('sebelum: ', random_nlist)
insertionsort(random_nlist)
print ('sesudah : ', random_nlist)