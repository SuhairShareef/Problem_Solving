def binarySearch(arr, num, left = 0, right = None):
    if right is None:
        right = len(arr) - 1
    
    if left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == num:
            return mid
        
        elif arr[mid] > num:
            return binarySearch(arr, num, left, mid - 1)
            
        else:
            return binarySearch(arr, num, mid + 1, right)
    
    return None
    
print(binarySearch([1,2,3,4,5,6], 2))