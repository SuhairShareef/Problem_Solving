"""
optional follow up: If there are multiple solutions print the one whose first number is smallest, if there are still multiple solutions, print the one whose second number is smallest, and so on(the lexicographically minimal).
*/

There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example, to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.

You may assume that there are no duplicate edges in the input prerequisites.

There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.

Example:

Input: 4, [[1,0],[2,0],[3,1],[3,2]]

Output: [0,1,2,3] or [0,2,1,3]

Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both
            
"""
from collections import defaultdict
def CourseSchedule(numCourses, prerequisites):
    graph = defaultdict(set)
    pre = [0] * numCourses
    q = []
    res = []

    for v, u in prerequisites:
        pre[v] += 1
        graph[u].add(v)

    for i in range(numCourses):
        if pre[i] == 0:
            q.append(i)

    while q:
        curr = q.pop()
        res.append(curr)
        for nei in graph[curr]:
            pre[nei] -= 1
            if pre[nei] == 0:
                q.append(nei)
                
    for num in pre:
        if num > 0:
            return []
    return res