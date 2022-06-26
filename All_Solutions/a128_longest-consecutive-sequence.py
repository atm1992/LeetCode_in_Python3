# -*- coding: UTF-8 -*-
"""
title: 最长连续序列
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.


Example 1:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9


Constraints:
0 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
"""
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """哈希表"""
        res = 0
        num_set = set(nums)
        n = len(nums)
        # 每个元素最多被访问2次，因此时间复杂度为O(2n)，也属于O(n)
        for num in num_set:
            # 只有当元素是连续序列的起始值时，才会进入当前条件
            if num - 1 not in num_set:
                tmp_res = 1
                while num + 1 in num_set:
                    tmp_res += 1
                    num += 1
                res = max(res, tmp_res)
                # 剪枝。若某个连续序列的长度超过原始序列长度的一半，则不可能还会有比它更长的连续序列了。
                if res >= (n + 1) // 2:
                    break
        return res


if __name__ == '__main__':
    print(Solution().longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))
