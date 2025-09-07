from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x:x[0])
        ans = [intervals[0]]

        for i in intervals[1:]:
            left, right = i[0], i[1]
            if left > ans[-1][1]:
                ans.append(i)
            elif left <= ans[-1][1]:
                if right > ans[-1][1]:
                    ans[-1][1] = right

            # else:

        return ans

intervals = [[1,3],[2,6],[8,10],[15,18]]
# intervals = [[1,4],[4,5]]
# intervals = [[4,7],[1,4]]
print(Solution().merge(intervals))