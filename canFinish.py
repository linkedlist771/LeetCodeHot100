from collections import defaultdict
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        这个就是判断这个有向图，有没有环：
        1. 有环 => False
        2. 无环 => True

        使用三染色方法来解决
        """
        graph = defaultdict(list)

        for course, prerequisite in prerequisites:
            graph[prerequisite].append(course)

        color_map = [0] * numCourses  # 0 未处理，  1正在访问  2处理完的

        def has_cycle(start_point: int) -> bool:
            if color_map[start_point] == 1:
                # 遇到灰色节点，有环
                return True
            elif color_map[start_point] == 2:
                # 已经处理完了
                return False
            color_map[start_point] = 1  # 标记为正在处理。
            for neighbor in graph[start_point]:
                if has_cycle(neighbor):
                    return True

            color_map[start_point] = 2  # 标记为处理完了。

            return False

        for course in range(numCourses):
            if color_map[course] == 0:  # 未处理:
                if has_cycle(course):
                    return False

        return True
