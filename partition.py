from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        """
        将字符串分割成所有可能的回文子串组合。
        核心思路：
        使用回溯算法穷举所有可能的分割方案。从字符串的每个位置开始，
        尝试所有可能的结束位置形成子串，如果子串是回文就加入当前分割方案，
        然后递归处理剩余部分。通过回溯确保探索所有可能的分割组合。

        算法步骤：
        1. 递归函数backtrack(start_idx)处理从start_idx开始的字符串
        2. 结束条件：start_idx == n时，所有字符处理完，保存当前分割方案
        3. 尝试分割：从start_idx到每个可能的end_idx，获取子串s[start_idx:end_idx+1]
        4. 回文检查：只有回文子串才继续处理
        5. 递归+回溯：将回文子串加入方案 → 递归处理剩余部分 → 撤
        """
        n = len(s)

        def is_palindrome(s: str):
            # if len(s) == 1:
            #     return True
            left = 0
            right = len(s) - 1
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        def backtrack(start_idx: int):
            if start_idx == n:
                # 已经结束了，保存这个结果。
                ans.append(current_partition[:])

            for end_idx in range(start_idx, n):
                # 遍历每个结束的位置。

                sub_str = s[start_idx : end_idx + 1]
                if is_palindrome(sub_str):
                    # 记录该分割
                    current_partition.append(sub_str)
                    # 然后从后面的继续开始
                    backtrack(end_idx + 1)
                    current_partition.pop()  # 去掉

        ans = []
        current_partition = []
        backtrack(0)
        return ans
