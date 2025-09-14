from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        进行前序遍历， 然后根据层级存储。
        """
        ans: List[List[int]] = []

        def preorder(node: Optional[TreeNode], level: int):
            # 在前序遍历里面添加对于层级的存储。
            if not node:
                return
            # print(node.val)
            if level == len(ans):  # 看看到了第几层了
                ans.append([])

            # 当前层里面加上
            ans[level].append(node.val)  # 这时ans[-1]指向的不是当前层，而是最深的那一层

            preorder(node.left, level + 1)
            preorder(node.right, level + 1)

        preorder(root, 0)
        return ans
