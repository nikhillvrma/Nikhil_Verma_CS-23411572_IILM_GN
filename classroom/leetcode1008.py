# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        inorder = sorted(preorder)
        index_map = {val: i for i, val in enumerate(inorder)}
        
        self.preIndex = 0
        
        def build(left, right):
            if left > right:
                return None
            
            root_val = preorder[self.preIndex]
            self.preIndex += 1
            
            root = TreeNode(root_val)
            
            mid = index_map[root_val]
            
            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)
            
            return root
        
        return build(0, len(preorder) - 1)