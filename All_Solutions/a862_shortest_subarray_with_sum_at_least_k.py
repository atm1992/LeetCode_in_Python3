# -*- coding: UTF-8 -*-
"""
title: 和至少为 K 的最短子数组
Given an integer array nums and an integer k, return the length of the shortest non-empty subarray of nums with a sum of at least k. If there is no such subarray, return -1.
A subarray is a contiguous part of an array.


Example 1:
Input: nums = [1], k = 1
Output: 1

Example 2:
Input: nums = [1,2], k = 4
Output: -1

Example 3:
Input: nums = [2,-1,2], k = 3
Output: 3


Constraints:
1 <= nums.length <= 10^5
-10^5 <= nums[i] <= 10^5
1 <= k <= 10^9
"""
from collections import deque
from typing import List


class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        """
        前缀和 + 单调双端队列。注意：这里是单调双端队列，而不是单调栈。
        使用前缀和数组，是为了方便计算子数组的和。
        从前往后遍历前缀和数组，遍历过程中，将符合条件的前缀和加入到双端队列中，双端队列中的前缀和需满足严格单调递增。
        对于当前遍历的前缀和cur_sum(作为子数组的结尾)而言：
        从前往后遍历单调双端队列，判断双端队列的当前队头pre_sum_arr[j] (作为子数组的开头)，是否满足条件cur_sum - pre_sum_arr[j] >= k，
        若满足条件，则此时的子数组长度就是以pre_sum_arr[j]作为子数组开头所能得到的最小长度，即使往后遍历前缀和数组再次遇到了满足 >= k的子数组结尾，
        其长度也必然会大于当前长度。所以之后无需再考虑将当前队头pre_sum_arr[j]作为子数组的开头了，因此可以将其从双端队列的队头pop掉；
        若不满足条件，则双端队列中之后的前缀和(只可能会更大)就更不用考虑了，因为双端队列中的前缀和是严格单调递增的。这说明不存在以cur_sum作为结尾的子数组。

        要想满足 >= k的条件，自然是希望双端队列中的前缀和(作为子数组的开头)越小越好，在把cur_sum加入到双端队列时，若队列末尾的某些前缀和大于等于cur_sum，
        则可直接把队列末尾的那些前缀和pop掉，因为如果往后遍历到的某个前缀和 - 那些前缀和 >= k，那么一定也会满足 该前缀和 - cur_sum >= k，将cur_sum作为子数组开头，数组的长度会更短。
        """
        res = len(nums) + 1
        cur_sum = 0
        # 初始时，(下标为0, 前缀和为0)
        queue = deque([(0, 0)])
        # 将nums的起始下标设置为1
        for i, num in enumerate(nums, 1):
            # 计算前缀和。使用一个变量来记录前缀和，而没有使用一个前缀和数组，节省了空间
            cur_sum += num
            while queue and cur_sum - queue[0][1] >= k:
                res = min(res, i - queue.popleft()[0])
                # 剪枝。提前返回
                if res == 1:
                    return 1
            while queue and queue[-1][1] >= cur_sum:
                queue.pop()
            queue.append((i, cur_sum))
        return res if res < len(nums) + 1 else -1


if __name__ == '__main__':
    print(Solution().shortestSubarray(nums=[2, -1, 2], k=3))
