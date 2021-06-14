from collections import Counter
def orderSort(arr1, arr2):
    result = [-1] * len(arr1)
    elementCount = dict(Counter(arr1))
    index = 0

    for num in arr2:
        for i in range(index, elementCount[num] + index):
            print(i)
            result[i] = num
        index += elementCount[num] 
        elementCount[num] = 0
    
    elementCount = dict(sorted(elementCount.items()))
    
    for num in elementCount:
        for i in range(index, elementCount[num] + index):
            result[i] = num
        index += elementCount[num]
    
    return result

print(orderSort([2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19], [2, 1, 4, 3, 9, 6]))