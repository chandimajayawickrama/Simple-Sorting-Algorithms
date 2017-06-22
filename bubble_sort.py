import time
import random
def bubble_sort(array):
    start_time = time.time()
    swapped = False
    if len(array)==0:
      array =[]
      return array
    while not swapped :
        for i,val in enumerate(array):
            for j,val1 in enumerate(array):
                if (array[i]>array[j]):
                    array[i],array[j] = array[j],array[i]
                    swapped = True

    # print("%s" %(time.time() -start_time))
    return array


# Check whether the array is empty,when getting an input from the user
try:
    l = input().split(' ')
    l = [int(x) for x in l]
    bubble_sort(l)
except:
    print("[]")

# Generate random numbers in between the given range
# a= [int(2*random.random()) for i in range(1000)];

# Generate an array of descending order in the given range
# a = list(range(0,100))

# Generate an array of ascending order in the given range
# b=a[::-1]

bubble_sort(l)
