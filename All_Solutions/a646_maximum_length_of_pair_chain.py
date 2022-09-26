# -*- coding: UTF-8 -*-
"""
title: 最长数对链
You are given an array of n pairs pairs where pairs[i] = [lefti, righti] and lefti < righti.
A pair p2 = [c, d] follows a pair p1 = [a, b] if b < c. A chain of pairs can be formed in this fashion.
Return the length longest chain which can be formed.
You do not need to use up all the given intervals. You can select pairs in any order.


Example 1:
Input: pairs = [[1,2],[2,3],[3,4]]
Output: 2
Explanation: The longest chain is [1,2] -> [3,4].

Example 2:
Input: pairs = [[1,2],[7,8],[4,5]]
Output: 3
Explanation: The longest chain is [1,2] -> [4,5] -> [7,8].


Constraints:
n == pairs.length
1 <= n <= 1000
-1000 <= lefti < righti <= 1000
"""
from typing import List


class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        """
        排序 + 动态规划。参考LeetCode题435。
        假设 dp[i] 表示以数对i结尾的最长数对链的长度。
        状态转移方程：dp[i] = max(dp[j]) + 1 其中，pairs[j][0] < pairs[i][0] 且 pairs[j][1] < pairs[i][0]
        """
        sorted_pairs = sorted(pairs)
        dp = []
        for i, (num, _) in enumerate(sorted_pairs):
            cur_len = 0
            for j in range(i - 1, -1, -1):
                if j + 1 <= cur_len:
                    break
                if sorted_pairs[j][1] < num:
                    cur_len = max(cur_len, dp[j])
            dp.append(cur_len + 1)
        # 可以验证，此时的 max(dp) == dp[-1]
        return dp[-1]

    def findLongestChain_2(self, pairs: List[List[int]]) -> int:
        """
        排序 + 贪心。参考LeetCode题435。执行速度远快于上面。
        要使数对链尽可能长，则需让数对递增得尽可能慢，因此希望每次append的那个数对的right尽可能小。若多个数对的right都相同(即 存在重叠)，
        则只需从中选出任意一个left符合要求的数对即可。先对pairs按right升序，然后对符合要求的数对进行累加
        """
        res = 0
        # -1000 <= lefti
        pre_right = -1001
        for left, right in sorted(pairs, key=lambda item: item[1]):
            if pre_right < left:
                pre_right = right
                res += 1
        return res


if __name__ == '__main__':
    print(Solution().findLongestChain_2([[1, 2], [2, 3], [3, 4]]))
