from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # 中序遍历， 然后检查是否递增。

        def inorder(node):
            if not node:
                return []
            return inorder(node.left) + [node.val] + inorder(node.right)

        values = inorder(root)
        # 检查是否严格递增
        for i in range(1, len(values)):
            if values[i] <= values[i - 1]:
                return False
        return True

        return inorder(root)
