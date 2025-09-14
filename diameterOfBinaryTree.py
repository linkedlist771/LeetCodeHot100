from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        二叉树的直径就是左右子树最大深度加起来。
        那就是在求深度的过程中顺便记录直径。
        """
        global diameter
        diameter = 0

        def depth(node: Optional[TreeNode]) -> int:
            if not node:
                return 0

            left_depth = depth(node.left)
            right_depth = depth(node.right)
            global diameter
            diameter = max(diameter, left_depth + right_depth)

            return max(left_depth, right_depth) + 1

        depth(root)
        return diameter
