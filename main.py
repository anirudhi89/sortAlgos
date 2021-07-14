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

