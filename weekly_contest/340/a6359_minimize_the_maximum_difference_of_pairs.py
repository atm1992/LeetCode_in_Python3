# -*- coding: utf-8 -*-
# @date: 2023/4/10
# @author: liuquan
"""
title: 最小化数对的最大差值
You are given a 0-indexed integer array nums and an integer p. Find p pairs of indices of nums such that the maximum difference amongst all the pairs is minimized. Also, ensure no index appears more than once amongst the p pairs.
Note that for a pair of elements at the index i and j, the difference of this pair is |nums[i] - nums[j]|, where |x| represents the absolute value of x.
Return the minimum maximum difference among all p pairs.


Example 1:
Input: nums = [10,1,2,7,1,3], p = 2
Output: 1
Explanation: The first pair is formed from the indices 1 and 4, and the second pair is formed from the indices 2 and 5.
The maximum difference is max(|nums[1] - nums[4]|, |nums[2] - nums[5]|) = max(0, 1) = 1. Therefore, we return 1.

Example 2:
Input: nums = [4,2,1,2], p = 1
Output: 0
Explanation: Let the indices 1 and 3 form a pair. The difference of that pair is |2 - 2| = 0, which is the minimum we can attain.


Constraints:
1 <= nums.length <= 10^5
0 <= nums[i] <= 10^9
0 <= p <= (nums.length)/2
"""
from typing import List


class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        """
        排序 + 二分查找 + 贪心check
        看到这种最小化最大值、最大化最小值的问题，首先应想到二分猜答案
        要使差值最小，就应该让大小相近的两个数进行相减，因为最终结果跟元素下标无关，所以可以先排序
        """

        def check(diff: int) -> bool:
            cnt, i = 0, 1
            while i < n:
                if nums[i] - nums[i - 1] <= diff:
                    cnt += 1
                    if cnt >= p:
                        break
                    i += 2
                else:
                    i += 1
            return cnt >= p

        nums.sort()
        n = len(nums)
        left, right = 0, nums[n - 1] - nums[0]
        while left < right:
            mid = (left + right) // 2
            if check(mid):
                right = mid
            else:
                left = mid + 1
        return left


if __name__ == '__main__':
    print(Solution().minimizeMax(nums=[4, 2, 1, 2], p=1))
