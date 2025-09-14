from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        """

        思路是：
        1. 记录每个字符最后出现的位置。
        2. 对于每次划分， 如果包含字符串i就要包含字符串i的最后位置。
        3. 从第0个开始划分。
        """

        last_pos = {}

        for idx, char in enumerate(s):
            last_pos[char] = idx

        start = 0  # 当前的开始  都是当前划分的
        end = 0  # 当前的结束
        ans = []

        for idx, char in enumerate(s):
            end = max(last_pos[char], end)

            if idx == end:  # 到达结束的时候, 这种叫边界扩展法， 在跳跃游戏2里面也有
                ans.append(end - start + 1)
                start = end + 1

        return ans
