from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        根据二叉搜索树的性质， 其中第k个遍历的元素就是第k小的。
        """
        # ans = []
        self.count = 0
        self.ans: None | int = None

        def inorder(node: Optional[TreeNode]):
            if not node:
                return

            inorder(node.left)

            self.count += 1
            if self.count == k:
                self.ans = node.val
                raise StopIteration  # 提前终止

            inorder(node.right)

        try:
            inorder(root)
        except StopIteration:
            pass
        return self.ans
        #
        # if self.count < k:
        #     return -1
