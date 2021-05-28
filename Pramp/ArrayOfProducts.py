from typing import List

def ArrayOfProducts(array: List) -> List[List]:
    if len(array) > 1:
        leftProd = [1] * len(array)
        rightProd = [1] * len(array)
        
        for i in range(1, len(array)):
            leftProd[i] = leftProd[i - 1] * array[i - 1]
        
        for i in range(len(array) - 2, -1, -1):
            rightProd[i] = rightProd[i + 1] * array[i + 1]
        
        return [leftProd[i] * rightProd[i] for i in range(len(array))]
        
    else:
        return []

print(ArrayOfProducts([2,2]))
print(ArrayOfProducts([1,1,2,3,5,4]))