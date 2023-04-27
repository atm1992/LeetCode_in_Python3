# -*- coding: utf-8 -*-
# @date: 2023/4/22
# @author: liuquan
"""
title: 使数组严格递增
Given two integer arrays arr1 and arr2, return the minimum number of operations (possibly zero) needed to make arr1 strictly increasing.
In one operation, you can choose two indices 0 <= i < arr1.length and 0 <= j < arr2.length and do the assignment arr1[i] = arr2[j].
If there is no way to make arr1 strictly increasing, return -1.


Example 1:
Input: arr1 = [1,5,3,6,7], arr2 = [1,3,2,4]
Output: 1
Explanation: Replace 5 with 2, then arr1 = [1, 2, 3, 6, 7].

Example 2:
Input: arr1 = [1,5,3,6,7], arr2 = [4,3,1]
Output: 2
Explanation: Replace 5 with 3 and then replace 3 with 4. arr1 = [1, 3, 4, 6, 7].

Example 3:
Input: arr1 = [1,5,3,6,7], arr2 = [1,6,3,3]
Output: -1
Explanation: You can't make arr1 strictly increasing.


Constraints:
1 <= arr1.length, arr2.length <= 2000
0 <= arr1[i], arr2[i] <= 10^9
"""
from functools import lru_cache
from typing import List


class Solution:
    def makeArrayIncreasing(self, a: List[int], b: List[int]) -> int:
        """
        排序 + 二分查找 + 记忆化搜索
        dp[i][nxt] 表示将数组a中的前i个元素变成严格递增、且a[i] < nxt的最小操作次数
        状态转移方程：
        1、若a[i] < nxt，则可以选择不替换a[i]，此时 dp[i][nxt] = dp[i-1][a[i]]
        2、若数组b中存在小于nxt的值，则可选择将a[i]替换为数组b中小于nxt的最大值cur，此时 dp[i][nxt] = dp[i-1][cur] + 1。注意：此时无需关心a[i] 是否小于 nxt
        3、若a[i] >= nxt，且数组b中不存在小于nxt的值，则表示无法将数组a变成严格递增，此时返回+∞
        综上，取上面3种情况的最小值作为dp[i][nxt]
        最终结果为 dp[n-1][+∞] 可认为在数组a的末尾有一个哨兵元素+∞
        """
        # 对数组b进行升序，方便之后通过二分查找小于nxt的最大值cur
        b.sort()
        n = len(b)
        # arr1[i], arr2[i] <= 10^9
        MAX_INT = 10 ** 9 + 1

        @lru_cache(None)
        def dfs(i: int, nxt: int) -> int:
            if i < 0:
                return 0
            res = dfs(i - 1, a[i]) if a[i] < nxt else MAX_INT
            if b[0] >= nxt:
                return res
            l, r = 0, n - 1
            while l < r:
                mid = (l + r + 1) // 2
                if b[mid] >= nxt:
                    r = mid - 1
                else:
                    l = mid
            return min(res, dfs(i - 1, b[l]) + 1)

        res = dfs(len(a) - 1, MAX_INT)
        return res if res < MAX_INT else -1


if __name__ == '__main__':
    print(Solution().makeArrayIncreasing(a=[1, 5, 3, 6, 7], b=[1, 6, 3, 3]))
