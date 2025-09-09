from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        """
        可以发现以下规律:
            每一行都是由1和上一行的和得到的，这样就简单了。
        """
        ans = []

        for i in range(numRows):
            if i == 0:
                ans.append([1])
            elif i == 1:
                ans.append([1, 1])
            else:
                array = []
                for j in range(i + 1):
                    if j == 0 or j == i:
                        array.append(1)
                    else:
                        array.append(ans[i - 1][j - 1] + ans[i - 1][j])
                ans.append(array)
        return ans
