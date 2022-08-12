# -*- coding: UTF-8 -*-
"""
title: 随机数索引
Given an integer array nums with possible duplicates, randomly output the index of a given target number. You can assume that the given target number must exist in the array.
Implement the Solution class:
    Solution(int[] nums) Initializes the object with the array nums.
    int pick(int target) Picks a random index i from nums where nums[i] == target. If there are multiple valid i's, then each index should have an equal probability of returning.


Example 1:
Input
["Solution", "pick", "pick", "pick"]
[[[1, 2, 3, 3, 3]], [3], [1], [3]]
Output
[null, 4, 0, 2]
Explanation
Solution solution = new Solution([1, 2, 3, 3, 3]);
solution.pick(3); // It should return either index 2, 3, or 4 randomly. Each index should have equal probability of returning.
solution.pick(1); // It should return 0. Since in the array only nums[0] is equal to 1.
solution.pick(3); // It should return either index 2, 3, or 4 randomly. Each index should have equal probability of returning.


Constraints:
1 <= nums.length <= 2 * 10^4
-2^31 <= nums[i] <= 2^31 - 1
target is an integer from nums.
At most 10^4 calls will be made to pick.
"""
from collections import defaultdict
from random import choice, randrange
from typing import List


class Solution:
    """哈希表"""

    def __init__(self, nums: List[int]):
        self.num2idxs = defaultdict(list)
        for idx, num in enumerate(nums):
            self.num2idxs[num].append(idx)

    def pick(self, target: int) -> int:
        return choice(self.num2idxs[target])


class Solution2:
    """
    水塘抽样(蓄水池抽样)，适用于大数据流中的随机抽样。类似于LeetCode题382。本题Python3运行超时
    每次pick时，都完整遍历一次nums，假设当前是第i次(i从1开始)遇到等于target的元素，则从[0,i)中随机选择一个整数，若选出的这个整数等于0，
    则将当前元素的下标暂时作为res，之后若再次随机选出了0，则将那个元素的下标作为新的res，直到遍历完整个nums。
    设nums中有k个等于target的元素，则可证明这k个元素的下标成为最终res的概率是相等的，均为 1/k
    P(第i次遇到等于target的元素,其下标成为最终res)
    = P(第i次随机选出的整数为0) * P(第i+1次随机选出的整数 不 为0) * …… * P(第k次随机选出的整数 不 为0)
    = 1/i * (1 - 1/(i+1)) * …… * (1 - 1/k)
    = 1/i * i/(i+1) * …… * (k-1)/k
    = 1/k
    之所以叫水塘抽样(蓄水池抽样)，可理解为当水塘(蓄水池)满了时，之后每进入一滴水，就同样会有一滴水溢出水塘(蓄水池)，就类似于上面的替换操作。
    水塘抽样(蓄水池抽样)除了可以等概率(1/n)的随机从n个元素中选出1个元素；也可以等概率(k/n)的随机从n个元素中选出k个元素, k > 1。
    """

    def __init__(self, nums: List[int]):
        self.nums = nums

    def pick(self, target: int) -> int:
        i, res = 1, 0
        for idx, num in enumerate(self.nums):
            if num == target:
                # 第1次遇到等于target的元素，从[0,1)中随机选择一个整数，选出的整数只能是0，所以每次pick时，res的值最初都会是第1个等于target的元素下标
                if randrange(i) == 0:
                    res = idx
                i += 1
        return res

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
