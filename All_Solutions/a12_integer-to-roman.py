# -*- coding: UTF-8 -*-
"""
title: 整数转罗马数字
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.
Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX.
There are six instances where subtraction is used:
I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given an integer, convert it to a roman numeral.


Example 1:
Input: num = 3
Output: "III"

Example 2:
Input: num = 4
Output: "IV"

Example 3:
Input: num = 9
Output: "IX"

Example 4:
Input: num = 58
Output: "LVIII"
Explanation: L = 50, V = 5, III = 3.

Example 5:
Input: num = 1994
Output: "MCMXCIV"
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.


Constraints:
1 <= num <= 3999
"""


class Solution:
    def intToRoman(self, num: int) -> str:
        """模拟罗马数字的唯一表示法"""
        mappings = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
                    (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
        res = []
        for value, symbol in mappings:
            while num >= value:
                num -= value
                res.append(symbol)
            if num == 0:
                break
        return ''.join(res)

    def intToRoman_2(self, num: int) -> str:
        """硬编码数字。千位数字只能由 M 表示；百位数字只能由 C、CD、D、CM 表示；十位数字只能由 X、XL、L、XC 表示；个位数字只能由 I、IV、V、IX 表示。"""
        # 因为 num <= 3999，所以千位数字只需编码到3即可。若某一位置上的数字为0，则用空字符串表示
        THOUSANDS = ['', 'M', 'MM', 'MMM']
        HUNDREDS = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
        TENS = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
        ONES = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']

        thousands_digit = num // 1000
        hundreds_digit = num % 1000 // 100
        tens_digit = num % 100 // 10
        ones_digit = num % 10
        return ''.join([THOUSANDS[thousands_digit], HUNDREDS[hundreds_digit], TENS[tens_digit], ONES[ones_digit]])


if __name__ == '__main__':
    print(Solution().intToRoman_2(3999))
