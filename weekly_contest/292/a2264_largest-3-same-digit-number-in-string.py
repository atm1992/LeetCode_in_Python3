# -*- coding: UTF-8 -*-
"""
title: 字符串中最大的 3 位相同数字
You are given a string num representing a large integer. An integer is good if it meets the following conditions:
    It is a substring of num with length 3.
    It consists of only one unique digit.
Return the maximum good integer as a string or an empty string "" if no such integer exists.
Note:
    A substring is a contiguous sequence of characters within a string.
    There may be leading zeroes in num or a good integer.


Example 1:
Input: num = "6777133339"
Output: "777"
Explanation: There are two distinct good integers: "777" and "333".
"777" is the largest, so we return "777".

Example 2:
Input: num = "2300019"
Output: "000"
Explanation: "000" is the only good integer.

Example 3:
Input: num = "42352338"
Output: ""
Explanation: No substring of length 3 consists of only one unique digit. Therefore, there are no good integers.


Constraints:
3 <= num.length <= 1000
num only consists of digits.
"""


class Solution:
    def largestGoodInteger(self, num: str) -> str:
        cnt = 1
        res = ""
        last_ch = num[0]
        for i in range(1, len(num)):
            if num[i] != last_ch:
                last_ch = num[i]
                cnt = 1
            else:
                cnt += 1
            if cnt == 3:
                if last_ch > res:
                    res = last_ch
        return res * 3 if res else ''

    def largestGoodInteger_2(self, num: str) -> str:
        """模拟"""
        for i in range(9, -1, -1):
            t = str(i) * 3
            if t in num:
                return t
        return ''


if __name__ == '__main__':
    print(Solution().largestGoodInteger("42352338"))
