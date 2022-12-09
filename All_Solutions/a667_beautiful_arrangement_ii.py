# -*- coding: UTF-8 -*-
"""
title: 优美的排列 II
Given two integers n and k, construct a list answer that contains n different positive integers ranging from 1 to n and obeys the following requirement:
    Suppose this list is answer = [a1, a2, a3, ... , an], then the list [|a1 - a2|, |a2 - a3|, |a3 - a4|, ... , |an-1 - an|] has exactly k distinct integers.
Return the list answer. If there multiple valid answers, return any of them.


Example 1:
Input: n = 3, k = 1
Output: [1,2,3]
Explanation: The [1,2,3] has three different positive integers ranging from 1 to 3, and the [1,1] has exactly 1 distinct integer: 1

Example 2:
Input: n = 3, k = 2
Output: [1,3,2]
Explanation: The [1,3,2] has three different positive integers ranging from 1 to 3, and the [2,1] has exactly 2 distinct integers: 1 and 2.


Constraints:
1 <= k < n <= 10^4
"""
from typing import List


class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        """
        脑筋急转弯。从特殊情况到一般情况
        当k为1时，序列1 ~ n可以按如下顺序[1, 2, 3, ……, n-1, n]排列，相邻元素的差值均为1
        当k取最大值n-1时，序列1 ~ n可以按如下顺序[1, n, 2, n-1, 3, ……]排列，相邻元素的差值从n-1到1
        对于其它的一般情况，可以让前半部分完全升序(即 相邻元素的差值均为1)，后半部分的差值从k到1，即 [1, 2, ……, n-k, n, n-k+1, n-1, n-k+2, ……]
        """
        res = list(range(1, n - k))
        i, j = n - k, n
        while i <= j:
            res.append(i)
            if i < j:
                res.append(j)
            i += 1
            j -= 1
        return res


if __name__ == '__main__':
    print(Solution().constructArray(n=7, k=5))
