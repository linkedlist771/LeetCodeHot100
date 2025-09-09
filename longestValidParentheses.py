class Solution:
    def longestValidParentheses(self, s: str) -> int:
        """
        思路是这样的：
        1. 记录最后没被匹配的右括号。
        2. 然后pop统计。
        """

        stack = [-1]

        max_bracket_length = 0

        for idx, char in enumerate(s):
            if char == "(":
                stack.append(idx)

            else:  # ')'
                stack.pop()
                if not stack:
                    stack.append(idx)
                else:
                    length = idx - stack[-1]
                    max_bracket_length = max(length, max_bracket_length)

        return max_bracket_length
