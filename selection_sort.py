import time
import random
def selection_sort(array):
    start_time = time.time()
    for i in range(0,len(array)-1):
        position = i
        for j in range(i+1,len(array)):
            if array[position] > array[j]:
                position = j
        array[i],array[position] = array[position],array[i]
    # print("%s" % (time.time() - start_time))
    return array

# Check whether the array is empty,when getting an input from the user
# try:
#     l = input().split(' ')
#     l = [int(x) for x in l]
#     selection_sort(l)
# except:
#     print("[]")

# Generate random numbers in between the given range
# a = [int(1000* random.random()) for i in range(500)];

# Generate an array of ascending order in the given range
# a = list(range(0,10000))

# Generate an array of descending order in the given range
# b=a[::-1]

# selection_sort(b)
