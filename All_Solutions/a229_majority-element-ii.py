# -*- coding: UTF-8 -*-
"""
title: 求众数 II
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.


Example 1:
Input: nums = [3,2,3]
Output: [3]

Example 2:
Input: nums = [1]
Output: [1]

Example 3:
Input: nums = [1,2]
Output: [1,2]


Constraints:
1 <= nums.length <= 5 * 10^4
-10^9 <= nums[i] <= 10^9

Follow up: Could you solve the problem in linear time and in O(1) space?
"""
from collections import defaultdict
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        """哈希表"""
        n = len(nums)
        num2cnt = defaultdict(int)
        for num in nums:
            num2cnt[num] += 1
        return [k for k, v in num2cnt.items() if v > n // 3]

    def majorityElement_2(self, nums: List[int]) -> List[int]:
        """
        摩尔投票法。出现次数超过1/3的元素最多两个，这两个元素的出现次数加起来超过2/3，因此不可能还有其它元素能超过1/3。
        每次选择三个互不相同的元素进行删除(抵消)
        """
        res = []
        n = len(nums)
        # vote_1 为num_1的票数，vote_2 为num_2的票数
        num_1, num_2 = 0, 0
        vote_1, vote_2 = 0, 0
        for num in nums:
            if num == num_1 and vote_1 > 0:
                vote_1 += 1
            elif num == num_2 and vote_2 > 0:
                vote_2 += 1
            # 先给num_1赋值，等下一次遇到不同的值时，再给num_2赋值
            elif vote_1 == 0:
                num_1 = num
                vote_1 += 1
            # 注意：这里是elif，num赋值给了num_1之后，就不会再进入这里了，所以不存在 num_1 == num_2
            elif vote_2 == 0:
                num_2 = num
                vote_2 += 1
            # 若当前num既不等于num_1，也不等于num_2，则相互抵消一次
            else:
                vote_1 -= 1
                vote_2 -= 1
        if vote_1 > 0 and nums.count(num_1) > n // 3:
            res.append(num_1)
        if vote_2 > 0 and nums.count(num_2) > n // 3:
            res.append(num_2)
        return res


if __name__ == '__main__':
    print(Solution().majorityElement_2([1, 2]))
