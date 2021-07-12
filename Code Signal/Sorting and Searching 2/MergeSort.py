def mergeSort(arr, left=0, right=None):
    if right is None:
        right = len(arr)
        
    if left >= right:
        return 
    
    mid = (left + right) // 2
    mergeSort(arr, left, mid)
    mergeSort(arr, mid + 1, right)
    merge(arr, left, mid, right)


def merge(arr, left, mid, right):
    lside = arr[left: mid + 1]
    rside = arr[mid + 1: right + 1]
    
    i = j = 0
    sortedIndex = left
    
    while i < len(lside) and j < len(rside):
        if lside[i] <= rside[j]:
            array[sortedIndex] = lside[i]
            i = i + 1
        # Opposite from above
        else:
            array[sortedIndex] = rside[j]
            j = j + 1

        # Regardless of where we got our element from
        # move forward in the sorted part
        sortedIndex = sortedIndex + 1

    while i < len(lside):
        array[sortedIndex] = lside[i]
        i = i + 1
        sortedIndex = sortedIndex + 1

    while j < len(rside):
        array[sortedIndex] = rside[j]
        j = j + 1
        sortedIndex = sortedIndex + 1
        
array = [33, 42, 9, 37, 8, 47, 5, 29, 49, 31, 4, 48, 16, 22, 26]
mergeSort(array)
print(array)