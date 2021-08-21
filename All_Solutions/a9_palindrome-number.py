# -*- coding: UTF-8 -*-
"""
title: 回文数。
Given an integer x, return true if x is palindrome integer.
An integer is a palindrome when it reads the same backward as forward. For example, 121 is palindrome while 123 is not.


Example 1:
Input: x = 121
Output: true

Example 2:
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

Example 4:
Input: x = -101
Output: false


Constraints:
-2^31 <= x <= 2^31 - 1

Follow up: Could you solve it without converting the integer to a string?
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_str = str(x)
        left, right = 0, len(x_str) - 1
        while left < right:
            if x_str[left] != x_str[right]:
                return False
            left += 1
            right -= 1
        return True

    def isPalindrome_2(self, x: int) -> bool:
        """不转成字符串，直接对数字进行处理。逐位反转后一半，每次都判断原始的前半部分与反转后的后半部分之间的大小关系"""
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        reverse_part = 0
        while x > reverse_part:
            reverse_part = reverse_part * 10 + x % 10
            x //= 10
        # x < reverse_part 时，不一定就不是回文数。例如：12321、3
        return x == reverse_part or x == reverse_part // 10
