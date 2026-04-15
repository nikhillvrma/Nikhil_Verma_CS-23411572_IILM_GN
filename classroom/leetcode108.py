# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def create(start, end):
            if start > end:
                return None
            mid = (start + end) // 2
            root = TreeNode(nums[mid], start, end)
            root.left = create(start, mid - 1)
            root.right = create(mid + 1, end)
            return root

        return create(0, len(nums) - 1)
