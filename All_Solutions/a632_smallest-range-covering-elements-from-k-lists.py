# -*- coding: UTF-8 -*-
"""
title: 最小区间
You have k lists of sorted integers in non-decreasing order. Find the smallest range that includes at least one number from each of the k lists.
We define the range [a, b] is smaller than range [c, d] if b - a < d - c or a < c if b - a == d - c.


Example 1:
Input: nums = [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]
Output: [20,24]
Explanation:
List 1: [4, 10, 15, 24,26], 24 is in range [20,24].
List 2: [0, 9, 12, 20], 20 is in range [20,24].
List 3: [5, 18, 22, 30], 22 is in range [20,24].

Example 2:
Input: nums = [[1,2,3],[1,2,3],[1,2,3]]
Output: [1,1]


Constraints:
nums.length == k
1 <= k <= 3500
1 <= nums[i].length <= 50
-10^5 <= nums[i][j] <= 10^5
nums[i] is sorted in non-decreasing order.
"""
import heapq
from collections import defaultdict
from typing import List


class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        """贪心 + 最小堆。推荐此方法"""
        # -10^5 <= nums[i][j] <= 10^5
        left, right = -10 ** 5, 10 ** 5
        queue = []
        max_num = -10 ** 5
        for row, item in enumerate(nums):
            # 将每个列表中的第一个元素(最小值)放入最小堆
            queue.append((item[0], row, 0))
            # 记录最小堆中已有元素的最大值
            max_num = max(max_num, item[0])
        heapq.heapify(queue)
        while True:
            num, row, col = heapq.heappop(queue)
            # max_num 是最小堆中已有元素的最大值，num 是最小堆中已有元素的最小值
            if max_num - num < right - left:
                left, right = num, max_num
            if col == len(nums[row]) - 1:
                break
            heapq.heappush(queue, (nums[row][col + 1], row, col + 1))
            max_num = max(max_num, nums[row][col + 1])
        return [left, right]

    def smallestRange_2(self, nums: List[List[int]]) -> List[int]:
        """哈希表 + 滑动窗口。参考LeetCode题76"""
        # 记录每个num分别在哪些列表中出现过。5 ——> [0, 2, 2] 表示元素5分别在下标为0以及下标为2的列表中出现过，并且在下标为2的列表中出现过两次
        num2idxs = defaultdict(list)
        # -10^5 <= nums[i][j] <= 10^5
        max_num, min_num = -10 ** 5, 10 ** 5
        for idx, item in enumerate(nums):
            for num in item:
                num2idxs[num].append(idx)
                min_num = min(min_num, num)
                max_num = max(max_num, num)
        left, right = min_num, max_num
        start = end = min_num
        # 总共n个列表
        n = len(nums)
        # cnt 用来记录有多少个列表中的元素落在[start, end]内。当cnt == n时，[start, end] 是一个符合题目要求的区间，然后更新left、right
        cnt = 0
        # 记录n个列表中，每个列表分别有多少个元素落在[start, end]内。最终要求每个列表至少有1个元素落在[start, end]内
        idx2cnt = [0] * n
        while end <= max_num:
            if end in num2idxs:
                for idx in num2idxs[end]:
                    idx2cnt[idx] += 1
                    # 只在idx2cnt[idx]为1时，cnt才加1。而不是>=时加1，那样会重复加1
                    cnt += idx2cnt[idx] == 1
                # 开始收缩start，并且更新left、right
                while cnt == n:
                    if end - start < right - left:
                        left, right = start, end
                    if start in num2idxs:
                        for idx in num2idxs[start]:
                            idx2cnt[idx] -= 1
                            cnt -= idx2cnt[idx] == 0
                    start += 1
            end += 1
        return [left, right]


if __name__ == '__main__':
    print(Solution().smallestRange_2(nums=[[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]]))
