# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        
        
        
# Referenced other Solutions

#         if root == None: return 
#         if root: #그렇다면 root left와 root right 가 invertTree되는 순서는?
#             root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
#         return root 
    
        q = collections.deque([root])
        print(q[0])
        while q:
            node = q.popleft()
            if node:
                node.left, node.right = node.right, node.left
                q.append(node.left)
                q.append(node.right)
        return root