# -*- coding: UTF-8 -*-
"""
title: 和为s的连续正数序列
输入一个正整数 target ，输出所有和为 target 的连续正整数序列（至少含有两个数）。
序列内的数字由小到大排列，不同序列按照首个数字从小到大排列。


示例 1：
输入：target = 9
输出：[[2,3,4],[4,5]]

示例 2：
输入：target = 15
输出：[[1,2,3,4,5],[4,5,6],[7,8]]


限制：
1 <= target <= 10^5
"""
from typing import List


class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        """双指针"""
        res = []
        left, right = 1, 2
        while left < right:
            # 等差数列求和公式。若不知道此公式，也可用滑动窗口
            total = (left + right) * (right - left + 1) // 2
            if total == target:
                res.append(list(range(left, right + 1)))
                left += 1
            elif total < target:
                right += 1
            else:
                left += 1
        return res


if __name__ == '__main__':
    print(Solution().findContinuousSequence(15))
