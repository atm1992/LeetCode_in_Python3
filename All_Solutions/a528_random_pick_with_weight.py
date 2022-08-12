# -*- coding: UTF-8 -*-
"""
title: 按权重随机选择
You are given a 0-indexed array of positive integers w where w[i] describes the weight of the ith index.
You need to implement the function pickIndex(), which randomly picks an index in the range [0, w.length - 1] (inclusive) and returns it. The probability of picking an index i is w[i] / sum(w).
For example, if w = [1, 3], the probability of picking index 0 is 1 / (1 + 3) = 0.25 (i.e., 25%), and the probability of picking index 1 is 3 / (1 + 3) = 0.75 (i.e., 75%).


Example 1:
Input
["Solution","pickIndex"]
[[[1]],[]]
Output
[null,0]
Explanation
Solution solution = new Solution([1]);
solution.pickIndex(); // return 0. The only option is to return 0 since there is only one element in w.

Example 2:
Input
["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
[[[1,3]],[],[],[],[],[]]
Output
[null,1,1,1,1,0]
Explanation
Solution solution = new Solution([1, 3]);
solution.pickIndex(); // return 1. It is returning the second element (index = 1) that has a probability of 3/4.
solution.pickIndex(); // return 1
solution.pickIndex(); // return 1
solution.pickIndex(); // return 1
solution.pickIndex(); // return 0. It is returning the first element (index = 0) that has a probability of 1/4.
Since this is a randomization problem, multiple answers are allowed.
All of the following outputs can be considered correct:
[null,1,1,1,1,0]
[null,1,1,1,1,1]
[null,1,1,1,0,0]
[null,1,1,1,0,1]
[null,1,0,1,0,0]
......
and so on.


Constraints:
1 <= w.length <= 10^4
1 <= w[i] <= 10^5
pickIndex will be called at most 10^4 times.
"""
import bisect
import random
from typing import List


class Solution:
    """
    前缀和 + 二分查找
    假设所有权重的累加和为total，则可将原问题转化为在[1, total]内随机选出一个整数a，返回整数a所在的区间下标i。
    使用各个权重将[1, total]划分为n个区间。例如：w = [3, 1, 2, 4]，则可将 [1, 10] 划分为以下4个区间：[[1, 3], [4, 4], [5, 6], [7, 10]]。
    查找区间下标i的过程，可转化为在前缀和数组上进行二分查找。w = [3, 1, 2, 4] 对应的前缀和数组pre_sum为：[0, 3, 4, 6, 10]
    在pre_sum中二分查找第一个大于等于整数a的元素下标，该下标减1即为结果
    """

    def __init__(self, w: List[int]):
        pre_sum = [0]
        for num in w:
            pre_sum.append(pre_sum[-1] + num)
        self.pre_sum = pre_sum
        self.total = pre_sum[-1]

    def pickIndex(self) -> int:
        a = random.randint(1, self.total)
        return bisect.bisect_left(self.pre_sum, a) - 1

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
