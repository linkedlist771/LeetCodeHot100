from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.


        思路1：
        遍历整个矩阵， 维护两个数组，记录需要被置为0行和列。


        思路2:
        把第一列的数组用来记录位置，然后只用给出两个变量用来记录第一列和第一行是不是
        是不是需要置为0.

        """
        first_row = False
        first_col = False

        m = len(matrix)
        n = len(matrix[0])
        # 检查第一行
        for j in range(n):
            if matrix[0][j] == 0:
                first_row = True

        # 检查第一列
        for i in range(m):
            if matrix[i][0] == 0:
                first_col = True

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0  # 标记第i行需要置零
                    matrix[0][j] = 0  # 标记第j列需要置零

                    # cols.add(j)

        for i in range(1, m):
            for j in range(1, n):
                # 但是矩阵内可能已经就有1了
                if (matrix[i][0] == 0 or matrix[0][j] == 0) and matrix[i][j] != 0:
                    matrix[i][j] = 0

        # 使用first row和first col来置0
        if first_row:
            # = True

            for j in range(n):
                matrix[0][j] = 0
        if first_col:
            # 检查第一列
            for i in range(m):
                matrix[i][0] = 0

        # 然后把0列和1列置为0. 如果需要的话。

        # 最后置为0

        # rows = set()
        # cols = set()
        #
        # m = len(matrix)
        # n= len(matrix[0])
        #
        #
        # for i in range(m):
        #     for j in range(n):
        #         if matrix[i][j] == 0:
        #             rows.add(i)
        #             cols.add(j)
        #
        # for i in range(m):
        #     for j in range(n):
        #         if (i in rows or  j in cols) and matrix[i][j] != 0:
        #             matrix[i][j] = 0
