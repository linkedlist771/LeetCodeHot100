from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        采用回溯的方式来求解这个问题。
        尝试使用每个， 然后擦掉。
        """
        ans = []
        n = len(nums)

        def backtrack(path: list):
            if n == len(path):
                # 退出 顺便添加这个解决方案
                ans.append(
                    path.copy()
                )  # 回溯过程中的修改：在回溯过程中，同一个 path 对象会被不断修改（通过 path.append() 和 path.pop()）。
                return

            for i in nums:
                if i not in path:
                    # 没有尝试过，
                    path.append(i)
                    backtrack(path)
                    path.pop()  # 尝试其他的

        backtrack([])
        return ans
