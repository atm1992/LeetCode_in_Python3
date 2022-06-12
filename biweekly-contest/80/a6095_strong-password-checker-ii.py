# -*- coding: UTF-8 -*-
"""
title: 强密码检验器 II
A password is said to be strong if it satisfies all the following criteria:
    It has at least 8 characters.
    It contains at least one lowercase letter.
    It contains at least one uppercase letter.
    It contains at least one digit.
    It contains at least one special character. The special characters are the characters in the following string: "!@#$%^&*()-+".
    It does not contain 2 of the same character in adjacent positions (i.e., "aab" violates this condition, but "aba" does not).
Given a string password, return true if it is a strong password. Otherwise, return false.


Example 1:
Input: password = "IloveLe3tcode!"
Output: true
Explanation: The password meets all the requirements. Therefore, we return true.

Example 2:
Input: password = "Me+You--IsMyDream"
Output: false
Explanation: The password does not contain a digit and also contains 2 of the same character in adjacent positions. Therefore, we return false.

Example 3:
Input: password = "1aB!"
Output: false
Explanation: The password does not meet the length requirement. Therefore, we return false.


Constraints:
1 <= password.length <= 100
password consists of letters, digits, and special characters: "!@#$%^&*()-+".
"""


class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        if len(password) < 8:
            return False
        mask = 0
        for idx, ch in enumerate(password):
            if idx > 0 and ch == password[idx - 1]:
                return False
            if ch.isdigit():
                mask |= 1
            elif ch.islower():
                mask |= 2
            elif ch.isupper():
                mask |= 4
            else:
                mask |= 8
        return mask == 15


if __name__ == '__main__':
    print(Solution().strongPasswordCheckerII(password="1aB!"))
