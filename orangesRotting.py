from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        所以说bfs和dfs主要的区别就是前者是queue 后者是stack

        思路：
        1. 检查所有的腐烂位置添加到双端队列里面，， 统计新鲜数量。
        2. 开始BFS，用双端队列， 但是从的是当前的双端队列的数量开始遍历。
        每次popleft。
        3. 然后bfs的过程中加到tail上， 并不会影响当前一轮扩散。
        """
        m = len(grid)
        n = len(grid[0])
        q = deque()
        fresh_count = 0

        for i in range(m):
            for j in range(n):
                val = grid[i][j]
                if val == 1:
                    fresh_count += 1
                elif val == 2:
                    q.append((i, j))

        if fresh_count == 0:
            return 0
        minutes = 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while q and fresh_count > 0:
            # 当处理完所有已经添加的腐烂橘子 或者 无新鲜的句子
            # 分别对应1： 有离群节点， 返回-1
            # 对应时间
            rotten_orange_nums = len(q)
            for _ in range(rotten_orange_nums):
                x, y = q.popleft()
                for dx, dy in directions:
                    nx = x + dx
                    ny = y + dy
                    if (
                        0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1
                    ):  # == 1 代表是新鲜的， 也就是没visited
                        q.append((nx, ny))
                        grid[nx][ny] = 2
                        fresh_count -= 1  # 记得减少
            minutes += 1

        if fresh_count == 0:
            return minutes
        else:
            return -1
