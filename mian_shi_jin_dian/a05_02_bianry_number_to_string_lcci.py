# -*- coding: UTF-8 -*-
"""
title: 二进制数转字符串
Given a real number between 0 and 1 (e.g., 0.72) that is passed in as a double, print the binary representation. If the number cannot be represented accurately in binary with at most 32 characters, print "ERROR".


Example1:
 Input: 0.625
 Output: "0.101"

Example2:
 Input: 0.1
 Output: "ERROR"
 Note: 0.1 cannot be represented accurately in binary.


Note:
This two charaters "0." should be counted into 32 characters.
The number of decimal places for num is at most 6 digits
"""


class Solution:
    def printBin(self, num: float) -> str:
        """
        十进制整数转换为二进制整数 —— "除2取余，逆序排列"。具体做法是：用2去除十进制整数，可以得到一个商和余数；
        再用2去除商，又会得到一个商和余数，如此进行，直到商为零，然后把先得到的余数作为二进制数的低位有效位，
        后得到的余数作为二进制数的高位有效位，依次排列起来。

        十进制小数转换为二进制小数 —— "乘2取整，顺序排列"。具体做法是：用2去乘十进制小数，可以得到积，将积的整数部分取出，
        再用2去乘余下的小数部分，又得到一个积，再将积的整数部分取出，如此进行，直到积中的小数部分为零，或达到所要求的精度为止。
        然后把取出的整数部分按顺序排列起来，先取的整数作为二进制小数的高位有效位，后取的整数作为低位有效位。
        """
        res = ['0', '.']
        while num != 0 and len(res) <= 32:
            num *= 2
            if num < 1:
                res.append('0')
            else:
                res.append('1')
                num -= 1
        return 'ERROR' if num != 0 else ''.join(res)


if __name__ == '__main__':
    print(Solution().printBin(0.1))
