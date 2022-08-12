# -*- coding: UTF-8 -*-
"""
title: 字符串解码
Given an encoded string, return its decoded string.
The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.
You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc.
Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].


Example 1:
Input: s = "3[a]2[bc]"
Output: "aaabcbc"

Example 2:
Input: s = "3[a2[c]]"
Output: "accaccacc"

Example 3:
Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"


Constraints:
1 <= s.length <= 30
s consists of lowercase English letters, digits, and square brackets '[]'.
s is guaranteed to be a valid input.
All the integers in s are in the range [1, 300].
"""


class Solution:
    def decodeString(self, s: str) -> str:
        """栈"""
        stack = []
        n = len(s)
        idx = 0
        while idx < n:
            ch = s[idx]
            if ch.isdigit():
                start_idx = idx
                idx += 1
                while s[idx].isdigit():
                    idx += 1
                stack.append(s[start_idx:idx])
            elif ch == ']':
                # word 初始时需要是空数组，而不能是空字符串。
                # 若用空字符串直接拼接，然后逆序，会有问题。例如：stack = ['[', 'dyf', 't', 'aa']，
                # 空字符串直接拼接后逆序的结果为：'aatdyf' ——> 'fydtaa'
                # 空数组append后逆序拼接的结果为：['aa', 't', 'dyf'] ——> ['dyf', 't', 'aa'] ——> 'dyftaa'
                word = []
                while stack[-1] != '[':
                    word.append(stack.pop())
                word = ''.join(word[::-1])
                # pop [
                stack.pop()
                # pop 数字
                stack.append(word * int(stack.pop()))
                idx += 1
            else:
                stack.append(ch)
                idx += 1
        return ''.join(stack)


if __name__ == '__main__':
    print(Solution().decodeString("3[z]2[2[y]pq4[2[jk]e1[f]]]ef"))
