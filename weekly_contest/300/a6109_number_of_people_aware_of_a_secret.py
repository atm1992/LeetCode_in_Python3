# -*- coding: UTF-8 -*-
"""
title: 知道秘密的人数
On day 1, one person discovers a secret.
You are given an integer delay, which means that each person will share the secret with a new person every day, starting from delay days after discovering the secret. You are also given an integer forget, which means that each person will forget the secret forget days after discovering it. A person cannot share the secret on the same day they forgot it, or on any day afterwards.
Given an integer n, return the number of people who know the secret at the end of day n. Since the answer may be very large, return it modulo 10^9 + 7.


Example 1:
Input: n = 6, delay = 2, forget = 4
Output: 5
Explanation:
Day 1: Suppose the first person is named A. (1 person)
Day 2: A is the only person who knows the secret. (1 person)
Day 3: A shares the secret with a new person, B. (2 people)
Day 4: A shares the secret with a new person, C. (3 people)
Day 5: A forgets the secret, and B shares the secret with a new person, D. (3 people)
Day 6: B shares the secret with E, and C shares the secret with F. (5 people)

Example 2:
Input: n = 4, delay = 1, forget = 3
Output: 6
Explanation:
Day 1: The first person is named A. (1 person)
Day 2: A shares the secret with B. (2 people)
Day 3: A and B share the secret with 2 new people, C and D. (4 people)
Day 4: A forgets the secret. B, C, and D share the secret with 3 new people. (6 people)


Constraints:
2 <= n <= 1000
1 <= delay < forget <= n
"""


class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        """
        动态规划
        dp[i] 表示在第i天刚知道秘密的人。1 <= i <= n, dp[0] = 0, dp[1] = 1
        第i天刚知道秘密的人可以在第[i+delay, i+forget)天分享给别人，所以在第i+delay天刚知道秘密的人中，有一部分贡献来自于dp[i]。
        也就意味着dp[i]可以向dp[i+delay] ~ dp[i+forget-1]做贡献。
        最后第n天知道秘密的总人数为：在第[n-forget+1, n]天刚知道秘密的人，只有这些人在第n天会还记得秘密。
        """
        mod = 10 ** 9 + 7
        dp = [0] * (n + 1)
        dp[1] = 1
        for i in range(1, n + 1):
            if dp[i] == 0:
                continue
            for j in range(i + delay, min(i + forget, n + 1)):
                dp[j] = (dp[j] + dp[i]) % mod
        res = 0
        # forget <= n
        for i in range(n - forget + 1, n + 1):
            res = (res + dp[i]) % mod
        return res

    def peopleAwareOfSecret_2(self, n: int, delay: int, forget: int) -> int:
        """
        动态规划 + 前缀和优化
        dp[i] 表示在第i天刚知道秘密的人。1 <= i <= n, dp[0] = 0, dp[1] = 1
        dp[i] 可以从dp[i-forget+1] ~ dp[i-delay]转移过来，即 dp[i] = sum(dp[i-forget+1], ……, dp[i-delay])
        最后第n天知道秘密的总人数为：在第[n-forget+1, n]天刚知道秘密的人，只有这些人在第n天会还记得秘密。即 res = sum(dp[n-forget+1], ……, dp[n])
        pre_sum[i] 表示前i天内刚知道秘密的人。1 <= i <= n, pre_sum[0] = 0, pre_sum[1] = 1
        所以，dp[i] = sum(dp[i-forget+1], ……, dp[i-delay]) = pre_sum[i-delay] - pre_sum[i-forget]
        res = sum(dp[n-forget+1], ……, dp[n]) = pre_sum[n] - pre_sum[n-forget]
        """
        mod = 10 ** 9 + 7
        pre_sum = [0] * (n + 1)
        pre_sum[1] = 1
        for i in range(2, n + 1):
            dp_i = (pre_sum[max(i - delay, 0)] - pre_sum[max(i - forget, 0)]) % mod
            pre_sum[i] = (pre_sum[i - 1] + dp_i) % mod
        # Python 中，-2 % 10 == 8。所以无需像其它语言那样，((pre_sum[n] - pre_sum[n-forget]) % mod + mod) % mod
        return (pre_sum[n] - pre_sum[n - forget]) % mod


if __name__ == '__main__':
    print(Solution().peopleAwareOfSecret(n=6, delay=2, forget=4))
