# Definition for a binary tree node.


from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        这个就是使用递归就行了， 分别求两个左子树和右子树的最大深度， 然后
        取其中大值就行了。
        """
        if not root:
            return 0

        left_max_depth = self.maxDepth(root.left)
        right_max_depth = self.maxDepth(root.right)

        return max(left_max_depth, right_max_depth) + 1  # 这个是取两个子树种更长的
        # 由于是递归，一层层返回。
