# -*- coding: UTF-8 -*-
"""
title: 循环码排列
Given 2 integers n and start. Your task is return any permutation p of (0,1,2.....,2^n -1) such that :
    p[0] = start
    p[i] and p[i+1] differ by only one bit in their binary representation.
    p[0] and p[2^n -1] must also differ by only one bit in their binary representation.


Example 1:
Input: n = 2, start = 3
Output: [3,2,0,1]
Explanation: The binary representation of the permutation is (11,10,00,01).
All the adjacent element differ by one bit. Another valid permutation is [3,1,0,2]

Example 2:
Input: n = 3, start = 2
Output: [2,6,7,5,4,0,1,3]
Explanation: The binary representation of the permutation is (010,110,111,101,100,000,001,011).


Constraints:
1 <= n <= 16
0 <= start < 2^n
"""
from typing import List


class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        """直接使用LeetCode题89的结果，然后截取头部若干个元素拼接到尾部"""
        res = [0]
        for i in range(n):
            for j in range(len(res) - 1, -1, -1):
                res.append(res[j] | (1 << i))
        idx = res.index(start)
        return res[idx:] + res[:idx]

    def circularPermutation_2(self, n: int, start: int) -> List[int]:
        """
        使用镜像反射法求解格雷编码。参考LeetCode题89
        本题与题89的区别在于：题89要求第一个整数是 0，而本题要求第一个整数是 start。因此只需将求出的每一项结果都与start进行异或即可。
        """
        res = [start]
        for i in range(n):
            for j in range(len(res) - 1, -1, -1):
                # res[j] ^ start 将元素变成从0开始，最后再 ^ start 消除之前 ^ start的影响，变回从start开始
                res.append(((res[j] ^ start) | (1 << i)) ^ start)
        return res

    def circularPermutation_3(self, n: int, start: int) -> List[int]:
        """使用公式法求解格雷编码。参考LeetCode题89"""
        return [i ^ (i >> 1) ^ start for i in range(1 << n)]


if __name__ == '__main__':
    print(Solution().circularPermutation_2(n=2, start=3))
