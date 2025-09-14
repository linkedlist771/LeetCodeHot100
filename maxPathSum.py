from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        """
        思路是这样的， 定义一个max_gain 函数
        定义就是这个节点可以贡献给最大路径和的贡献。
        然和呢， 在求的过程更新最大路径和。
        """
        self.max_path_sum = float("-inf")

        def max_gain(node: TreeNode | None) -> int:
            if not node:
                return 0
            # 这里还要处理，如果贡献是负数， 那么就不选了， 减枝条， 所以贡献是0
            left_gain = max(max_gain(node.left), 0)
            right_gain = max(max_gain(node.right), 0)
            val = node.val
            # 因为可以走两遍
            self.max_path_sum = max(self.max_path_sum, left_gain + right_gain + val)

            # 返回这条路径的最大gain ，要么右边要么左边
            return val + max(left_gain, right_gain)

        max_gain(root)
        return self.max_path_sum
