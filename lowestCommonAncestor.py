from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        """
        如果root 就是p或者q，直接返回。
        然后从root的左右分别找p 和 q的lca， 然后呢：
        1. 两者都存在， 证明 p 和 q分别在这个root的左右子树。 这个root就是lca。
        2. 两者只有一个存在， 证明都在一个子树上， 返回哪个存在的子树。
        """
        if not root:
            return None

        if root == q or root == p:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root

        return left or right
