# -*- coding: UTF-8 -*-
"""
title：接雨水。
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
例如：输入数组 [0,1,0,2,1,0,1,3,2,1,2,1]，输出 6

解题思路：
方法一：暴力法（Python超时，其它语言可以）
对于数组中的每个元素，只考虑该柱子上方是否可以盛水，能盛多少水
柱子上能盛多少水，取决于该柱子左右两侧最近的最大值
时间复杂度O(N^2)，空间复杂度为O(1)

方法二：动态规划
在方法一中存在大量的重复计算，对于每个柱子都需要遍历一次左右两侧的最高柱子。
可以使用两个数组maxleft、maxright来分别存储左右两侧的最高柱子，maxleft[i]表示下标为i柱子左侧的最高柱子。
这样就只需遍历一次便可得到结果，遍历重复计算
时间复杂度O(N)，空间复杂度为O(N)

方法三：双指针法
使用left,right两个指针逐步向中间移动，使用maxleft、maxright这两个变量来存储当前的左右两侧最大值
若maxleft小于maxright，则left移动一步；否则right移动一步，直到left小于right
时间复杂度O(N)，空间复杂度为O(1)
"""
from typing import List


class Solution_1:
    """暴力法。此方案Python运行超时"""

    def trap(self, height: List[int]) -> int:
        if not height or len(height) < 3:
            return 0
        res = 0
        for i in range(len(height)):
            max_left, max_right = 0, 0
            for l in range(i):
                max_left = max(max_left, height[l])
            for r in range(i + 1, len(height)):
                max_right = max(max_right, height[r])
            if min(max_left, max_right) > height[i]:
                res += min(max_left, max_right) - height[i]
        return res


class Solution_2:
    """动态规划"""

    def trap(self, height: List[int]) -> int:
        if not height or len(height) < 3:
            return 0
        n = len(height)
        # 千万不能写成maxleft = maxright = [0] * n，否则修改maxright的时候也会修改maxleft
        # 引用传递，maxleft、maxright指向的是同一个数组
        maxleft, maxright = [0] * n, [0] * n
        res = 0
        # 初始化
        maxleft[0] = 0
        maxright[n - 1] = 0
        for l in range(1, n):
            maxleft[l] = max(height[l - 1], maxleft[l - 1])
        for r in range(n - 2, -1, -1):
            maxright[r] = max(height[r + 1], maxright[r + 1])
        # 第一个柱子以及最后一个柱子上面肯定是没有水的
        for i in range(1, n - 1):
            if min(maxleft[i], maxright[i]) > height[i]:
                res += min(maxleft[i], maxright[i]) - height[i]
        return res


class Solution_3:
    """双指针法"""

    def trap(self, height: List[int]) -> int:
        if not height or len(height) < 3:
            return 0
        n = len(height)
        maxleft, maxright = height[0], height[n - 1]
        left, right = 1, n - 2
        res = 0
        while left <= right:
            # 更新maxleft, maxright
            # 确保此时的maxleft一定大于等于height[left]，从而确保maxleft-height[left]大于等于0
            maxleft = max(height[left], maxleft)
            maxright = max(height[right], maxright)
            # 能否盛水，盛多少水，取决于短板（矮的那个）
            if maxleft < maxright:
                # res每次累加的都是当前柱子上能接多少雨水，所以当left = right时，累加的是left和right最后共同指向的那根柱子
                res += maxleft - height[left]
                left += 1
            else:
                res += maxright - height[right]
                right -= 1
        return res
