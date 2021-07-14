def bubblesort(array):
    n = len(array)
    done = False
    while not done:
        done = True
        for i in range(n-1):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
                done = False
    print(array)

# Testing it
test = [5,2,4,1,3]
bubblesort(test)

def selectionsort(array):
    smallest = array[0]
    for i in range(len(array)):
        x = i+1
        while x < len(array):
            if array[i] < array[x]:
                smallest = array[i]
                x += 1
            else:
                smallest = array[x]
                array[x], array[i] = array[i], array[x]
    print(array)


# Testing it
test = [52,133,15,74]
selectionsort(test)

def insertionsort(array):
    for idx, number in enumerate(array):
        while idx > 0:
            if array[idx] < array[idx-1]:
                array[idx-1], array[idx], = array[idx], array[idx-1]
                idx -= 1
                continue
            break
    print(array)
# Testing it
test = [5,2,3,1,4]
insertionsort(test)



