# -*- coding: utf-8 -*-
# @date: 2023/4/23
# @author: liuquan
"""
title: 填充书架
You are given an array books where books[i] = [thicknessi, heighti] indicates the thickness and height of the ith book. You are also given an integer shelfWidth.
We want to place these books in order onto bookcase shelves that have a total width shelfWidth.
We choose some of the books to place on this shelf such that the sum of their thickness is less than or equal to shelfWidth, then build another level of the shelf of the bookcase so that the total height of the bookcase has increased by the maximum height of the books we just put down. We repeat this process until there are no more books to place.
Note that at each step of the above process, the order of the books we place is the same order as the given sequence of books.
    For example, if we have an ordered list of 5 books, we might place the first and second book onto the first shelf, the third book on the second shelf, and the fourth and fifth book on the last shelf.
Return the minimum possible height that the total bookshelf can be after placing shelves in this manner.


Example 1:
Input: books = [[1,1],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]], shelfWidth = 4
Output: 6
Explanation:
The sum of the heights of the 3 shelves is 1 + 3 + 2 = 6.
Notice that book number 2 does not have to be on the first shelf.

Example 2:
Input: books = [[1,3],[2,4],[3,2]], shelfWidth = 6
Output: 4


Constraints:
1 <= books.length <= 1000
1 <= thicknessi <= shelfWidth <= 1000
1 <= heighti <= 1000
"""
from typing import List


class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        """
        动态规划
        dp[i]表示放置前i本书的最小高度
        状态转移方程：
        1、若将books[i]单独放在一层，则 dp[i] = dp[i-1] + books[i][1]
        2、若将books[i]和前面的若干本书放在同一层，前面的若干本书的厚度 + books[i][0]需满足小于等于shelfWidth，因此，可以从后往前遍历，
        找到最小的 dp[j-1] + max_height。表示将books[j]作为最后一层的第一本书，max_height 表示最后一层的最大高度
        初始值：因为题目已知books.length <= 1000 and heighti <= 1000 and thicknessi <= shelfWidth，所以最差情况就是一层只放一本书，
        高度不会超过 1000 * 1000，因此，可将dp[*]设置为 1000000，dp[0] = 0 没有一本书时，高度为0
        """
        n = len(books)
        dp = [0] + [1000000] * n
        for i in range(1, n + 1):
            j, total_t, max_h = i - 1, 0, 0
            while j >= 0 and total_t + books[j][0] <= shelfWidth:
                max_h = max(max_h, books[j][1])
                dp[i] = min(dp[i], dp[j] + max_h)
                total_t += books[j][0]
                j -= 1
        return dp[-1]


if __name__ == '__main__':
    print(Solution().minHeightShelves(books=[[1, 1], [2, 3], [2, 3], [1, 1], [1, 1], [1, 1], [1, 2]], shelfWidth=4))
