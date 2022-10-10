# -*- coding: UTF-8 -*-
"""
title: 鸡蛋掉落-两枚鸡蛋
You are given two identical eggs and you have access to a building with n floors labeled from 1 to n.
You know that there exists a floor f where 0 <= f <= n such that any egg dropped at a floor higher than f will break, and any egg dropped at or below floor f will not break.
In each move, you may take an unbroken egg and drop it from any floor x (where 1 <= x <= n). If the egg breaks, you can no longer use it. However, if the egg does not break, you may reuse it in future moves.
Return the minimum number of moves that you need to determine with certainty what the value of f is.


Example 1:
Input: n = 2
Output: 2
Explanation: We can drop the first egg from floor 1 and the second egg from floor 2.
If the first egg breaks, we know that f = 0.
If the second egg breaks but the first egg didn't, we know that f = 1.
Otherwise, if both eggs survive, we know that f = 2.

Example 2:
Input: n = 100
Output: 14
Explanation: One optimal strategy is:
- Drop the 1st egg at floor 9. If it breaks, we know f is between 0 and 8. Drop the 2nd egg starting from floor 1 and going up one at a time to find f within 8 more drops. Total drops is 1 + 8 = 9.
- If the 1st egg does not break, drop the 1st egg again at floor 22. If it breaks, we know f is between 9 and 21. Drop the 2nd egg starting from floor 10 and going up one at a time to find f within 12 more drops. Total drops is 2 + 12 = 14.
- If the 1st egg does not break again, follow a similar process dropping the 1st egg from floors 34, 45, 55, 64, 72, 79, 85, 90, 94, 97, 99, and 100.
Regardless of the outcome, it takes at most 14 drops to determine f.


Constraints:
1 <= n <= 1000
"""
import math


class Solution:
    def twoEggDrop(self, n: int) -> int:
        """
        动态规划
        假设 dp[i][j] 表示当前有i枚鸡蛋、需要验证j层楼的最小操作次数
        状态转移方程：
        当i为1时，只有1枚鸡蛋，此时只能选择从1楼开始逐层向上验证，即 dp[1][j] = j
        当i为2时，第一次操作可选择在[1, j]中的任一楼层k进行验证，
            若第一枚鸡蛋碎了，则问题转化为当前有1枚鸡蛋、需要验证k-1层楼的最小操作次数，即 dp[2][j] = dp[1][k-1] + 1 = k
            若第一枚鸡蛋没碎，则问题转化为当前有2枚鸡蛋、需要验证j-k层楼的最小操作次数，即 dp[2][j] = dp[2][j-k] + 1
            综上，考虑最坏情况，选择上面两种情况的较大值，dp[2][j] = min(dp[2][j], max(k, dp[2][j-k] + 1))
        """
        # 因为dp[1][j] = j，可根据j直接获取dp[1]的结果，因此dp数组只需保存dp[2]的结果。初始值dp[2][0] = 0，0层楼无需操作
        dp = [0]
        for j in range(1, n + 1):
            # n <= 1000，最多只需操作1000次
            tmp = 1000
            for k in range(1, j + 1):
                tmp = min(tmp, max(k, dp[j - k] + 1))
            dp.append(tmp)
        return dp[-1]

    def twoEggDrop_2(self, n: int) -> int:
        """
        动态规划 + 逆向思维。参考LeetCode题887
        假设有t次操作、k枚鸡蛋，求最多可以验证的楼层数f(t, k)。求出所有的f(t, k)之后，找到第一个满足 f(t, k) >= n 的t，即为最终所求结果
        使用动态规划求解所有的f(t, k)，假设在任意一层扔了一个鸡蛋：
            1、若这个鸡蛋没碎，则对应的是 f(t-1, k)，即 在扔鸡蛋的那层楼上可以有 f(t-1, k) 层
            2、若这个鸡蛋碎了，则对应的是 f(t-1, k-1)，即 在扔鸡蛋的那层楼下可以有 f(t-1, k-1) 层
        此题的k固定为2，因此，状态转移方程为：f(t, 2) = f(t-1, 1) + 1 + f(t-1, 2)
        因为只有1枚鸡蛋时，只能从1楼开始逐层向上验证，所以此时的操作次数就等于可验证的楼层数，即 f(t-1, 1) = t-1
        所以，f(t, 2) = t + f(t-1, 2)
        初始值：2枚鸡蛋的情况下，操作1次时，最多只能验证1层楼，即 f(1, 2) = 1
        """
        # 已知k == 2，若给定的楼层数n为1，则只需1次操作
        if n == 1:
            return 1
        floor = 1
        # 从操作2次开始计算，操作次数t最大不会超过楼层数n，所以最多计算n次操作就一定能验证n层楼。
        for t in range(2, n + 1):
            floor += t
            if floor >= n:
                return t

    def twoEggDrop_3(self, n: int) -> int:
        """
        数学
        方法二中的状态转移方程：f(t, 2) = t + f(t-1, 2) ，f(1, 2) = 1
        其实可使用数学公式进行计算，f(t, 2) = 1 + 2 + …… + t-1 + t = t * (t+1) / 2
        要求找到第一个满足 t * (t+1) / 2 >= n 的t值
        """
        return math.ceil((math.sqrt(8 * n + 1) - 1) / 2)


if __name__ == '__main__':
    print(Solution().twoEggDrop_3(100))
