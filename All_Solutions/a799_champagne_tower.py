# -*- coding: utf-8 -*-
# @date: 2023/3/29
# @author: liuquan
"""
title: 香槟塔
We stack glasses in a pyramid, where the first row has 1 glass, the second row has 2 glasses, and so on until the 100th row.  Each glass holds one cup of champagne.
Then, some champagne is poured into the first glass at the top. When the topmost glass is full, any excess liquid poured will fall equally to the glass immediately to the left and right of it.  When those glasses become full, any excess champagne will fall equally to the left and right of those glasses, and so on. (A glass at the bottom row has its excess champagne fall on the floor.)
For example, after one cup of champagne is poured, the top most glass is full. After two cups of champagne are poured, the two glasses on the second row are half full.  After three cups of champagne are poured, those two cups become full - there are 3 full glasses total now. After four cups of champagne are poured, the third row has the middle glass half full, and the two outside glasses are a quarter full, as pictured below.
Now after pouring some non-negative integer cups of champagne, return how full the jth glass in the ith row is (both i and j are 0-indexed.)


Example 1:
Input: poured = 1, query_row = 1, query_glass = 1
Output: 0.00000
Explanation: We poured 1 cup of champange to the top glass of the tower (which is indexed as (0, 0)). There will be no excess liquid so all the glasses under the top glass will remain empty.

Example 2:
Input: poured = 2, query_row = 1, query_glass = 1
Output: 0.50000
Explanation: We poured 2 cups of champange to the top glass of the tower (which is indexed as (0, 0)). There is one cup of excess liquid. The glass indexed as (1, 0) and the glass indexed as (1, 1) will share the excess liquid equally, and each will get half cup of champange.

Example 3:
Input: poured = 100000009, query_row = 33, query_glass = 17
Output: 1.00000


Constraints:
0 <= poured <= 10^9
0 <= query_glass <= query_row < 100
"""
from functools import lru_cache


class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        """
        记忆化搜索
        dp[i][j] = (dp[i-1][j-1] - 1) / 2 + (dp[i-1][j] - 1) / 2
        只有当自身装满后，才会向下流
        dp[0]中只有dp[0][0] = poured，其余的dp[0]均为0
        """

        @lru_cache(None)
        def helper(i: int, j: int) -> float:
            if i == 0:
                return poured if j == 0 else 0
            left, right = 0, 0
            # 剪枝
            if j - 1 >= 0:
                left = max(helper(i - 1, j - 1) - 1, 0)
            if j >= 0:
                right = max(helper(i - 1, j) - 1, 0)
            return (left + right) / 2

        return min(helper(query_row, query_glass), 1)

    def champagneTower_2(self, poured: int, query_row: int, query_glass: int) -> float:
        """模拟"""
        # 初始时，将所有的香槟一次性倒给 (0, 0)
        cur_now = [poured]
        for i in range(1, query_row + 1):
            nxt_row = [0] * (i + 1)
            for j, num in enumerate(cur_now):
                num = (num - 1) / 2
                if num > 0:
                    nxt_row[j] += num
                    nxt_row[j + 1] += num
            cur_now = nxt_row
        return min(cur_now[query_glass], 1)


if __name__ == '__main__':
    print(Solution().champagneTower_2(poured=25, query_row=6, query_glass=1))
