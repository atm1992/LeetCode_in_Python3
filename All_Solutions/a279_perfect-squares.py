# -*- coding: UTF-8 -*-
"""
title: 完全平方数
Given an integer n, return the least number of perfect square numbers that sum to n.
A perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself. For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.


Example 1:
Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.

Example 2:
Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.


Constraints:
1 <= n <= 10^4
"""


class Solution:
    def numSquares(self, n: int) -> int:
        """动态规划。dp[i] 表示最少需要多少个 数的平方 来表示整数i。假设 i 中可以包含的最大的平方为 j^2，即 j^2 <= i <= (j+1)^2，
        则状态转移方程为 dp[i] = dp[i - j^2] + 1
        边界条件：dp[0] = 0
        """
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            # min_val最大为i，因为 i 最多需要 i 个 1 相加
            min_val = i
            j = 1
            while j * j <= i:
                min_val = min(min_val, dp[i - j * j])
                j += 1
            dp[i] = min_val + 1
        return dp[-1]

    def numSquares_2(self, n: int) -> int:
        """贪心算法。先判断n是否可以用1个数的平方来表示？用2个数的平方和来表示？用3个数的平方和来表示？……
        有一个数学定理叫做四平方和定理，该定理证明了任意一个正整数都可以被表示为至多四个正整数的平方和。也就是说答案的上界为4，
        因此只需判断1、2、3是否为结果，若不是，则直接返回4
        执行速度远超上面的动态规划。
        """
        squares = [i * i for i in range(1, int(n ** 0.5) + 1)]
        squares_set = set(squares)

        def divisible(n: int, cnt: int) -> bool:
            """数字n是否可用cnt个数字的平方和来表示"""
            if cnt == 1:
                return n in squares_set
            for square in squares:
                # 进入到for循环，表示cnt > 1，也就意味着经过了cnt为1时的遍历（cnt是从小到大遍历的），彼时返回的False，
                # 就说明squares中不存在等于n的数字，所以这里的判断条件加不加等号都没关系，因为不可能有square等于n
                if square >= n:
                    # 特别注意：如果遍历的是squares_set，那么这里就不能用break，因为set是无序的，而需要改成continue
                    break
                if divisible(n - square, cnt - 1):
                    return True
            return False

        # n 最多需要 n 个 1 相加，最终结果不可能超过n，所以最终结果的范围一定是 [1, n]
        # for cnt in range(1, n + 1):
        #     if divisible(n, cnt):
        #         return cnt

        res = 4
        # 应用四平方和定理
        for cnt in [1, 2, 3]:
            if divisible(n, cnt):
                res = cnt
                break
        return res


if __name__ == '__main__':
    print(Solution().numSquares(13))
