# -*- coding: UTF-8 -*-
"""
title: 括号的分数
Given a balanced parentheses string s, return the score of the string.
The score of a balanced parentheses string is based on the following rule:
    "()" has score 1.
    AB has score A + B, where A and B are balanced parentheses strings.
    (A) has score 2 * A, where A is a balanced parentheses string.


Example 1:
Input: s = "()"
Output: 1

Example 2:
Input: s = "(())"
Output: 2

Example 3:
Input: s = "()()"
Output: 2


Constraints:
2 <= s.length <= 50
s consists of only '(' and ')'.
s is a balanced parentheses string.
"""


class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        """递归"""
        n = len(s)
        if n == 2:
            return 1
        balance = 0
        for i, ch in enumerate(s):
            balance += 1 if ch == '(' else -1
            if balance == 0:
                if i == n - 1:
                    return self.scoreOfParentheses(s[1:-1]) * 2
                else:
                    return self.scoreOfParentheses(s[:i + 1]) + self.scoreOfParentheses(s[i + 1:])

    def scoreOfParentheses_2(self, s: str) -> int:
        """
        栈
        将平衡字符串s看作是 空字符串 + s，空字符串的分数为0，最终结果就是 0 + 字符串s的分数，即 AB 形式
        之后每次遇到 (，就先压入一个0，可看做是前面有个空字符串；每次遇到 )，就把栈顶pop出来，进行计算，若栈顶元素为0，则表示当前字符的前一个字符就是对应的 (，此时的分数为1，即 ()；
        若栈顶元素不为0，则表示当前的 ) 和它对应的 ( 之间存在嵌套的括号，栈顶元素就是这段嵌套的括号的分数，此时的分数为 2 * 栈顶元素，即 (A) 形式。
        综合两种情况：当前的 ) 到它对应的 ( 这段子字符串的分数为 max(2 * 栈顶元素, 1)
        最后把这段子字符串的分数累加到前面的子字符串，即 AB 形式。最终stack中只会剩下一个元素，那就是最终结果
        """
        stack = [0]
        for ch in s:
            if ch == '(':
                stack.append(0)
            else:
                # 注意：不能写成 stack[-1] += max(2 * stack.pop(), 1)，因为这等价于 stack[-1] = stack[-1] + max(2 * stack.pop(), 1)，
                # 实际应该是 stack[-1] = stack[-2] + max(2 * stack.pop(), 1) 或写成 stack[-1] = max(2 * stack.pop(), 1) + stack[-1]
                score = max(2 * stack.pop(), 1)
                stack[-1] += score
        return stack[0]

    def scoreOfParentheses_3(self, s: str) -> int:
        """
        计算最终分数和
        ((())) 的最终分数其实取决于最内层 () 的深度balance，其分数为 2^balance，当 s[i]==')' and s[i-1]=='(' 时，就说明遍历到了最内层的()了，
        此时的 balance = 3 - 1 = 2，即 ((())) 的最终分数为 2^2 = 4
        同理，(())()((())) = 2 + 1 + 4 = 7。总之，只有在遇到()时，才会去累加计算最终分数，有几个()，就计算几次 2^balance
        """
        res = balance = 0
        for i, ch in enumerate(s):
            balance += 1 if ch == '(' else -1
            if ch == ')' and s[i - 1] == '(':
                res += 2 ** balance
        return res


if __name__ == '__main__':
    print(Solution().scoreOfParentheses_3(s="(())()((()))"))
