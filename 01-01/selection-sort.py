def selectionSort(alist):

   for i in range(len(alist)):

      
       minPosition = i

       for j in range(i+1, len(alist)):
           if alist[minPosition] > alist[j]:
               minPosition = j
                
              
       temp = alist[i]
       alist[i] = alist[minPosition]
       alist[minPosition] = temp

   return alist

import random
print(selectionSort([random.randint(-10, 10) for c in range(10)]))