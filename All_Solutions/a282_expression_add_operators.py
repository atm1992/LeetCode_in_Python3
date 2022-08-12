# -*- coding: UTF-8 -*-
"""
title: 给表达式添加运算符
Given a string num that contains only digits and an integer target, return all possibilities to insert the binary operators '+', '-', '*' between the digits of num so that the resultant expression evaluates to the target value.
Note that operands in the returned expressions should not contain leading zeros.


Example 1:
Input: num = "123", target = 6
Output: ["1*2*3","1+2+3"]
Explanation: Both "1*2*3" and "1+2+3" evaluate to 6.

Example 2:
Input: num = "232", target = 8
Output: ["2*3+2","2+3*2"]
Explanation: Both "2*3+2" and "2+3*2" evaluate to 8.

Example 3:
Input: num = "3456237490", target = 9191
Output: []
Explanation: There are no expressions that can be created from "3456237490" to evaluate to 9191.


Constraints:
1 <= num.length <= 10
num consists of only digits.
-2^31 <= target <= 2^31 - 1
"""
from typing import List


class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        """回溯"""
        n = len(num)
        res = []

        def backtrack(expression: List[str], idx: int, total: int, last_num: int) -> None:
            """
            expression 是由一个个字符组成的结果数组，idx 表示当前指向num的哪个下标。total 表示当前的计算结果，用于和target进行比较。
            last_num 表示当前最后一个算入total的数，记录它的原因是 如果下一个符号是 * ，则需先把它从total减去，然后乘以下一个数，再算入total。
            """
            if idx == n:
                if total == target:
                    res.append(''.join(expression))
                return
            # 记录当前符号的idx
            sign_idx = len(expression)
            if idx > 0:
                # 给待添加的符号占位，该符号的下标就是sign_idx，第一个数字前面不能有符号
                expression.append('')
            val = 0
            for j in range(idx, n):
                # 若idx位为0，则val只能等于0，后面不能再拼接其它字符
                if j > idx and num[idx] == '0':
                    break
                ch = num[j]
                val = val * 10 + int(ch)
                expression.append(ch)
                if idx == 0:
                    # 若当前val为第一个数字，则total直接为val
                    backtrack(expression, j + 1, val, val)
                else:
                    expression[sign_idx] = '+'
                    backtrack(expression, j + 1, total + val, val)
                    expression[sign_idx] = '-'
                    # total - val 可看作是 total + (-val)，last_num 为 -val
                    backtrack(expression, j + 1, total - val, -val)
                    expression[sign_idx] = '*'
                    backtrack(expression, j + 1, total - last_num + last_num * val, last_num * val)
            # 回溯时，清除掉sign_idx及其之后的所有位
            del expression[sign_idx:]

        backtrack([], 0, 0, 0)
        return res


if __name__ == '__main__':
    print(Solution().addOperators(num="232", target=8))
