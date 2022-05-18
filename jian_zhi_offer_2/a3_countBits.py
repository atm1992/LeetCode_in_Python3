# -*- coding: UTF-8 -*-
"""
title: 前 n 个数字二进制中 1 的个数
给定一个非负整数 n ，请计算 0 到 n 之间的每个数字的二进制表示中 1 的个数，并输出一个数组。


示例 1:
输入: n = 2
输出: [0,1,1]
解释:
0 --> 0
1 --> 1
2 --> 10

示例 2:
输入: n = 5
输出: [0,1,1,2,1,2]
解释:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101


说明 :
0 <= n <= 10^5

进阶:
给出时间复杂度为 O(n*sizeof(integer)) 的解答非常容易。但你可以在线性时间 O(n) 内用一趟扫描做到吗？
要求算法的空间复杂度为 O(n) 。
你能进一步完善解法吗？要求在C++或任何其他语言中不使用任何内置函数（如 C++ 中的 __builtin_popcount ）来执行此操作。
"""
from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n + 1):
            cnt = 0
            while i:
                cnt += 1
                i &= i - 1
            res.append(cnt)
        return res

    def countBits_2(self, n: int) -> List[int]:
        """
        动态规划 - 最高有效位
        最高有效位是指二进制表示中的最高位1。例如：13 = 1101, 5 = 101，13二进制中1的个数等于13-8=5二进制中1的个数 加1
        通过1、2、4、8、16、…… 对所有数字进行分段，例如：4 ~ 8 之间的5、6、7可转换为1、2、3，然后加上4
        """
        res = [0]
        high_bit = 0
        for i in range(1, n + 1):
            # 二进制表示中只有一位1
            if i & (i - 1) == 0:
                high_bit = i
                res.append(1)
            else:
                res.append(res[i - high_bit] + 1)
        return res

    def countBits_3(self, n: int) -> List[int]:
        """
        动态规划 - 最低有效位
        若y为偶数，则y二进制中1的个数等于y>>1二进制中1的个数 + 0；
        若y为奇数，则y二进制中1的个数等于y>>1二进制中1的个数 + 1；
        后面的 +0、+1 可写成 y & 1
        """
        res = [0]
        for i in range(1, n + 1):
            # 注意运算符之间的优先级，不能写成 res[i >> 1] + i & 1
            res.append(res[i >> 1] + (i & 1))
        return res

    def countBits_4(self, n: int) -> List[int]:
        """
        动态规划 - 最低设置位
        y二进制中1的个数等于y&(y-1)二进制中1的个数 + 1
        """
        res = [0]
        for i in range(1, n + 1):
            res.append(res[i & (i - 1)] + 1)
        return res


if __name__ == '__main__':
    print(Solution().countBits_4(5))
