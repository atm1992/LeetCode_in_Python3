# -*- coding: UTF-8 -*-
"""
title: 分割两个字符串得到回文串
You are given two strings a and b of the same length. Choose an index and split both strings at the same index, splitting a into two strings: aprefix and asuffix where a = aprefix + asuffix, and splitting b into two strings: bprefix and bsuffix where b = bprefix + bsuffix. Check if aprefix + bsuffix or bprefix + asuffix forms a palindrome.
When you split a string s into sprefix and ssuffix, either ssuffix or sprefix is allowed to be empty. For example, if s = "abc", then "" + "abc", "a" + "bc", "ab" + "c" , and "abc" + "" are valid splits.
Return true if it is possible to form a palindrome string, otherwise return false.
Notice that x + y denotes the concatenation of strings x and y.


Example 1:
Input: a = "x", b = "y"
Output: true
Explaination: If either a or b are palindromes the answer is true since you can split in the following way:
aprefix = "", asuffix = "x"
bprefix = "", bsuffix = "y"
Then, aprefix + bsuffix = "" + "y" = "y", which is a palindrome.

Example 2:
Input: a = "xbdef", b = "xecab"
Output: false

Example 3:
Input: a = "ulacfd", b = "jizalu"
Output: true
Explaination: Split them at index 3:
aprefix = "ula", asuffix = "cfd"
bprefix = "jiz", bsuffix = "alu"
Then, aprefix + bsuffix = "ula" + "alu" = "ulaalu", which is a palindrome.


Constraints:
1 <= a.length, b.length <= 10^5
a.length == b.length
a and b consist of lowercase English letters
"""


class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        """双指针"""

        def is_palindrome(s: str, i: int, j: int) -> bool:
            # 避免切片产生的额外空间
            while i < j and s[i] == s[j]:
                i += 1
                j -= 1
            return i >= j

        def check(a: str, b: str) -> bool:
            left, right = 0, len(a) - 1
            while left < right and a[left] == b[right]:
                left += 1
                right -= 1
            if left >= right:
                return True
            # 判断中间剩余部分是否为回文串
            return is_palindrome(a, left, right) or is_palindrome(b, left, right)

        return check(a, b) or check(b, a)


if __name__ == '__main__':
    print(Solution().checkPalindromeFormation(a="ulacfd", b="jizalu"))
