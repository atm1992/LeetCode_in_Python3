# -*- coding: utf-8 -*-
# @date: 2023/3/25
# @author: liuquan
"""
title: 使数组元素全部相等的最少操作次数
You are given an array nums consisting of positive integers.
You are also given an integer array queries of size m. For the ith query, you want to make all of the elements of nums equal to queries[i]. You can perform the following operation on the array any number of times:
    Increase or decrease an element of the array by 1.
Return an array answer of size m where answer[i] is the minimum number of operations to make all elements of nums equal to queries[i].
Note that after each query the array is reset to its original state.


Example 1:
Input: nums = [3,1,6,8], queries = [1,5]
Output: [14,10]
Explanation: For the first query we can do the following operations:
- Decrease nums[0] 2 times, so that nums = [1,1,6,8].
- Decrease nums[2] 5 times, so that nums = [1,1,1,8].
- Decrease nums[3] 7 times, so that nums = [1,1,1,1].
So the total number of operations for the first query is 2 + 5 + 7 = 14.
For the second query we can do the following operations:
- Increase nums[0] 2 times, so that nums = [5,1,6,8].
- Increase nums[1] 4 times, so that nums = [5,5,6,8].
- Decrease nums[2] 1 time, so that nums = [5,5,5,8].
- Decrease nums[3] 3 times, so that nums = [5,5,5,5].
So the total number of operations for the second query is 2 + 4 + 1 + 3 = 10.

Example 2:
Input: nums = [2,9,6,3], queries = [10]
Output: [20]
Explanation: We can increase each value in the array to 10. The total number of operations will be 8 + 1 + 4 + 7 = 20.


Constraints:
n == nums.length
m == queries.length
1 <= n, m <= 10^5
1 <= nums[i], queries[i] <= 10^9
"""
from typing import List


class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        """排序 + 前缀和 + 二分查找 + 哈希表"""
        nums.sort()
        n = len(nums)
        pre_sum = [0]
        for num in nums:
            pre_sum.append(pre_sum[-1] + num)
        target2times = {}
        res = []
        for target in queries:
            if target in target2times:
                res.append(target2times[target])
                continue
            if nums[-1] <= target:
                res.append(n * target - pre_sum[-1])
                target2times[target] = res[-1]
                continue
            left, right = 0, n - 1
            # 在有序nums中二分查找第一个大于等于target的元素下标
            while left < right:
                mid = (left + right) // 2
                if nums[mid] >= target:
                    right = mid
                else:
                    left = mid + 1
            times = (left * target - pre_sum[left]) + (pre_sum[-1] - pre_sum[left] - (n - left) * target)
            res.append(times)
            target2times[target] = times
        return res


if __name__ == '__main__':
    print(Solution().minOperations(nums=[3, 1, 6, 8], queries=[1, 5]))
