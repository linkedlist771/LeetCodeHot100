class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        思路是这样的:
        定义一个二维dp数组， 其中dp[i][j]代表:
        text1[:i]  text2[:j] 这两个的lcs
        那么:
        if text1[i] == text2[j]:
            dp[i][j] = dp[i-1][j-1]  + 1  # 如果是最长子字符串。 在这里记录最大长度。
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])  # 如果是最长子字符串。  那么为0
        """
        m = len(text1)
        n = text2.__len__()

        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1  # 如果是最长子字符串。 在这里记录最大长度。
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])  # 如果是最长子字符串。  那么为0

        return dp[m][n]
