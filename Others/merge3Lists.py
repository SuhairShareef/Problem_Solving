"""
Merge three sorted lists without dublicates
"""


def merge3Lists(nums1, nums2, nums3):
    index1, index2, index3 = 0, 0, 0
    res = []
    prev = float("-inf")
    
    while index1 < len(nums1) or index2 < len(nums2) or index3 < len(nums3):
        a, b, c, = float("inf"), float("inf"), float("inf")
        if index1 < len(nums1):
            a = nums1[index1]
        
        if index2 < len(nums2):
            b = nums2[index2]
            
        if index3 < len(nums3):
            c = nums3[index3]
        
        min_num = min([a, b, c])
        
        if min_num > prev:
            res.append(min_num)
            prev = min_num
        
        if index1 < len(nums1) and nums1[index1] == min_num:
            index1 += 1
        
        if index2 < len(nums2) and nums2[index2] == min_num:
            index2 += 1
        
        if index3 < len(nums3) and nums3[index3] == min_num:
            index3 += 1
    return res
