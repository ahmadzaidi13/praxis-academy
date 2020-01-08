print ("masukkan berapa banyak data: ")
a = []
number = int(input())
for x in range(number):
    number1 = int(input("masukkan nilai ke-"+str(x)+" = "))
    a.append(number1)
print("sebelum di sorting: ", a)

from insertionsort import *
from bubblesort import *
from quicksort import quicksort
from shellsort import shellSort
from selectionsort import selectionSort

def show_menu():
    print ("metode sorting:")
    print ("1. bubble sort")
    print ("2. insertion sort")
    print ("3. quick sort")
    print ("4. shell sort")
    print ("5. selection sort")
    print ("6. exit")



    x1 = int(input("Masukan metode sorting : "))

    if x1 == 1:
        b = a[:]
        bubblesort(b)
        print ("sebelum di sorting oleh bubble sort:", a)
        print ("setelah di sorting oleh bubble sort:", b)

    elif x1== 2:
        b = a[:]
        insertionsort(b)
        print ("sebelum di sorting oleh insertion sort:", a)
        print ("setelah di sorting oleh insertion sort:", b)

    elif x1== 3:
        b = a[:]
        quicksort(b, 0, len(a) -1)
        print ("sebelum di sorting oleh quick sort:", a)
        print ("setelah di sorting oleh quick sort:", b)

    elif x1== 4:
        b = a[:]
        shellSort(b)
        print ("sebelum di sorting oleh quick sort:", a)
        print ("setelah di sorting oleh quick sort:", b)
        
    elif x1== 5:
        b = a[:]
        selectionSort(a)
        print ("sebelum di sorting oleh quick sort:", a)
        print ("setelah di sorting oleh quick sort:", b)
       
    elif x1== 6:
        exit()
    else:
        print("Tidak Ada pilihan itu ")

if __name__ == "__main__":
    while True:
        show_menu()

# def multiplevalue(x):
#     switcher = {
#         1: print("bubblesort"),
#         2: print("insertionsort")
#     }

# if x == multiplevalue():
#     print("berhasil")


# from bubblesort import *
# bubblesort(a)
# print ("setelah di sorting oleh bubble sort:", a)

# from insertionsort import *
# insertionsort(a)
# print ("setelah di sorting oleh insertion sort:", a)

# from quicksort import quicksort
# quicksort(a, 0, len(a) -1)
# print ("setelah di sorting oleh quick sort:", a)

# from shellsort import shellSort
# shellSort(a)
# print (a)
# print ("setelah di sorting oleh shell sort:", a)