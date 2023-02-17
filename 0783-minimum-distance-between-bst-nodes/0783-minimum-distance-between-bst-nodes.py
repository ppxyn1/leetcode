# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        lst = []
        res=[]
        
        def inOrder(tree):
            if tree==None: return 
            if tree.left:
                inOrder(tree.left)
            lst.append(tree.val)
            if tree.right:
                inOrder(tree.right)
                
                
        inOrder(root)
        for i in range(len(lst)-1):
            res.append(abs(lst[i]-lst[i+1]))
        # print(res)
        return min(res)
            