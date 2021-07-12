from typing import List


def sortColors(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    [2,2,2,2,2]
    [0,2,1,1,1]
    [0,0,1,1,2,2]
    
    low = 0
    high = len(nums) - 1
    mid = (low+high) // 2
        
        zeros   ones      ?      twos
    [0 --- low --- mid --- high --- (len(nums) - 1)]
    """
    
    low = 0
    mid = 0
    high = len(nums) - 1
    
    while mid <= high:
        if nums[mid] == 1:
            mid += 1
        
        elif nums[mid] == 0:
            nums[mid], nums[low] = nums[low], nums[mid]
            low += 1
            mid += 1
        
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1
