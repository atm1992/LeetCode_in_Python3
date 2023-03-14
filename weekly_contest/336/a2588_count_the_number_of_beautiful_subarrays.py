# -*- coding: UTF-8 -*-
"""
title: 统计美丽子数组数目
You are given a 0-indexed integer array nums. In one operation, you can:
    Choose two different indices i and j such that 0 <= i, j < nums.length.
    Choose a non-negative integer k such that the kth bit (0-indexed) in the binary representation of nums[i] and nums[j] is 1.
    Subtract 2^k from nums[i] and nums[j].
A subarray is beautiful if it is possible to make all of its elements equal to 0 after applying the above operation any number of times.
Return the number of beautiful subarrays in the array nums.
A subarray is a contiguous non-empty sequence of elements within an array.


Example 1:
Input: nums = [4,3,1,2,4]
Output: 2
Explanation: There are 2 beautiful subarrays in nums: [4,3,1,2,4] and [4,3,1,2,4].
- We can make all elements in the subarray [3,1,2] equal to 0 in the following way:
  - Choose [3, 1, 2] and k = 1. Subtract 21 from both numbers. The subarray becomes [1, 1, 0].
  - Choose [1, 1, 0] and k = 0. Subtract 20 from both numbers. The subarray becomes [0, 0, 0].
- We can make all elements in the subarray [4,3,1,2,4] equal to 0 in the following way:
  - Choose [4, 3, 1, 2, 4] and k = 2. Subtract 22 from both numbers. The subarray becomes [0, 3, 1, 2, 0].
  - Choose [0, 3, 1, 2, 0] and k = 0. Subtract 20 from both numbers. The subarray becomes [0, 2, 0, 2, 0].
  - Choose [0, 2, 0, 2, 0] and k = 1. Subtract 21 from both numbers. The subarray becomes [0, 0, 0, 0, 0].

Example 2:
Input: nums = [1,10,4]
Output: 0
Explanation: There are no beautiful subarrays in nums.


Constraints:
1 <= nums.length <= 10^5
0 <= nums[i] <= 10^6
"""
from collections import defaultdict
from typing import List


class Solution:
    def beautifulSubarrays(self, nums: List[int]) -> int:
        """
        前缀异或和 + 哈希表
        注意：[0] 也是一个美丽子数组。applying the above operation any number of times 包含了操作0次，
        不操作的话，就不受 i != j 的限制了，所以只有一个元素0的子数组也是美丽子数组
        """
        sum2cnt = defaultdict(int)
        sum2cnt[0] = 1
        pre_sum = 0
        for num in nums:
            pre_sum ^= num
            sum2cnt[pre_sum] += 1
        # 从相同的多个pre_sum中任选两个进行组合，每种组合都是一个美丽子数组
        return sum(cnt * (cnt - 1) // 2 for cnt in sum2cnt.values() if cnt > 1)

    def beautifulSubarrays_2(self, nums: List[int]) -> int:
        sum2cnt = defaultdict(int)
        sum2cnt[0] = 1
        res, pre_sum = 0, 0
        for num in nums:
            pre_sum ^= num
            res += sum2cnt[pre_sum]
            sum2cnt[pre_sum] += 1
        return res


if __name__ == '__main__':
    print(Solution().beautifulSubarrays(nums=[4, 3, 1, 2, 4]))
