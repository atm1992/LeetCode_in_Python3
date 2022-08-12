# -*- coding: UTF-8 -*-
"""
title：验证回文串
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise. 

Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Example 3:
Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.

Constraints:
1 <= s.length <= 2 * 10^5
s consists only of printable ASCII characters.

解题思路：
首先，得到只保留大小写字母、数字的字符串；
然后，将大写字母转换为小写字母；
最后，判断字符串的逆序与原字符串是否相等。
只考虑大小写字母和数字，其余字符不考虑
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        tmp = ''.join(ch.lower() for ch in s if ch.isalnum())
        # 也可对tmp使用首尾双指针来判断是否为回文
        return tmp[::-1] == tmp

    def isPalindrome_2(self, s: str) -> bool:
        """在原字符串上直接判断，将空间复杂度从O(n)优化到O(1)"""
        left, right = 0, len(s) - 1
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if left < right:
                if s[left].lower() != s[right].lower():
                    return False
                left += 1
                right -= 1
        return True


if __name__ == '__main__':
    print(Solution().isPalindrome("A man, a plan, a canal: Panama"))
