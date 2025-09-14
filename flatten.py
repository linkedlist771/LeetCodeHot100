from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        # 最简单的思路， 先前序遍历 存储节点， 然后链接上

        nodes = []

        def preorder(node: Optional[TreeNode]):
            if not node:
                return
            nodes.append(node)
            preorder(node.left)
            preorder(node.right)

        preorder(root)

        # 链接这个nodes:
        if not nodes:
            return None
        dummy = TreeNode()
        dummy.right = nodes[0]

        for i in range(len(nodes) - 1):
            node = nodes[i]
            node.left = None
            node.right = nodes[i + 1]

        nodes[-1].left = None
        nodes[-1].right = None
