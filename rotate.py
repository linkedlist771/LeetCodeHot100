from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        # 递归的那啥就行了， 只用给出旋转最外围的就行了。
        """
        (0, 0),   (0, 1),    (0, 2)   .... (0, n-1)
    =>  (0, n-1), (1, n-1),  (2, n-1) .....(n-1, n-1)
        (row, col) => (col, n - row - 1)
        
        1. 先上下翻转矩阵
        2. 然后沿着对角线翻转矩阵就行了。
        """
        n = len(matrix)

        ## 1. 水平翻转

        for row in range(n // 2):
            for col in range(n):
                target_row = n - 1 - row
                matrix[row][col], matrix[target_row][col] = (
                    matrix[target_row][col],
                    matrix[row][col],
                )

        ## 2. 沿着对角线翻转

        for row in range(n):
            for col in range(row):
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]
