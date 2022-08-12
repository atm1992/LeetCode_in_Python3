# -*- coding: UTF-8 -*-
"""
title: 判断一个数的数字计数是否等于数位的值
You are given a 0-indexed string num of length n consisting of digits.
Return true if for every index i in the range 0 <= i < n, the digit i occurs num[i] times in num, otherwise return false.


Example 1:
Input: num = "1210"
Output: true
Explanation:
num[0] = '1'. The digit 0 occurs once in num.
num[1] = '2'. The digit 1 occurs twice in num.
num[2] = '1'. The digit 2 occurs once in num.
num[3] = '0'. The digit 3 occurs zero times in num.
The condition holds true for every index in "1210", so return true.

Example 2:
Input: num = "030"
Output: false
Explanation:
num[0] = '0'. The digit 0 should occur zero times, but actually occurs twice in num.
num[1] = '3'. The digit 1 should occur three times, but actually occurs zero times in num.
num[2] = '0'. The digit 2 occurs zero times in num.
The indices 0 and 1 both violate the condition, so return false.


Constraints:
n == num.length
1 <= n <= 10
num consists of digits.
"""
from collections import defaultdict


class Solution:
    def digitCount(self, num: str) -> bool:
        num2cnt = defaultdict(int)
        for ch in num:
            num2cnt[int(ch)] += 1
        for i in range(len(num)):
            if int(num[i]) != num2cnt[i]:
                return False
        return True


if __name__ == '__main__':
    print(Solution().digitCount('030'))
