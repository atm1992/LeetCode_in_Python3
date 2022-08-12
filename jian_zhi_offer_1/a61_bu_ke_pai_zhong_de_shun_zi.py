# -*- coding: UTF-8 -*-
"""
title: 扑克牌中的顺子
从若干副扑克牌中随机抽 5 张牌，判断是不是一个顺子，即这5张牌是不是连续的。2～10为数字本身，A为1，J为11，Q为12，K为13，而大、小王为 0，可以看成任意数字。A 不能视为 14。


示例 1:
输入: [1,2,3,4,5]
输出: True

示例 2:
输入: [0,0,1,2,5]
输出: True


限制：
数组长度为 5 
数组的数取值为 [0, 13] .
"""
from typing import List


class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        nums.sort()
        cnt_0 = cnt_gap = 0
        for i in range(5):
            if nums[i] == 0:
                cnt_0 += 1
            elif i > 0 and nums[i - 1] > 0:
                # 除了大小王以外，不能存在重复
                if nums[i] == nums[i - 1]:
                    return False
                cnt_gap += nums[i] - nums[i - 1] - 1
        return cnt_0 >= cnt_gap


if __name__ == '__main__':
    print(Solution().isStraight([0, 0, 1, 2, 5]))
