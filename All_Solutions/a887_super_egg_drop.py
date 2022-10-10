# -*- coding: UTF-8 -*-
"""
title: 鸡蛋掉落
You are given k identical eggs and you have access to a building with n floors labeled from 1 to n.
You know that there exists a floor f where 0 <= f <= n such that any egg dropped at a floor higher than f will break, and any egg dropped at or below floor f will not break.
Each move, you may take an unbroken egg and drop it from any floor x (where 1 <= x <= n). If the egg breaks, you can no longer use it. However, if the egg does not break, you may reuse it in future moves.
Return the minimum number of moves that you need to determine with certainty what the value of f is.


Example 1:
Input: k = 1, n = 2
Output: 2
Explanation:
Drop the egg from floor 1. If it breaks, we know that f = 0.
Otherwise, drop the egg from floor 2. If it breaks, we know that f = 1.
If it does not break, then we know f = 2.
Hence, we need at minimum 2 moves to determine with certainty what the value of f is.

Example 2:
Input: k = 2, n = 6
Output: 3

Example 3:
Input: k = 3, n = 14
Output: 4


Constraints:
1 <= k <= 100
1 <= n <= 10^4
"""


class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        """
        动态规划。参考LeetCode题1884。运行超时，通过 63/121 个测试用例
        假设 dp[i][j] 表示当前有i枚鸡蛋、需要验证j层楼的最小操作次数
        状态转移方程：
        当i为1时，只有1枚鸡蛋，此时只能选择从1楼开始逐层向上验证，即 dp[1][j] = j
        当i大于1时，可任选一枚鸡蛋先在[1, j]中的任一楼层k进行验证，
            若该枚鸡蛋碎了，则问题转化为当前有i-1枚鸡蛋、需要验证k-1层楼的最小操作次数，即 dp[i][j] = dp[i-1][k-1] + 1
            若该枚鸡蛋没碎，则问题转化为当前有i枚鸡蛋、需要验证j-k层楼的最小操作次数，即 dp[i][j] = dp[i][j-k] + 1
            综上，考虑最坏情况，选择上面两种情况的较大值，dp[i][j] = min(dp[i][j], max(dp[i-1][k-1] + 1, dp[i][j-k] + 1))
        """
        # 楼层数为0时，无需任何操作。因为n <= 10^4，所以最多只需操作10000次
        dp = [[i for i in range(n + 1)]] + [[0] + [10000] * n for _ in range(k - 1)]
        for i in range(1, k):
            for j in range(1, n + 1):
                for k in range(1, j + 1):
                    dp[i][j] = min(dp[i][j], max(dp[i - 1][k - 1] + 1, dp[i][j - k] + 1))
        return dp[-1][-1]

    def superEggDrop_2(self, k: int, n: int) -> int:
        """
        动态规划 + 二分查找。
        优化方法一，方法一的时间复杂度为O(kn^2)，可使用二分查找优化至O(knlogn)，使用二分查找的方式来确定k
        可知dp[i-1][k-1]是个关于k的单调递增函数，在鸡蛋数i固定的情况下，楼层数k越大，自然就需要更多的操作次数。
        而dp[i][j-k]是个关于k的单调递减函数，i、j固定，k越大，需要的操作次数越少。
        因此，如果dp[i-1][k-1]、dp[i][j-k]是连续函数，那么让max(dp[i-1][k-1] + 1, dp[i][j-k] + 1)最小的k就是两者的交点。
        但dp[i-1][k-1]、dp[i][j-k]实际是离散函数，因此需要确定出交点左右两侧的点 k'、k'+1，其中，dp[i-1][k'-1] <= dp[i][j-k']，dp[i-1][k'] >= dp[i][j-k'-1]
        然后比较这两个点的计算结果，便可得到最小的dp[i][j]
        """
        # 楼层数为0时，无需任何操作。因为n <= 10^4，所以最多只需操作10000次
        dp = [[i for i in range(n + 1)]] + [[0] + [10000] * n for _ in range(k - 1)]
        for i in range(1, k):
            for j in range(1, n + 1):
                low, high = 1, j
                # 退出while循环时，low + 1 >= high。high等于1时，不会进入while循环；while循环中查找到了交点时，low = high = mid。
                # 之后比较这两个点的计算结果时，不能使用low、low+1，而应使用low、high，因为当high等于1时，low+1会越界
                while low + 1 < high:
                    mid = (low + high) // 2
                    if dp[i - 1][mid - 1] < dp[i][j - mid]:
                        low = mid
                    elif dp[i - 1][mid - 1] > dp[i][j - mid]:
                        high = mid
                    else:
                        # 这种二分查找的写法可以尽快退出while循环。常规的写法在此题会超时，通过 121/121 个测试用例
                        low = high = mid
                dp[i][j] = min(max(dp[i - 1][k - 1] + 1, dp[i][j - k] + 1) for k in (low, high))
        return dp[-1][-1]

    def superEggDrop_3(self, k: int, n: int) -> int:
        """
        动态规划 + 逆向思维。执行效率远超上面的方法
        假设有t次操作、k枚鸡蛋，求最多可以验证的楼层数f(t, k)。求出所有的f(t, k)之后，找到第一个满足 f(t, k) >= n 的t，即为最终所求结果
        使用动态规划求解所有的f(t, k)，假设在任意一层扔了一个鸡蛋：
            1、若这个鸡蛋没碎，则对应的是 f(t-1, k)，即 在扔鸡蛋的那层楼上可以有 f(t-1, k) 层
            2、若这个鸡蛋碎了，则对应的是 f(t-1, k-1)，即 在扔鸡蛋的那层楼下可以有 f(t-1, k-1) 层
        因此，状态转移方程为：f(t, k) = f(t-1, k-1) + 1 + f(t-1, k)
        边界条件：只能操作1次时，若鸡蛋数大于0，则最多只能验证1层楼；若鸡蛋数等于0，则只能验证0层楼。
        """
        # 已知1 <= k，若给定的楼层数n为1，则只需1次操作
        if n == 1:
            return 1
        # dp数组初始化为操作1次时的情况。鸡蛋数为0时，只能验证0层楼
        dp = [0] + [1] * k
        # 从操作2次开始计算，操作次数t最大不会超过楼层数n，所以最多计算n次操作就一定能验证n层楼。
        for i in range(2, n + 1):
            # 鸡蛋数为0时，只能验证0层楼，因此无需计算
            for j in range(k, 0, -1):
                dp[j] += dp[j - 1] + 1
                # 这个条件一定会成立，因为最多会计算n次操作，而n次操作一定能验证n层楼。另外在固定k的情况下，dp[t][k]是关于t单调递增的
                if j == k and dp[j] >= n:
                    return i


if __name__ == '__main__':
    print(Solution().superEggDrop_3(k=200, n=100000))
