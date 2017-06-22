import time
import random
def insertion_sort(array):
    start_time = time.time()
    for i in range(1,len(array)):
        j = i
        while ((j>0)and (array[j]<array[j-1])):
            array[j],array[j-1] = array[j-1],array[j]
            j = j-1

    # print("%s" % (time.time() - start_time))
    return array

# Check whether the array is empty
# try:
#     l = input().split(' ')
#     l = [int(x) for x in l]
#     insertion_sort(l)
# except:
#     print("[]")

# Generate random numbers in between the given range
# a = [int(1000* random.random()) for i in range(500)];

# Generate an array of ascending order in the given range
# a = list(range(0,100))

# Generate an array of descending order in the given range
# a = list(range(0,10000))
# b=a[::-1]

# insertion_sort(b)
