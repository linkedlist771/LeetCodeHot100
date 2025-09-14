class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        这个题也是只有一种解法:
        设置dp矩阵:
        大小为: dp[0:m+1][0:n+1]
        其中dp[i][j]
        代表word1前i个子字符串和word2前j个子字符串的最小编辑距离。

        1. 状态转移方程:
        if word1[i-1] == word2[j-1]:
            dp[i][j] = dp[i-1][j-1] # 最后一个字符相同， 直接编辑距离想通

        else:
            # 在插入， 修改， 删除里面三选一最小的， 但是三者都会
            # 带来额外的一次编辑
            dp[i][j] = min(dp[i-1][j] + 1,  dp[i][j-1] + 1, dp[i-1][j-1] + 1)

        2. 边界条件:
        # 当i为空的时候， 需要做j次添加。

        # 同理当j为空时要做i次添加。
        """
        m = len(word1)
        n = len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for j in range(n + 1):
            dp[0][j] = j

        for i in range(m + 1):
            dp[i][0] = i

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]  # 最后一个字符相同， 直接编辑距离想通

                else:
                    # 在插入， 修改， 删除里面三选一最小的， 但是三者都会
                    # 带来额外的一次编辑
                    dp[i][j] = min(
                        dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + 1
                    )

        return dp[m][n]
