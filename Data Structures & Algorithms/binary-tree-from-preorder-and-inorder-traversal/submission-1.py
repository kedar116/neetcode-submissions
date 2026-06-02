# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        #Optimal: Use a hashmap to store indices of the root in inorder 
        inorder_map={}
        for i in range(len(inorder)):
            inorder_map[inorder[i]]=i
        
        self.pre_idx=0
        def dfs(left,right):
            if left>right:
                return None
            
            root_val = preorder[self.pre_idx]
            root = TreeNode(root_val)
            self.pre_idx+=1

            mid = inorder_map[root_val]

            root.left = dfs(left, mid-1)
            root.right = dfs(mid+1, right)

            return root

        return dfs(0, len(inorder)-1)

