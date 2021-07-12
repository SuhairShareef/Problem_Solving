def heapSort(arr):
    span = (len(arr) // 2) - 1

    for i in range(span, -1, -1):
        heapify(arr, len(arr), i)

    for i in range(len(arr) - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  
        heapify(arr, i, 0)

def heapify(arr, n, i):
    largest = i 
    l = 2 * i + 1     
    r = 2 * i + 2     

    if l < n and arr[i] < arr[l]:
        largest = l
        
    if r < n and arr[largest] < arr[r]:
        largest = r
        
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i] 
        heapify(arr, n, largest)
  
arr = [20, 10, 15, 2, 7, 80]
heapSort(arr)
print(arr)
