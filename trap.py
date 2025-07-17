from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        """
        思路， 每个位置能接的最多的雨水取决于其左边最大的值和右边最大的取小，
        然后减去当前自己的值。

        双指针， 从左边和右边往中间， 由于两者都是从边缘往中间， 所以左指针
        左边得到的一定是left max, 对于自己而言， 对于右指针而言，右边的一定
        是right max

        每次遍历判断left和right的值， 我们取其中较小的来判断，比如height[left]比较小。

        并且此时的leftMax 一定比 右边的最大值还要小。

        反证法证明：    若此时出现 leftMax > rightMax，说明左边曾经见过一堵比右侧任何墙都高的墙。然而我们只有在 “当前高度更矮” 时才移动左指针；当左边出现如此高墙时，左侧就不会再矮了，接下来轮到右指针不停左移并不断抬高 rightMax 直到 ≥ leftMax（或指针相遇）。因此矛盾。


        """

        size = len(height)

        left = 0
        right = size - 1
        left_max = right_max = 0
        water = 0
        while left < right:
            left_max = max(height[left], left_max)
            right_max = max(height[right], right_max)
            if height[left] < height[right]:
                water += left_max - height[left]
                left += 1
            else:
                water += right_max - height[right]
                right -= 1

        return water
