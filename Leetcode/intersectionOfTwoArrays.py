from typing import List

def intersect(nums1, nums2):
    '''
        nums1 = [1,2,2,1] # {1:2, 2:2} --> x length
        nums2 = [2,2] # {2:2} --> y length
        inter -> [2,2]
        
        nums1 = [1,2,3,4]
        nums2 = []
        inter -> []
        
        nums1 = [1,2,3,4,5]
        nums2 = [5,4,3,2,1]
        inter -> [2,2]
        
        nums1 = [1,1,2,2]
        nums2 = [2,2]
    '''
    """
    
    
    nums1Count = dict(Counter(nums1))
    #nums2Count = dict(Counter(nums2))
    result = []
    
    for num in nums2:
        if num in nums1Count and nums1Count[num] > 0:
            result.append(num)
            nums1Count[num] -= 1
                
    return result"""
    result = []
    if len(nums1) == 0 or len(nums2) == 0:
        return result
    
    it1 = 0
    it2 = 0
    
    while it1 < len(nums1) and it2 < len(nums2):
        if nums1[it1] == nums2[it2]:
            result.append(nums1[it1])
            it1 += 1
            it2 += 1
        
        elif nums1[it1] < nums2[it2]:
            it1 += 1
        
        else:
            it2 += 1
    
    return result
            

print(intersect([1,1,2,2],[1,1,2,2]))