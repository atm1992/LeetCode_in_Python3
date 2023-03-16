# -*- coding: UTF-8 -*-
"""
title: 统计中位数为 K 的子数组
You are given an array nums of size n consisting of distinct integers from 1 to n and a positive integer k.
Return the number of non-empty subarrays in nums that have a median equal to k.
Note:
    The median of an array is the middle element after sorting the array in ascending order. If the array is of even length, the median is the left middle element.
        For example, the median of [2,3,1,4] is 2, and the median of [8,4,3,5,1] is 4.
    A subarray is a contiguous part of an array.


Example 1:
Input: nums = [3,2,1,4,5], k = 4
Output: 3
Explanation: The subarrays that have a median equal to 4 are: [4], [4,5] and [1,4,5].

Example 2:
Input: nums = [2,3,1], k = 3
Output: 1
Explanation: [3] is the only subarray that has a median equal to 3.


Constraints:
n == nums.length
1 <= n <= 10^5
1 <= nums[i], k <= n
The integers in nums are distinct.
"""
from collections import defaultdict
from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        """
        前缀和 + 哈希表
        将大于k的数记为1，小于k的数记为-1，等于k的数记为0
        要想子数组的中位数为k，需满足以下两个条件：
        1、子数组中必须包含k，等于k的元素有且只有一个
        2、大于k的元素个数 = 小于k的元素个数，此时子数组的长度为奇数；大于k的元素个数 = 小于k的元素个数 + 1，此时子数组的长度为偶数。
        因此子数组的和需要为0或1，即 pre_sum[j] - pre_sum[i] = 0 或 1  ——>  pre_sum[i] = pre_sum[j] 或 pre_sum[j] - 1
        使用哈希表来记录各个pre_sum的个数，将元素j作为结尾的满足要求的子数组个数为 pre_sum[j]的个数 + pre_sum[j] - 1 的个数
        """
        sum2cnt = defaultdict(int)
        # 初始时，前缀和为0的情况有一种，此时为空数组
        sum2cnt[0] = 1
        res, pre_sum, k_visited = 0, 0, False
        for num in nums:
            if num == k:
                k_visited = True
                # 此时不能将pre_sum记录到sum2cnt中，因为假设k的下标为i，则之后的pre_sum[j] - pre_sum[i]得到的子数组之和是不包含元素k的
                # 下面的sum2cnt[pre_sum]中包含了 [k] 这种子数组
                res += sum2cnt[pre_sum] + sum2cnt[pre_sum - 1]
                continue
            pre_sum += 1 if num > k else -1
            if not k_visited:
                sum2cnt[pre_sum] += 1
            else:
                res += sum2cnt[pre_sum] + sum2cnt[pre_sum - 1]
        return res


if __name__ == '__main__':
    print(Solution().countSubarrays(nums=[3, 2, 1, 4, 5], k=4))
