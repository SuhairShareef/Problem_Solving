# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

"""
n = range of numbers which can be picked (1, n)
pick = (unknown) guess the pick

API guess(n) --> (-1 -> bigger than the pick, 1 -> smaller than pick, 0 -> it's the pick)
"""

class Solution:
    def guessNumber(self, n: int) -> int:
        low = 1
        high = n
        
        while(high >= low):
            mid = (high + low) // 2
            ourGuess = guess(mid)
            
            if ourGuess == 0:
                return mid
            
            elif ourGuess == -1:
                high = mid - 1
            
            else:
                low = mid + 1
                