# -*- coding: utf-8 -*-
# @date: 2023/5/10
# @author: liuquan
"""
title: 可被 K 整除的最小整数
Given a positive integer k, you need to find the length of the smallest positive integer n such that n is divisible by k, and n only contains the digit 1.
Return the length of n. If there is no such n, return -1.
Note: n may not fit in a 64-bit signed integer.


Example 1:
Input: k = 1
Output: 1
Explanation: The smallest answer is n = 1, which has length 1.

Example 2:
Input: k = 2
Output: -1
Explanation: There is no such positive integer n divisible by 2.

Example 3:
Input: k = 3
Output: 3
Explanation: The smallest answer is n = 111, which has length 3.


Constraints:
1 <= k <= 10^5
"""


class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        """
        遍历
        由于n只由1组成，即个位数必须为1，因此当k为偶数时，n必然不存在。剩余的奇数(1、3、5、7、9)中，5乘以任何整数都不可能使得乘积的个位数为1，
        因此当k为2或5的倍数时，直接返回 -1
        假设现有cur_n = pre_n * 10 + 1，其中 pre_n >= 1，题目要求使得 n % k == 0
        则 cur_n % k = (pre_n * 10 + 1) % k = ((pre_n % k) * 10 + 1) % k，即 cur_remain = (pre_main * 10 + 1) % k
        所有余数必然都会小于k，可以从余数 1 % k 开始遍历，记录每次的余数，若出现了重复，则表示进入了循环，说明不存在满足题目要求的n
        """
        if k % 2 == 0 or k % 5 == 0:
            return -1
        remains = set()
        # 初始余数为1 % k，由于cur_remain必然小于k，所以cur_remain不会超出64位整数
        cur_remain = 1 % k
        while cur_remain > 0 and cur_remain not in remains:
            remains.add(cur_remain)
            cur_remain = (cur_remain * 10 + 1) % k
        return -1 if cur_remain > 0 else len(remains) + 1


if __name__ == '__main__':
    print(Solution().smallestRepunitDivByK(3))
