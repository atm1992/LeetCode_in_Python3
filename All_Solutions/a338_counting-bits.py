# -*- coding: UTF-8 -*-
"""
title: 比特位计数
Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.


Example 1:
Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10

Example 2:
Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101


Constraints:
0 <= n <= 10^5

Follow up:
It is very easy to come up with a solution with a runtime of O(n log n). Can you do it in linear time O(n) and possibly in a single pass?
Can you do it without using any built-in function (i.e., like __builtin_popcount in C++)?
"""
from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n + 1):
            tmp = 0
            while i:
                tmp += 1
                i &= i - 1
            res.append(tmp)
        return res

    def countBits_2(self, n: int) -> List[int]:
        """
        动态规划 —— 最高有效位。
        最高有效位 是指2的整数次幂，即 1、2、4、8、16、…… 这些数字都有个特征就是只有最高二进制位为1，其余位均为0
        介于 4 ~ 8 之间的5、6、7可看做是 4 + 1、4 + 2、4 + 3，即 1、2、3 的二进制表示再加上最高位的1，而1、2、3的二进制表示中1的个数在前面已经求出来了。
        若 y & (y-1) == 0，则表示y只有一位二进制位为1，也就意味着y是2的整数次幂
        """
        res = [0]
        high_bit = 0
        for i in range(1, n + 1):
            if i & (i - 1) == 0:
                high_bit = i
                res.append(1)
            else:
                res.append(res[i - high_bit] + 1)
        return res

    def countBits_3(self, n: int) -> List[int]:
        """
        动态规划 —— 最低有效位。
        若y为偶数，则 y的二进制表示中1的个数 等于 y>>1的二进制表示中1的个数 + 0
        若y为奇数，则 y的二进制表示中1的个数 等于 y>>1的二进制表示中1的个数 + 1
        可以统一写成 res[y >> 1] + (y & 1)
        """
        res = [0]
        for i in range(1, n + 1):
            # 注意运算符的优先级，i & 1 要放在 () 内
            res.append(res[i >> 1] + (i & 1))
        return res

    def countBits_4(self, n: int) -> List[int]:
        """
        动态规划 —— 最低设置位。
        假设 y = x & (x-1)，显然 0 <= y < x，x 比 y 多了一个最低位的1
        所以 res[x] = res[x & (x-1)] + 1
        """
        res = [0]
        for i in range(1, n + 1):
            res.append(res[i & (i - 1)] + 1)
        return res


if __name__ == '__main__':
    print(Solution().countBits_4(5))
