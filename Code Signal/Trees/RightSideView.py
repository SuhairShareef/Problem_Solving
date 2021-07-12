"""
Given a binary tree t, return its right view. To understand what the right view of the tree means, imagine yourself standing on the right side of the tree: The right view will be all the vertices that you can see. For example, imagine the following tree:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
 /
6               <---
In this case, you can see vertices 1, 3, 4, and 6.

Given binary tree t, return the values of the vertices in the right view, ordered from top to bottom.
"""

#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def treeRightView(t):
    result = []
    
    def rightVeiw(node, levels, currentLevel):
        if node is None:
            return 
        
        if currentLevel not in levels:
            levels.append(currentLevel)
            result.append(node.value)
        
        rightVeiw(node.right, levels, currentLevel + 1)
        rightVeiw(node.left, levels, currentLevel + 1)
          
    rightVeiw(t, [], 1)
    return result