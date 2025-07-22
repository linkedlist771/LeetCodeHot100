from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        从左到右，上到下，右到左，下到上轮流遍, 每次走完后，减小一个边界，
        然后当两个边界其中一个大于另一个， 然后到点就退出。
        """
        m = len(matrix)
        n = len(matrix[0])

        left = 0
        right = n - 1
        top = 0
        bottom = m - 1
        ans = []
        while True:
            # 1. 从左到右
            for i in range(left, right + 1):
                ans.append(matrix[top][i])

            top += 1
            if top > bottom:
                break
            # 2. 从上到下
            for i in range(top, bottom + 1):
                ans.append(matrix[i][right])

            right -= 1

            if right < left:
                break

            # 3. 从右到左
            for i in range(right, left - 1, -1):
                ans.append(matrix[bottom][i])

            bottom -= 1
            if top > bottom:
                break

            # 4. 从下到上。
            for i in range(bottom, top - 1, -1):
                ans.append(matrix[i][left])

            left += 1
            if right < left:
                break
        return ans
