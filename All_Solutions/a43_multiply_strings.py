# -*- coding: UTF-8 -*-
"""
title: 字符串相乘
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.
Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.


Example 1:
Input: num1 = "2", num2 = "3"
Output: "6"

Example 2:
Input: num1 = "123", num2 = "456"
Output: "56088"


Constraints:
1 <= num1.length, num2.length <= 200
num1 and num2 consist of digits only.
Both num1 and num2 do not contain any leading zero, except the number 0 itself.
"""


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        """模拟竖式乘法。从右往左遍历乘数num2，将乘数num2的每一位与被乘数num1相乘得到相应的结果，然后再将每次得到的结果累加。
        注意：乘数num2除了最低位以外，其余每一位的运算结果都需要后面补0"""
        res = '0'
        if num1 == '0' or num2 == '0':
            return res
        n1, n2 = len(num1), len(num2)
        for i in range(n2 - 1, -1, -1):
            carry = 0
            y = ord(num2[i]) - ord('0')
            # 需要补0的个数。逆序后就是此次计算的结果
            tmp = ['0'] * (n2 - 1 - i)
            for j in range(n1 - 1, -1, -1):
                product = (ord(num1[j]) - ord('0')) * y + carry
                tmp.append(str(product % 10))
                carry = product // 10
            if carry > 0:
                tmp.append(str(carry))
            res = self.addStrings(res, ''.join(tmp[::-1]))
        return res

    def addStrings(self, num1: str, num2: str) -> str:
        """字符串相加"""
        i, j = len(num1) - 1, len(num2) - 1
        carry = 0
        res = []
        while i >= 0 or j >= 0 or carry > 0:
            x = ord(num1[i]) - ord('0') if i >= 0 else 0
            y = ord(num2[j]) - ord('0') if j >= 0 else 0
            tmp = x + y + carry
            res.append(str(tmp % 10))
            carry = tmp // 10
            i -= 1
            j -= 1
        return ''.join(res[::-1])

    def multiply_2(self, num1: str, num2: str) -> str:
        """优化版竖式乘法。上个方法中，涉及到较多的字符串相加操作，这个操作比较耗时。使用数组来代替字符串存储结果，从而减少对字符串的操作。
        令m和n分别表示num1和num2的长度，并且num1和num2均不为0，则num1和num2的乘积的长度为 m+n−1 或 m+n。
        创建长度为 m+n 的数组 res_arr 用于存储乘积。对于任意的 0≤i<m 和 0≤j<n，num1[i]×num2[j] 的结果位于 res_arr[i+j+1]，
        若 res_arr[i+j+1]≥10，则将进位部分加到 res_arr[i+j]。"""
        if num1 == '0' or num2 == '0':
            return '0'
        m, n = len(num1), len(num2)
        res_arr = [0] * (m + n)
        for i in range(m - 1, -1, -1):
            x = ord(num1[i]) - ord('0')
            for j in range(n - 1, -1, -1):
                res_arr[i + j + 1] += x * (ord(num2[j]) - ord('0'))
        for i in range(m + n - 1, 0, -1):
            res_arr[i - 1] += res_arr[i] // 10
            res_arr[i] %= 10
        start_idx = 1 if res_arr[0] == 0 else 0
        return ''.join(map(str, res_arr[start_idx:]))


if __name__ == '__main__':
    print(Solution().multiply_2(num1="123", num2="456"))
