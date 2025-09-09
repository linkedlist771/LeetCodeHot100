from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        思路是这样的， 记录当前的和， 然后试着添加每一个元素，如果达到和退出。大于就减枝、
        """

        ans = []
        n = len(candidates)

        current_result = []
        # 可以先排序一下提升速度
        candidates = sorted(candidates)

        def backtrack(start: int, current_sum: int):
            if current_sum == target:
                ans.append(current_result.copy())
                return
            elif current_sum > target:
                # 减枝
                return

            # 然后开始回溯
            for i in range(start, n):
                number = candidates[i]
                current_result.append(number)
                backtrack(i, current_sum + number)
                current_result.pop()  # 回溯！这是关键

        backtrack(0, 0)
        return ans
