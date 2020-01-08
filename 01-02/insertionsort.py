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
