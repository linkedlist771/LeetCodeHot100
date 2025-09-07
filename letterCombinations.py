from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """
        思路就是回溯每个位置， 一共就n个digits
        """
        if not digits:
            return []
        phone_number_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        combination = []  # 存储当前的组合
        combinations = []  # 存储所有的组合

        n = len(digits)

        def backtrack(index: int):
            if index == n:  # when index equals n , break
                combinations.append("".join(combination))
                return

            else:
                chrs = phone_number_map[digits[index]]
                for chr in chrs:
                    combination.append(chr)
                    backtrack(index + 1)  # next
                    combination.pop()  # change another one to testify

        backtrack(0)
        return combinations
