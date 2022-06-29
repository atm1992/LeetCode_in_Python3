# -*- coding: UTF-8 -*-
"""
title: K 站中转内最便宜的航班
There are n cities connected by some number of flights. You are given an array flights where flights[i] = [fromi, toi, pricei] indicates that there is a flight from city fromi to city toi with cost pricei.
You are also given three integers src, dst, and k, return the cheapest price from src to dst with at most k stops. If there is no such route, return -1.


Example 1:
Input: n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1
Output: 700
Explanation:
The graph is shown above.
The optimal path with at most 1 stop from city 0 to 3 is marked in red and has cost 100 + 600 = 700.
Note that the path through cities [0,1,2,3] is cheaper but is invalid because it uses 2 stops.

Example 2:
Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1
Output: 200
Explanation:
The graph is shown above.
The optimal path with at most 1 stop from city 0 to 2 is marked in red and has cost 100 + 100 = 200.

Example 3:
Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 0
Output: 500
Explanation:
The graph is shown above.
The optimal path with no stops from city 0 to 2 is marked in red and has cost 500.


Constraints:
1 <= n <= 100
0 <= flights.length <= (n * (n - 1) / 2)
flights[i].length == 3
0 <= fromi, toi < n
fromi != toi
1 <= pricei <= 10^4
There will not be any multiple flights between two cities.
0 <= src, dst, k < n
src != dst
"""
from typing import List


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        """
        动态规划
        dp[i][j] 表示从src中转i-1站到达城市j的最低花费。题目要求最多中转k站，dp[1][dst]表示不中转，从src直达dst的最低花费；
        dp[k+1][dst]表示从src中转k站到达dst的最低花费。最终结果为：min(dp[1][dst], ……, dp[k+1][dst])
        状态转移方程：dp[i][j] = min(dp[i-1][k] + prices[k][j])，即 只要城市k有到城市j的航班，就可以从dp[i-1][k]转移到dp[i][j]
        初始值：dp[0] 表示从src不执行任何航班到达城市j的最低花费，显然，只能到达城市src，花费为0；到达其它城市的花费设为float('inf')
        """
        # k < n, n <= 100, pricei <= 10^4。所以最大花费 (k+1) * pricei <= n * pricei <= 100 * 10^4 < 1000001
        dp = [[1000001] * n for _ in range(k + 2)]
        dp[0][src] = 0
        # 因为src != dst，所以dp[0][dst]=1000001
        res = dp[0][dst]
        for i in range(1, k + 2):
            for k, j, price in flights:
                dp[i][j] = min(dp[i][j], dp[i - 1][k] + price)
            res = min(res, dp[i][dst])
        return -1 if res == 1000001 else res

    def findCheapestPrice_2(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        """动态规划。优化方法一，利用滚动数组的思想降低空间复杂度"""
        dp = [1000001] * n
        dp[src] = 0
        # 因为src != dst，所以dp[dst]=1000001
        res = dp[dst]
        for i in range(1, k + 2):
            tmp = [1000001] * n
            for k, j, price in flights:
                tmp[j] = min(tmp[j], dp[k] + price)
            dp = tmp
            res = min(res, dp[dst])
        return -1 if res == 1000001 else res


if __name__ == '__main__':
    print(Solution().findCheapestPrice_2(n=4, flights=[[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]],
                                         src=0, dst=3, k=1))
