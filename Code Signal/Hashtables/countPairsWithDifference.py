"""
Codewriting

Given an array a of positive integers, find the number of pairs of integers for which the difference between the two numbers is equal to a given number k. Since the number of pairs could be quite large, take it modulo 109 + 7 for your output.

Example

For k = 3 and a = [1, 6, 8, 2, 4, 9, 12], the output should be
countPairsWithDifference(k, a) = 3.

There are three pairs of integers whose difference is equal to 3: (1, 4), (6, 9) and (9, 12).

Input/Output

[execution time limit] 4 seconds (py3)

[input] integer k

The specified difference between two numbers.

Guaranteed constraints:
1 ≤ k ≤ 1000.

[input] array.integer a

Guaranteed constraints:
1 ≤ a.length ≤ 105,
1 ≤ a[i] ≤ 1000.

[output] integer

The number of pairs of integers with difference k modulo 109 + 7.

"""

from collections import Counter

def countPairsWithDifference(k, a):
    countOfNums = dict(Counter(a))
    count = 0
    
    for key in countOfNums:
        if (k + key) in countOfNums:
            count += (countOfNums[key] * countOfNums[k + key]) % (pow(10, 9) + 7) 
    
    return count
