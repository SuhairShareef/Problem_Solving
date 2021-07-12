"""
Given a binary tree of integers, return all the paths from the tree's root to its leaves as an array of strings. The strings should have the following format:
"root->node1->node2->...->noden", representing the path from root to noden, where root is the value stored in the root and node1,node2,...,noden are the values stored in the 1st, 2nd,...,
and nth nodes in the path respectively (noden representing the leaf).
"""

#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def treePaths(t):
    result = []
    path = []
    q = []
    
    def paths(node, path, pathLen):
        if node is None:
            return 
            
        if(len(path) > pathLen):
            path[pathLen] = node.value
        else:
            path.append(node.value)
            
        pathLen = pathLen + 1
 
        if node.left is None and node.right is None:
            ans = ""
            for i in path[0 : pathLen - 1]:
                ans += str(i) + '->'
            ans += str(path[pathLen - 1])
            result.append(ans)
            
        else:
            paths(node.left, path, pathLen)
            paths(node.right, path, pathLen)
    
    paths(t, [], 0)
    return result
