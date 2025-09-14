from typing import List, Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        思路是这样的：
        1. 前序遍历的第一个节点就是那个root节点， 根据这个来构建树。
        2. 找到root节点在中序中的位置， 左右划分这个前序和中序数组。 这样就行了。
        """
        inorder_val_map = {val: idx for idx, val in enumerate(inorder)}

        def build(pre_start, pre_end, in_start, in_end):
            if pre_start > pre_end:
                return None  # 这里是为什么?  # 当前数组为空的时候不需要构建了。

            root_val = preorder[pre_start]
            root = TreeNode(val=root_val)
            mid = inorder_val_map[root_val]

            left_size = mid - in_start  # 获取左边节点的数量。

            root.left = build(pre_start + 1, pre_start + left_size, in_start, mid - 1)
            root.right = build(pre_start + left_size + 1, pre_end, mid + 1, in_end)
            return root

        n = len(preorder)
        return build(0, n - 1, 0, n - 1)
