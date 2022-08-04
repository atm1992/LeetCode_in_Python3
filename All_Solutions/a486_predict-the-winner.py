# -*- coding: UTF-8 -*-
"""
title: 预测赢家
You are given an integer array nums. Two players are playing a game with this array: player 1 and player 2.
Player 1 and player 2 take turns, with player 1 starting first. Both players start the game with a score of 0. At each turn, the player takes one of the numbers from either end of the array (i.e., nums[0] or nums[nums.length - 1]) which reduces the size of the array by 1. The player adds the chosen number to their score. The game ends when there are no more elements in the array.
Return true if Player 1 can win the game. If the scores of both players are equal, then player 1 is still the winner, and you should also return true. You may assume that both players are playing optimally.


Example 1:
Input: nums = [1,5,2]
Output: false
Explanation: Initially, player 1 can choose between 1 and 2.
If he chooses 2 (or 1), then player 2 can choose from 1 (or 2) and 5. If player 2 chooses 5, then player 1 will be left with 1 (or 2).
So, final score of player 1 is 1 + 2 = 3, and player 2 is 5.
Hence, player 1 will never be the winner and you need to return false.

Example 2:
Input: nums = [1,5,233,7]
Output: true
Explanation: Player 1 first chooses 1. Then player 2 has to choose between 5 and 7. No matter which number player 2 choose, player 1 can choose 233.
Finally, player 1 has more score (234) than player 2 (12), so you need to return True representing player1 can win.


Constraints:
1 <= nums.length <= 20
0 <= nums[i] <= 10^7
"""
from typing import List


class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        """
        动态规划
        dp[i][j] 表示在下标[i, j]范围内，当前玩家与另一个玩家的分数之差的最大值，注意：当前玩家不一定是先手。
        1、i > j时，表示当前剩余数组为空，此时 dp[i][j] = 0
        2、i == j时，表示当前剩余数组只有一个元素，此时 dp[i][j] = nums[i]
        3、i < j时，当前玩家可选nums[i]或nums[j]，从中选择可以让分数之差达到最大的那个元素：
        3.1、若当前玩家选择了nums[i]，则另一玩家能获得的最大分数之差就是dp[i+1][j]，因此当前玩家能获得的最大分数之差就是nums[i] - dp[i+1][j]；
        3.2、若当前玩家选择了nums[j]，则另一玩家能获得的最大分数之差就是dp[i][j-1]，因此当前玩家能获得的最大分数之差就是nums[j] - dp[i][j-1]；
        对上述两种情况取最大值，就是当前玩家最终能获得的最大分数之差，即 dp[i][j] = max(nums[i] - dp[i+1][j], nums[j] - dp[i][j-1])
        最终的dp[0][n-1]就表示玩家1能获得的最大分数之差，若 dp[0][n-1] >= 0，则返回True
        """
        n = len(nums)
        dp = [[0] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if i == j:
                    dp[i][j] = nums[i]
                else:
                    dp[i][j] = max(nums[i] - dp[i + 1][j], nums[j] - dp[i][j - 1])
        return dp[0][n - 1] >= 0

    def PredictTheWinner_2(self, nums: List[int]) -> bool:
        """动态规划。使用滚动数组降低方法一的空间复杂度"""
        n = len(nums)
        dp = [0] * n
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if i == j:
                    dp[j] = nums[i]
                else:
                    dp[j] = max(nums[i] - dp[j], nums[j] - dp[j - 1])
        return dp[-1] >= 0


if __name__ == '__main__':
    print(Solution().PredictTheWinner([1, 5, 233, 7]))
