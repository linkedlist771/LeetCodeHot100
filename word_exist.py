from typing import List, Optional


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """

        定义一个check函数吗，从一个点出发， 开始检测单词
        第k个位置开始后的，能否匹配下去， 是否能继续匹配下去。
        匹配下去的方法就用回溯， 然后呢， 回溯的时候用DFS，然后DFS
        记得去掉方便回溯。

        """
        directions = [
            (-1, 0), (1, 0),
            (0, 1), (0, -1),

        ]

        m, n = len(board), len(board[0])


        def check(i :int, j: int, k: int):

            if board[i][j] != word[k]:
                return False

            if k == len(word) - 1:
                return True

            result = False
            visited.add((i, j))

            for dx, dy in directions:
                ni = i + dx
                nj = j + dy
                if 0<= ni < m and 0 <= nj < n :
                    # 如果满足这个要求的话。
                    if  (ni ,nj) not in visited:
                        if check(ni, nj, k+1):
                            result = True
                            break
            visited.remove((i, j))

            return result



        visited = set()


        for i in range(m):
            for j in range(n):
                if check(i, j, 0):
                    return True

        return False
