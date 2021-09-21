# -*- coding: UTF-8 -*-
"""
title: 最长有效括号
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.


Example 1:
Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".

Example 2:
Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".

Example 3:
Input: s = ""
Output: 0


Constraints:
0 <= s.length <= 3 * 10^4
s[i] is '(', or ')'.
"""


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        """动态规划。时间复杂度O(n)，空间复杂度为O(n)"""
        res = 0
        n = len(s)
        # dp[i] 表示以元素i结尾的有效括号长度。若i==0或元素i为(，则dp[i]一定为0。因此，只需考虑元素i为)时的情况：分为 元素i-1为) 和 元素i-1为( 。
        # 一、元素i-1为(，dp[i] = dp[i-2] + 2 。
        # 二、元素i-1为)，则需要元素i-dp[i-1]-1为(才能与元素i的)相配，所以，当元素i-dp[i-1]-1为(时，dp[i] = dp[i-1] + 2 + dp[i-dp[i-1]-2]；当元素i-dp[i-1]-1为)时，dp[i] = 0 。
        dp = [0] * n
        # [0]*0 = []，可以兼容n=0、1时的情况
        for i in range(1, n):
            if s[i] == ')':
                if s[i - 1] == '(':
                    dp[i] = dp[i - 2] + 2 if i - 2 >= 0 else 2
                elif i - dp[i - 1] - 1 >= 0 and s[i - dp[i - 1] - 1] == '(':
                    dp[i] = dp[i - 1] + 2 + dp[i - dp[i - 1] - 2] if i - dp[i - 1] - 2 >= 0 else dp[i - 1] + 2
                res = max(res, dp[i])
        return res

    def longestValidParentheses_2(self, s: str) -> int:
        """栈。时间复杂度O(n)，空间复杂度为O(n)
        设计一个栈，栈底元素始终为最后一个未匹配的)的下标，初始栈底元素为-1，可以兼容s中的第一个元素为(的情况，例如：()) ，i=1时，有效括号的长度为 1 - (-1)= 2 。
        从前往后遍历，遇到(，元素下标入栈；遇到)，栈顶元素出栈。然后再获取当前栈顶元素的下标(并不出栈)，将当前元素)的下标减去栈顶元素的下标，即为有效括号的长度。
        若获取当前栈顶元素的下标时，发现当前栈为空，则表示刚才出栈的栈顶元素为最后一个未匹配的)，也就意味着当前元素)并不存在匹配的(，因此把当前元素)入栈，
        作为新的最后一个未匹配的)。
        """
        res = 0
        stack = [-1]
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                # 这里之所以可以直接将栈顶元素出栈，是因为栈底元素始终为最后一个未匹配的)的下标 或 -1
                stack.pop()
                # 说明刚才将 最后一个未匹配的)的下标 或 -1 pop出去了，所以要将当前元素)的下标放到栈底
                if not stack:
                    stack.append(i)
                else:
                    res = max(res, i - stack[-1])
        return res

    def longestValidParentheses_3(self, s: str) -> int:
        """不使用额外空间。时间复杂度O(n)，空间复杂度为O(1)
        先从前往后遍历，使用两个变量left、right分别统计左括号、右括号的个数。若right>left，则表示以right结尾的字符串不是有效括号，left、right清零；若right=left，则表示以right结尾的字符串是有效括号。
        不过，上述算法无法处理类似与 (() 这种左括号数始终大于右括号数的情况。因此，还需从后往前再遍历一次，依旧使用两个变量left、right分别统计左括号、右括号的个数，
        若left>right，则表示以left起始到s结尾的字符串不是有效括号，left、right清零；若left=right，则表示以left起始到s结尾的字符串是有效括号。
        """
        res = 0
        left = right = 0
        n = len(s)
        for i in range(n):
            if s[i] == '(':
                left += 1
            else:
                right += 1
            if right > left:
                left = right = 0
            elif right == left:
                res = max(res, 2 * right)

        left = right = 0
        for i in range(n - 1, -1, -1):
            if s[i] == '(':
                left += 1
            else:
                right += 1
            if left > right:
                left = right = 0
            elif left == right:
                res = max(res, 2 * left)
        return res
