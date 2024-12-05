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

# A = [1, 6, 7, 4, 8, 5, 3, 2, 9]

# for k in range(1, len(A)):
#     item = A[k]
#     i = k
#     while i > 0 and A[i - 1] > item:
#         A[i] = A[i - 1]
#         i -= 1
#     A[i] = item
#     print(A)
# print(A)


def mergeSort(arr):
    if len(arr) > 1:   #deviding into groups

        mid = len(arr) // 2

        #deviding into left and right groups:
        left_half = arr[:mid]
        right_half = arr[mid:]

        mergeSort(left_half)
        mergeSort(right_half)


        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:

                arr[k] = left_half[i]
                i += 1

            else:

                arr[k] = right_half[j]
                j += 1

            k += 1

        while i < len(left_half):

            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):

            arr[k] = right_half[j]
            j += 1
            k += 1



array = [38, 27, 43, 3, 9, 82, 10]
mergeSort(array)
print("Sorted array:", array)