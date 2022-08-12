# -*- coding: UTF-8 -*-
"""
title: 字母大小写全排列
Given a string s, you can transform every letter individually to be lowercase or uppercase to create another string.
Return a list of all possible strings we could create. Return the output in any order.


Example 1:
Input: s = "a1b2"
Output: ["a1b2","a1B2","A1b2","A1B2"]

Example 2:
Input: s = "3z4"
Output: ["3z4","3Z4"]


Constraints:
1 <= s.length <= 12
s consists of lowercase English letters, uppercase English letters, and digits.
"""
from typing import List


class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        """迭代"""
        res = [[]]
        for ch in s:
            n = len(res)
            if ch.isalpha():
                for i in range(n):
                    # 将当前已遍历过的字符所组成的全排列复制一份，放到res的末尾，其下标为 n+i
                    res.append(res[i][:])
                    res[i].append(ch.lower())
                    res[n + i].append(ch.upper())
            else:
                for i in range(n):
                    res[i].append(ch)
        return [''.join(item) for item in res]

    def letterCasePermutation_2(self, s: str) -> List[str]:
        """
        位掩码
        假设字符串s中的大小写字母个数为m，则最终结果中会有2^m个字符串。可用m位的二进制数(位掩码)来表示各个字母的大小写情况。
        例如：s = "a1b2"，则位掩码可为00、01、10、11，分别对应 "a1b2"、"a1B2"、"A1b2"、"A1B2"
        """
        m = sum(ch.isalpha() for ch in s)
        res = []
        for bits in range(1 << m):
            idx = 0
            word = []
            for ch in s:
                if ch.isalpha():
                    if (bits >> idx) & 1:
                        word.append(ch.upper())
                    else:
                        word.append(ch.lower())
                    # 注意：只有当ch是英文字母时，idx才会加1
                    idx += 1
                else:
                    word.append(ch)
            res.append(''.join(word))
        return res


if __name__ == '__main__':
    print(Solution().letterCasePermutation_2("a1b2"))
