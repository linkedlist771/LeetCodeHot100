from copy import deepcopy
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        """
        两个树互为镜像，当且仅当：
        1. 树1的左子树和树2的右子树一样
        2. 树1的右子树和树2的左子树一样
        3. 他们的值也一样。
        """

        if not root:
            return False

        def check(tree1: Optional[TreeNode], tree2: Optional[TreeNode]) -> bool:
            if not tree1 and not tree2:
                return True  # 两者都是None， 那么子树一样
            if not tree1 or not tree2:
                return False  # 一个非空

            return (
                (tree1.val == tree2.val)
                and check(tree1.right, tree2.left)
                and check(tree1.left, tree2.right)
            )

        return check(root.left, root.right)
