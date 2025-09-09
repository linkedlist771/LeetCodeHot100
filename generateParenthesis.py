from copy import copy
from typing import List, Optional


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        算法步骤

        状态维护：

        current_brackets：当前正在构建的括号字符串
        left_bracket_num：已使用的左括号 ( 数量
        right_bracket_number：已使用的右括号 ) 数量


        终止条件：
        pythonif left_bracket_num == right_bracket_number == n:
            ans.append(copy(current_brackets))  # 找到一个有效组合

        递归规则（关键的剪枝条件）：

        添加左括号：if left_bracket_num < n

        只要左括号还没用完就可以添加


        添加右括号：if left_bracket_num > right_bracket_number

        只有当左括号数量大于右括号时才能添加右括号（保证有效性）




        回溯操作：
        pythoncurrent_brackets = current_brackets[:-1]  # 撤销刚才的选择
        """
        # 这个也是用回溯解决
        ans = []

        def backtrack(
            current_brackets: str, left_bracket_num: int, right_bracket_number: int
        ):
            if left_bracket_num == right_bracket_number == n:
                ans.append(copy(current_brackets))
                return

            # 不满足嘛

            if left_bracket_num < n:
                # 左括号小于有括号数量， 不会发生 =>>>
                # 加左括号
                current_brackets += "("
                backtrack(current_brackets, left_bracket_num + 1, right_bracket_number)
                current_brackets = current_brackets[:-1]  # 回溯：删除最后添加的字符

            if left_bracket_num > right_bracket_number:
                current_brackets += ")"

                backtrack(current_brackets, left_bracket_num, right_bracket_number + 1)
                current_brackets = current_brackets[:-1]  # 回溯：删除最后添加的字符

        backtrack("", 0, 0)

        return ans
