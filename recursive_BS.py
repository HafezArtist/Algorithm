#wanna try this? change the array in line 21 and the element that you want to find. Add first and last index of your array as up and down:


def recursive_Binary_Search(array, x, down, up):
    if down > up:
        return "Not Found!"
    
    mid = (up + down) // 2

    if array[mid] == x:
        return f"Found!{mid}"
    
    elif array[mid] < x:
        return recursive_Binary_Search(array, x, mid + 1, up)
    
    else:
        return recursive_Binary_Search(array, x, down, mid - 1)
    


result = recursive_Binary_Search([1, 5, 6, 8, 10, 75, 99], 75, 0, 6)
print(result)