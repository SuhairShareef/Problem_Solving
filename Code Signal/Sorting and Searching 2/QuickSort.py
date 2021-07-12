def quickSort(arr: list):
    if len(arr) <= 1:
        return arr
        
    pivot = arr[len(arr) // 2]
    left = []       # elements that are less than the pivot
    mid = []        # elements that are equal to the pivot
    right = []      # elements that are greater than the pivot
    
    for num in arr:
        if num < pivot:
            left.append(num)
        elif num == pivot:
            mid.append(num)
        else:
            right.append(num)
            
    return quickSort(left) + mid + quickSort(right)

print(quickSort([5,2,7,5,6,3,1]))