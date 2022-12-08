# -*- coding: UTF-8 -*-
"""
title: 移掉 K 位数字
Given string num representing a non-negative integer num, and an integer k, return the smallest possible integer after removing k digits from num.


Example 1:
Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.

Example 2:
Input: num = "10200", k = 1
Output: "200"
Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.

Example 3:
Input: num = "10", k = 2
Output: "0"
Explanation: Remove all the digits from the number and it is left with nothing which is 0.


Constraints:
1 <= k <= num.length <= 10^5
num consists of only digits.
num does not have any leading zeros except for the zero itself.
"""


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        """
        贪心 + 单调栈
        要想使剩余的数字尽可能小，则需保证靠前的数字尽可能小。
        从左往右遍历num字符串，若只能删除一位数字，则找到第一个满足条件 num[i] < num[i-1] 的下标i，然后删除num[i-1]。
        若整个num字符串已符合单调递增，则从右侧逐个删除。
        暴力的做法需要遍历num字符串k次，可使用单调栈来进一步优化，只需遍历一次num字符串
        """
        stack = []
        for d in num:
            while k > 0 and stack and stack[-1] > d:
                stack.pop()
                k -= 1
            # 忽略前导0
            if not stack and d == '0':
                continue
            stack.append(d)
        # 因为前面忽略了前导0，所以在这里当k > 0时，有可能stack已经为空了
        while k > 0 and stack:
            stack.pop()
            k -= 1
        return ''.join(stack) if stack else '0'


if __name__ == '__main__':
    print(Solution().removeKdigits(num="10", k=2))
