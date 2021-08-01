"""
There are N network nodes, labeled from 1 to N.

Given times, a list of travel times as directed edges times[i] = (u, v, w), where u is the source node, v is the target node, and w is the time it takes for a signal to travel from source to target.

Now, we send a signal from a certain node K. How long will it take for all nodes to receive the signal? If it is impossible, return -1.

Example:

Input: times = [[2,1,1],[2,3,1],[3,4,1]], N = 4, K = 2
Output: 2
"""
from collections import defaultdict, deque
def NetworkDelayTime(times, n, k):
    graph = defaultdict(list)
    time = [0] + [float("inf")] * n
    q = deque([(0, k)])
    
    for u, v, w in times:
        graph[u].append((v, w))
    
    while q:
        t, v = q.popleft()
        if t < time[v]:
            time[v] = t
            for u, w in graph[v]:
                    q.append((t + w, u))
    
    m = max(time)
    if m < float("inf"):
        return m
    return -1