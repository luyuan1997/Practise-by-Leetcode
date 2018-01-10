"""Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
"""
"""
可以采用递归方式来解决，二叉树的最大深度要么在左子树要么在右子树，只要不断地在两个子树中寻找就可以
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        else:
            return 1+max(self.maxDepth(root.left),self.maxDepth(root.right))
