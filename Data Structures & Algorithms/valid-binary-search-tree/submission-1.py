# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def maxVal(node):
            while node.right:
                node=node.right
            return node.val

        def minVal(node):
            while node.left:
                node=node.left
            return node.val

        def dfs(node):
            if not node:
                return True
            if node.left:
                if maxVal(node.left) >= node.val:
                    return False
            if node.right:
                if minVal(node.right) <= node.val:
                    return False
            return dfs(node.left) and dfs(node.right)
        return dfs(root)