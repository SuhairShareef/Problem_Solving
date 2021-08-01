"""
Mr-Spy has n cities labeled from 1 to n and a list of undirected roads between them. His goal is to construct new roads so that there is a route between any two cities.

Since its too easy for him to do it he assigned the following task to you.
Find out the minimum number of new undirected roads required to achieve his goal.

A road always connects two different cities, and there is at most one road between any two cities.

Example:

input: n = 4, roads = [[1, 2], [3, 4]]

output: 1
"""
from collections import defaultdict

def BuildingRoads(n, roads):
    graph = defaultdict(list)
    visited = [False] * (n + 1)
    count = 0
    
    def dfs(v):
        visited[v] = True
        for city in graph[v]:
            if not visited[city]:
                dfs(city)    
    
    
    # Cosntructing graph
    for road in roads:
        graph[road[0]].append(road[1])
        graph[road[1]].append(road[0])
    
    
    for c in range(1, n + 1):
        if not visited[c]:
            dfs(c)
            count += 1
    
    return count - 1