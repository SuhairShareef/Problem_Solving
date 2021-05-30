"""
94. Binary Tree Inorder Traversal
Given the root of a binary tree, return the inorder traversal of its nodes' values.

Example 1:
Input: root = [1,null,2,3]
Output: [1,3,2]
Example 2:

Input: root = []
Output: []

Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
 

Follow up: Recursive solution is trivial, could you do it iteratively?

"""
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorderTraversal(root: TreeNode) -> List[int]:
    result = []
    
    if root:
        result.extend(inorderTraversal(root.left))
        result.append(root.val)
        result.extend(inorderTraversal(root.right))
    
    return result

def inorderTraversalIter(root: TreeNode) -> List[int]:
    result = []
    stack = []
    currentNode = root

    while True:
        if currentNode is not None:
            stack.append(currentNode)
            currentNode = currentNode.left

        elif(stack):
            currentNode = stack.pop()
            result.append(currentNode.val)
            currentNode = currentNode.right

        else:
            break

    return result
