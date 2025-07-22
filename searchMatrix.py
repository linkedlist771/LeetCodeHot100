from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        每次就是走右边或者走下边的比较， 肯定就是这两种。

        Z字查找: 从左下角开始找， 右边的比这个大，上面的比这个小：
        1. 如果这个比target大， 那么就网上走。
        2. 如果小，那么往右走

        """

        m = len(matrix)
        n = len(matrix[0])
        x = 0
        y = n - 1

        while x < m and y >= 0:
            current = matrix[x][y]

            if current == target:
                return True

            elif current > target:
                # 往上走
                y -= 1
            else:
                # 往右走
                x += 1
        return False
