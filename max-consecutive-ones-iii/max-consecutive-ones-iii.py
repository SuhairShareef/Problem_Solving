class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        res, left = 0, 0
        
        for right in range(len(nums)):
            if nums[right] == 0:
                if k == 0:
                    while nums[left] != 0:
                        left += 1
                    left += 1
                
                else:
                    k -= 1
            
            res = max(res, right - left + 1)
        
        return res