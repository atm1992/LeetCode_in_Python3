# -*- coding: UTF-8 -*-
"""
title: 青蛙过河
A frog is crossing a river. The river is divided into some number of units, and at each unit, there may or may not exist a stone. The frog can jump on a stone, but it must not jump into the water.
Given a list of stones' positions (in units) in sorted ascending order, determine if the frog can cross the river by landing on the last stone. Initially, the frog is on the first stone and assumes the first jump must be 1 unit.
If the frog's last jump was k units, its next jump must be either k - 1, k, or k + 1 units. The frog can only jump in the forward direction.


Example 1:
Input: stones = [0,1,3,5,6,8,12,17]
Output: true
Explanation: The frog can jump to the last stone by jumping 1 unit to the 2nd stone, then 2 units to the 3rd stone, then 2 units to the 4th stone, then 3 units to the 6th stone, 4 units to the 7th stone, and 5 units to the 8th stone.

Example 2:
Input: stones = [0,1,2,3,4,8,9,11]
Output: false
Explanation: There is no way to jump to the last stone as the gap between the 5th and 6th stone is too large.


Constraints:
2 <= stones.length <= 2000
0 <= stones[i] <= 2^31 - 1
stones[0] == 0
stones is sorted in a strictly increasing order.
"""
from typing import List


class Solution:
    def canCross(self, stones: List[int]) -> bool:
        """
        动态规划。注意：只要能够到达最后一个石子，就表示能够成功过河，并未要求每个石子都要走一遍，有些中间石子是可以跳过的。
        dp[i][k] 表示青蛙能否从上一个石子跳跃k个单位到达编号为i的石子。所有石子的编号范围为: [0, n-1]
        状态转移方程：
        dp[i][k] = dp[j][k-1] or dp[j][k] or dp[j][k+1]。假设上一个石子的编号为j，只有当到达石子j时的步数为k-1或k或k+1时，从石子j跳到石子i的步数才允许为k，即 stones[i] - stones[j] = k
        初始值：dp[0][0] = True。从上一个石子跳跃到编号为0的石子(即第一个石子)的步数为0，这样可以保证从第一个石子开始跳跃的步数只能为1。为0、-1没有实际意义
        只要 dp[n-1][*] 中有一个为True，就表示能够到达最后一个石子，即 能够成功过河。
        算法优化：
        1、初始时，青蛙通过跳0步到达石子0，之后每次跳跃，青蛙所在的石子编号至少加1，而每次跳跃的步数最多加1，所以可知，青蛙从石子j跳到石子i的步数k必定小于等于i
        2、若石子j与石子i之间的距离大于i，则表示青蛙无法从石子j跳到石子i，直接返回False
        """
        n = len(stones)
        dp = [[False] * n for _ in range(n)]
        dp[0][0] = True
        # 先遍历一次所有的石子，验证是否存在无法跳跃过去的两个相邻石子
        for i in range(1, n):
            if stones[i] - stones[i - 1] > i:
                return False
        for i in range(1, n):
            for j in range(i - 1, -1, -1):
                k = stones[i] - stones[j]
                # 因为从上一个石子跳到石子j所使用的步数最多只能为j，所以从石子j跳到石子i的步数最多为j+1
                # 若k大于j+1，则表示无需再尝试更前面的石子了，因为无法从它们跳到石子i
                if k > j + 1:
                    break
                dp[i][k] = dp[j][k - 1] or dp[j][k] or dp[j][k + 1]
                if i == n - 1 and dp[i][k]:
                    return True
        return False


if __name__ == '__main__':
    print(Solution().canCross(stones=[0, 1, 2, 3, 4, 8, 9, 11]))
