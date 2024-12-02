def selectionSort(arr):

    #length of the list:
    n = len(arr)

    #iterating the list for the indexes:
    for i in range(n):

        #imagining that the i index is the smallest number:
        minIndex = i

        #iterating the list for the lowest value:(i + 1 is for checking the next index, n is for the list length):
        for j in range(i + 1, n):

            #if the iterated value is smaller that the minimum value shown in minIndex, change the index i, to j:
            if arr[j] < arr[minIndex]:

                minIndex = j

        #if minimum index wasn't i, change the place of i and j:
        if minIndex != i:
            arr[i], arr[minIndex] = arr[minIndex], arr[i]

    return arr


def bubbleSort(arr):

    n = len(arr)

    for i in range(n):

        swapped = False

        for j in range(0, n - i - 1):

            if arr[j] > arr[j + 1]:

                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        if not swapped:
            break

    return arr


# print(bubbleSort([15, 20, 8, 6, 40, 100]))



#insertion sort

A = [5, 2, 7, 11, -7, 8, 20, 1, 15]

for k in range(1, len(A)):
    item = A[k]
    i = k
    while i > 0 and A[i - 1] > item:
        A[i] = A[i - 1]
        i -= 1
    A[i] = item
    print(A)
print(A)