# -*- coding: UTF-8 -*-
"""
title: 最大交换
You are given an integer num. You can swap two digits at most once to get the maximum valued number.
Return the maximum valued number you can get.


Example 1:
Input: num = 2736
Output: 7236
Explanation: Swap the number 2 and the number 7.

Example 2:
Input: num = 9973
Output: 9973
Explanation: No swap.


Constraints:
0 <= num <= 10^8
"""


class Solution:
    def maximumSwap(self, num: int) -> int:
        """贪心。待交换的大数字必须在待交换的小数字右侧，并尽量大；待交换的小数字必须比待交换的大数字小，并尽量靠左。"""
        nums = list(str(num))
        n = len(nums)
        max_idx = n - 1
        l_idx, r_idx = -1, -1
        for i in range(n - 2, -1, -1):
            if nums[i] > nums[max_idx]:
                max_idx = i
            elif nums[i] < nums[max_idx]:
                # l_idx 尽量靠左，nums[r_idx] 尽量大
                l_idx, r_idx = i, max_idx
        if l_idx == -1:
            return num
        nums[l_idx], nums[r_idx] = nums[r_idx], nums[l_idx]
        return int(''.join(nums))


if __name__ == '__main__':
    print(Solution().maximumSwap(6436))
