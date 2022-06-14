# -*- coding: UTF-8 -*-
"""
title: 按权重生成随机数
给定一个正整数数组 w ，其中 w[i] 代表下标 i 的权重（下标从 0 开始），请写一个函数 pickIndex ，它可以随机地获取下标 i，选取下标 i 的概率与 w[i] 成正比。
例如，对于 w = [1, 3]，挑选下标 0 的概率为 1 / (1 + 3) = 0.25 （即，25%），而选取下标 1 的概率为 3 / (1 + 3) = 0.75（即，75%）。
也就是说，选取下标 i 的概率为 w[i] / sum(w) 。


示例 1：
输入：
inputs = ["Solution","pickIndex"]
inputs = [[[1]],[]]
输出：
[null,0]
解释：
Solution solution = new Solution([1]);
solution.pickIndex(); // 返回 0，因为数组中只有一个元素，所以唯一的选择是返回下标 0。

示例 2：
输入：
inputs = ["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
inputs = [[[1,3]],[],[],[],[],[]]
输出：
[null,1,1,1,1,0]
解释：
Solution solution = new Solution([1, 3]);
solution.pickIndex(); // 返回 1，返回下标 1，返回该下标概率为 3/4 。
solution.pickIndex(); // 返回 1
solution.pickIndex(); // 返回 1
solution.pickIndex(); // 返回 1
solution.pickIndex(); // 返回 0，返回下标 0，返回该下标概率为 1/4 。
由于这是一个随机问题，允许多个答案，因此下列输出都可以被认为是正确的:
[null,1,1,1,1,0]
[null,1,1,1,1,1]
[null,1,1,1,0,0]
[null,1,1,1,0,1]
[null,1,0,1,0,0]
......
诸若此类。


提示：
1 <= w.length <= 10000
1 <= w[i] <= 10^5
pickIndex 将被调用不超过 10000 次
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
