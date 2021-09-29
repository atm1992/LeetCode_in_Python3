# -*- coding: UTF-8 -*-
"""
title: 外观数列
The count-and-say sequence is a sequence of digit strings defined by the recursive formula:
countAndSay(1) = "1"
countAndSay(n) is the way you would "say" the digit string from countAndSay(n-1), which is then converted into a different digit string.
To determine how you "say" a digit string, split it into the minimal number of groups so that each group is a contiguous section all of the same character. Then for each group, say the number of characters, then say the character. To convert the saying into a digit string, replace the counts with a number and concatenate every saying.
For example, the saying and conversion for digit string "3322251":
Given a positive integer n, return the nth term of the count-and-say sequence.


Example 1:
Input: n = 1
Output: "1"
Explanation: This is the base case.

Example 2:
Input: n = 4
Output: "1211"
Explanation:
countAndSay(1) = "1"
countAndSay(2) = say "1" = one 1 = "11"
countAndSay(3) = say "11" = two 1's = "21"
countAndSay(4) = say "21" = one 2 + one 1 = "12" + "11" = "1211"
 

Constraints:
1 <= n <= 30
"""


class Solution:
    def countAndSay(self, n: int) -> str:
        res = '1'
        for _ in range(n - 1):
            tmp = {}
            tmp_res = ''
            for i in range(len(res)):
                key = str(res[i])
                pre_key = str(res[i - 1]) if i > 0 else '-1'
                if key == pre_key:
                    tmp[key] += 1
                else:
                    if pre_key != '-1':
                        tmp_res += str(tmp.pop(pre_key)) + pre_key
                    tmp[key] = 1
            tmp_res += str(tmp[res[-1]]) + res[-1]
            res = tmp_res
        return res

    def countAndSay_2(self, n: int) -> str:
        """递归 + 双指针"""
        if n == 1:
            return '1'
        last_res = self.countAndSay_2(n - 1)
        last_len = len(last_res)
        res = ''
        i, j = 0, 1
        while j < last_len:
            if last_res[j] != last_res[i]:
                res += str(j - i) + last_res[i]
                i = j
            j += 1
        res += str(j - i) + last_res[i]
        return res


if __name__ == '__main__':
    print(Solution().countAndSay_2(4))
