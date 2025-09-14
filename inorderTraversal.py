# Definition for a binary tree node.

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """

        思路：
        中序：
        左 递归
        中 # 访问
        右 递归
        """
        ans = []

        def inter_order(node: Optional[TreeNode]):
            if not node:
                # 为空
                return

            # 中序就是左中右。

            inter_order(node.left)
            ans.append(node.val)
            inter_order(node.right)

        inter_order(root)
        return ans
