from typing import List


def numIdenticalPairs(nums: List[int]) -> int:
    count = {}
    ident = 0
    
    for num in nums:
        if not num in count:
            count[num] = 0
        count[num] += 1
    
    for num in count:
        ident += (count[num] * (count[num] - 1)) // 2
        print(num)
    
    return ident

print(numIdenticalPairs([1,1,1,1]))