"""
While Natsha rested, he invented a smart game. Given two numbers N and M, Natsha wants to know how many operations are necessary to convert N into M.

Six operations are allowed:

Operation 1: N = N*2
Operation 2: N = N*3
Operation 3: N = N/2
Operation 4: N = N/3
Operation 5: N = N+7
Operation 6: N = N-7
Given N and M, return the minimum number of operations to convert N into M.

Example:

input: N = 10, M = 15
output: 2
"""
from collections import deque
def SmartGame(n, m):
    def operations(num):
        return [num * 2, num * 3, num // 2, num // 3, num + 7, num - 7]
        
    visited = set()
    q = deque([(n, 0)])
        
    while q:
        curr, op = q.popleft()
        if curr == m:
            return op

        neighbors = operations(curr)
        for nei in neighbors:
            if nei not in visited:
                if nei == m:
                    return op + 1
                q.append((nei, op + 1))
    
    return -1