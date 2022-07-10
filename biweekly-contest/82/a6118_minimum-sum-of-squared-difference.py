# -*- coding: UTF-8 -*-
"""
title: 最小差值平方和
You are given two positive 0-indexed integer arrays nums1 and nums2, both of length n.
The sum of squared difference of arrays nums1 and nums2 is defined as the sum of (nums1[i] - nums2[i])^2 for each 0 <= i < n.
You are also given two positive integers k1 and k2. You can modify any of the elements of nums1 by +1 or -1 at most k1 times. Similarly, you can modify any of the elements of nums2 by +1 or -1 at most k2 times.
Return the minimum sum of squared difference after modifying array nums1 at most k1 times and modifying array nums2 at most k2 times.
Note: You are allowed to modify the array elements to become negative integers.


Example 1:
Input: nums1 = [1,2,3,4], nums2 = [2,10,20,19], k1 = 0, k2 = 0
Output: 579
Explanation: The elements in nums1 and nums2 cannot be modified because k1 = 0 and k2 = 0.
The sum of square difference will be: (1 - 2)^2 + (2 - 10)^2 + (3 - 20)^2 + (4 - 19)^2 = 579.

Example 2:
Input: nums1 = [1,4,10,12], nums2 = [5,8,6,9], k1 = 1, k2 = 1
Output: 43
Explanation: One way to obtain the minimum sum of square difference is:
- Increase nums1[0] once.
- Increase nums2[2] once.
The minimum of the sum of square difference will be:
(2 - 5)^2 + (4 - 8)^2 + (10 - 7)^2 + (12 - 9)^2 = 43.
Note that, there are other ways to obtain the minimum of the sum of square difference, but there is no way to obtain a sum smaller than 43.


Constraints:
n == nums1.length == nums2.length
1 <= n <= 10^5
0 <= nums1[i], nums2[i] <= 10^5
0 <= k1, k2 <= 10^9
"""
import heapq
from collections import defaultdict
from typing import List


class Solution:
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
        """贪心 + 优先队列"""
        diff = []
        for n1, n2 in zip(nums1, nums2):
            if n1 != n2:
                diff.append(abs(n1 - n2))
        cnt = k1 + k2
        if cnt >= sum(diff):
            return 0
        num2cnt = defaultdict(int)
        for num in diff:
            # 因为之后要使用最小堆，所以num前面添加了一个负号
            num2cnt[-num] += 1
        nums = list(num2cnt.keys())
        # 最小堆
        heapq.heapify(nums)
        while cnt > 0:
            n1 = heapq.heappop(nums)
            if nums:
                n2 = heapq.heappop(nums)
                # n1、n2都是负数
                if (n2 - n1) * num2cnt[n1] <= cnt:
                    cnt -= (n2 - n1) * num2cnt[n1]
                    num2cnt[n2] += num2cnt[n1]
                    num2cnt.pop(n1)
                    heapq.heappush(nums, n2)
                    continue
            div, mod = divmod(cnt, num2cnt[n1])
            if div == 0:
                num2cnt[n1] -= mod
                num2cnt[n1 + 1] += mod
            else:
                num2cnt[n1 + div] += num2cnt[n1] - mod
                num2cnt[n1 + div + 1] += mod
                num2cnt.pop(n1)
            break
        res = 0
        for num, cnt in num2cnt.items():
            res += num * num * cnt
        return res


if __name__ == '__main__':
    print(Solution().minSumSquareDiff(nums1=[1, 4, 10, 12], nums2=[5, 8, 6, 9], k1=1, k2=1))
