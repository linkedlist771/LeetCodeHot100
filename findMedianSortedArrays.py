from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """

        定义一个函数： 找到两个数组第k小的。


        然后根据奇和偶判获取中位数candidate。
        第k小的：
        每次取数组较短的一个， 然后取 k // 2 和自己长度取小。
        剩下的就是 n - i , 判断这两个最大的大小， 然后缩减区间范围。
        注意下边界条例的处理。
        """

        def find_kth(nums1: List[int], nums2: List[int], k: int) -> int:
            m = len(nums1)
            n = len(nums2)
            if m > n:
                # 把nums1 变成较小的
                nums1, nums2 = nums2, nums1
                m, n = n, m

            if k == 1:
                if nums1 and nums2:
                    return min(nums1[0], nums2[0])

            if not nums1:
                # 边界条件
                return nums2[k - 1]

            i = min(k // 2, m)
            j = k - i

            if nums1[i - 1] > nums2[j - 1]:
                # 左边的更大， 排除右边的
                return find_kth(nums1, nums2[j:], i)

            else:
                return find_kth(nums1[i:], nums2, j)

        length = len(nums1) + len(nums2)
        if length % 2 == 0:
            return (
                find_kth(nums1, nums2, length // 2)
                + find_kth(nums1, nums2, length // 2 + 1)
            ) / 2.0
        else:
            return find_kth(nums1, nums2, (length + 1) // 2)
