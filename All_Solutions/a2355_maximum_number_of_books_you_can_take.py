# -*- coding: utf-8 -*-
# @date: 2023/3/27
# @author: liuquan
"""
title: 你能拿走的最大图书数量
You are given a 0-indexed integer array books of length n where books[i] denotes the number of books on the ith shelf of a bookshelf.
You are going to take books from a contiguous section of the bookshelf spanning from l to r where 0 <= l <= r < n. For each index i in the range l <= i < r, you must take strictly fewer books from shelf i than shelf i + 1.
Return the maximum number of books you can take from the bookshelf.


Example 1:
Input: books = [8,5,2,7,9]
Output: 19
Explanation:
- Take 1 book from shelf 1.
- Take 2 books from shelf 2.
- Take 7 books from shelf 3.
- Take 9 books from shelf 4.
You have taken 19 books, so return 19.
It can be proven that 19 is the maximum number of books you can take.

Example 2:
Input: books = [7,0,3,4,5]
Output: 12
Explanation:
- Take 3 books from shelf 2.
- Take 4 books from shelf 3.
- Take 5 books from shelf 4.
You have taken 12 books so return 12.
It can be proven that 12 is the maximum number of books you can take.

Example 3:
Input: books = [8,2,3,7,3,4,0,1,4,3]
Output: 13
Explanation:
- Take 1 book from shelf 0.
- Take 2 books from shelf 1.
- Take 3 books from shelf 2.
- Take 7 books from shelf 3.
You have taken 13 books so return 13.
It can be proven that 13 is the maximum number of books you can take.


Constraints:
1 <= books.length <= 10^5
0 <= books[i] <= 10^5
"""
from typing import List


class Solution:
    def maximumBooks(self, books: List[int]) -> int:
        """
        单调递增栈 + 动态规划
        dp[i] 表示以books[i]结尾时能拿走的最大图书数量，最终结果为 max(dp)
        为了使得拿走的图书数量为最大，则尽量希望从j到i是一个公差为1的等差数列，此时的dp[i]可使用等差数列求和公式得到
        若在中间的k处断了，即 books[k] < books[i] - (i-k)，其中 j < k < i
        即 books[k] - k < books[i] - i，此时 dp[i] = dp[k] + (books[i] + (books[i] - 1) + ……)
        (books[i] + (books[i] - 1) + ……) 是一个尾项为books[i]、长度为min(i - k, books[i])、公差为1的等差数列
        注意：长度不是一定为i - k，当books[i] < i - k时，若等差数列的长度还是为i - k，则此时的首项为 books[i] - (i - k) + 1 <= 0
        即 有可能导致等差数列的前几项为负数，从而使得dp[i]反而变小。因此等差数列的长度size = min(i - k, books[i])，首项为 books[i] - size + 1
        即 dp[i] = dp[k] + size * (2 * books[i] - size + 1) // 2
        可使用一个单调栈来存储 (books[i] - i, i, dp[i])，根据 books[i] - i 递增
        """
        # 因为0 <= books[i]，所以 books[0] - 0 肯定大于 -1
        res, stack = 0, [(-1, -1, 0)]
        for i, num in enumerate(books):
            while len(stack) > 1 and stack[-1][0] >= num - i:
                stack.pop()
            _, j, dp_j = stack[-1]
            size = min(i - j, num)
            dp_i = dp_j + size * (2 * num - size + 1) // 2
            res = max(res, dp_i)
            stack.append((num - i, i, dp_i))
        return res


if __name__ == '__main__':
    print(Solution().maximumBooks(books=[7, 0, 3, 4, 5]))
