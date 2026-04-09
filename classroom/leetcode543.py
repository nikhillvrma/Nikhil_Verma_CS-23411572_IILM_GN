# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def h(root):
            if root == None:
                return 0
            lh = h(root.left)
            rh = h(root.right)
            return max(lh, rh) + 1

        def dia(root):
            if root == None:
                return 0
            lh = h(root.left)
            rh = h(root.right)
            lstDia = dia(root.left)
            rstDia = dia(root.right)
            return max({lh + rh, lstDia, rstDia})

        return dia(root)
