from typing import List, Optional


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        """
        思路： 二分建立树， 由于数组是排序好的
        每次取其中中间， 然后构建二叉树
        """
        n = len(nums)

        def build(left: int, right: int) -> Optional[TreeNode]:
            if left > right:
                return

            mid = (right - left) // 2 + left

            val = nums[mid]
            root = TreeNode(val)
            root.left = build(left, mid - 1)  # 左边
            root.right = build(mid + 1, right)

            return root

        return build(0, n - 1)
