# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        result = ""
        q = deque()
        q.append(root)
        while q:
            node = q.popleft()
            if not node:
                result+="#,"
            else:
                result+=str(node.val)+","
                q.append(node.left)
                q.append(node.right)
        return result
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None
        nodes = data.split(",")
        root = TreeNode(nodes[0])
        q = deque()
        q.append(root)
        i=1
        while q and i<len(nodes):
            curr = q.popleft()
            if nodes[i]!="#":
                left = TreeNode(int(nodes[i]))
                curr.left = left
                q.append(left)
            i+=1

            if nodes[i]!="#":
                right = TreeNode(int(nodes[i]))
                curr.right = right
                q.append(right)
                
            i+=1
        return root



