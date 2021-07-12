# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        low = 1
        high = n
        
        if n == 1:
            return 1
        
        while(high >= low):
            mid = (high + low) // 2
            print(mid)
            condition = isBadVersion(mid)
            prev = isBadVersion(mid - 1)
            
            if condition is True and prev is False:
                return mid
            
            elif condition is True and prev is True:
                high = mid - 1
            
            else:
                low = mid + 1
                
                
        