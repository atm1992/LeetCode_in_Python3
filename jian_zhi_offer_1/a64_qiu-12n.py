# -*- coding: UTF-8 -*-
"""
title: 求1+2+…+n
求 1+2+...+n ，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。


示例 1：
输入: n = 3
输出: 6

示例 2：
输入: n = 9
输出: 45


限制：
1 <= n <= 10000
"""


class Solution:
    def sumNums(self, n: int) -> int:
        return sum(range(n + 1))

    def sumNums_2(self, n: int) -> int:
        """递归。此方法效率最低"""
        _sum = [0, 1]
        try:
            return _sum[n]
        except IndexError:
            return n + self.sumNums_2(n - 1)

    def __init__(self):
        self.res = 0

    def sumNums_3(self, n: int) -> int:
        """递归。建议此方法"""
        # 利用逻辑运算符的短路性质。先一路递归到n==0，然后向上返回时，不断 res += n
        n and self.sumNums_3(n - 1)
        self.res += n
        return self.res


if __name__ == '__main__':
    print(Solution().sumNums(9))
