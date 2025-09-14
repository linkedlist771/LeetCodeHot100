from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        """
        这一题还是用的前缀和的思路， 和找数组里面的类似， 唯一不同的时，
        获取匹配次数然后加和。
        的时候需要从左右子树进行， 并且要回溯， 因为比如从左子树回到根节点
        然后再处理右子树的时候需要去掉左边的处理的路径。
        """
        self.prefix_sum_times = {0: 1}
        self.count = 0

        def path_sum(node: Optional[TreeNode], current_sum: int):
            if not node:
                return

            val = node.val
            current_sum += val
            count = self.prefix_sum_times.get(current_sum - targetSum, 0)
            self.count += count
            # 先查找后添加。
            self.prefix_sum_times[current_sum] = (
                self.prefix_sum_times.get(current_sum, 0) + 1
            )
            path_sum(node.left, current_sum)
            path_sum(node.right, current_sum)
            # 回溯
            self.prefix_sum_times[current_sum] -= 1

        path_sum(root, 0)
        return self.count
