"""
Given a binary tree t, determine whether it is symmetric around its center, i.e. each side mirrors the other.

Example:
For

t = {
    "value": 1,
    "left": {
        "value": 2,
        "left": {
            "value": 3,
            "left": null,
            "right": null
        },
        "right": {
            "value": 4,
            "left": null,
            "right": null
        }
    },
    "right": {
        "value": 2,
        "left": {
            "value": 4,
            "left": null,
            "right": null
        },
        "right": {
            "value": 3,
            "left": null,
            "right": null
        }
    }
}
the output should be isTreeSymmetric(t) = true.

Here's what the tree in this example looks like:

    1
   / \
  2   2
 / \ / \
3  4 4  3
As you can see, it is symmetric.
"""

#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def isTreeMirroredAroundTheCentre(t):
    def leftRightTraversal(root, result=[]):
        if root is None:
            return
            
        result.append(root.value)
        if root.left:
            leftRightTraversal(root.left, result)
        else:
            result.append(None)
        if root.right:
            leftRightTraversal(root.right, result)
        else:
            result.append(None)
    
        return result
    
    def rightLeftTraversal(root, result=[]):
        if root is None:
            return
        
        result.append(root.value)
        if root.right:
            rightLeftTraversal(root.right, result)
        else:
            result.append(None)
        if root.left:
            rightLeftTraversal(root.left, result)
        else:
            result.append(None)
    
        return result
        
    ans1 = leftRightTraversal(t.left)
    ans2 = rightLeftTraversal(t.right)
    if ans1 == ans2:
        return True
    return False