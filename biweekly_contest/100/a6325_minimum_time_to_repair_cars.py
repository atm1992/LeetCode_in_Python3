# -*- coding: UTF-8 -*-
"""
title: 修车的最少时间
You are given an integer array ranks representing the ranks of some mechanics. ranksi is the rank of the ith mechanic. A mechanic with a rank r can repair n cars in r * n^2 minutes.
You are also given an integer cars representing the total number of cars waiting in the garage to be repaired.
Return the minimum time taken to repair all the cars.
Note: All the mechanics can repair the cars simultaneously.


Example 1:
Input: ranks = [4,2,3,1], cars = 10
Output: 16
Explanation:
- The first mechanic will repair two cars. The time required is 4 * 2 * 2 = 16 minutes.
- The second mechanic will repair two cars. The time required is 2 * 2 * 2 = 8 minutes.
- The third mechanic will repair two cars. The time required is 3 * 2 * 2 = 12 minutes.
- The fourth mechanic will repair four cars. The time required is 1 * 4 * 4 = 16 minutes.
It can be proved that the cars cannot be repaired in less than 16 minutes.​​​​​

Example 2:
Input: ranks = [5,1,8], cars = 6
Output: 16
Explanation:
- The first mechanic will repair one car. The time required is 5 * 1 * 1 = 5 minutes.
- The second mechanic will repair four cars. The time required is 1 * 4 * 4 = 16 minutes.
- The third mechanic will repair one car. The time required is 8 * 1 * 1 = 8 minutes.
It can be proved that the cars cannot be repaired in less than 16 minutes.​​​​​


Constraints:
1 <= ranks.length <= 10^5
1 <= ranks[i] <= 100
1 <= cars <= 10^6
"""
import math
from collections import Counter
from typing import List


class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        """
        二分查找 + check
        因为若能在t分钟内修好所有汽车，则必然也能在t+1分钟内修好所有汽车。所以修车时间满足单调性
        假设最终结果为t，则 t 需要大于等于所有的 r * n^2，所以能力值为 r 的机械工最多可以修理 t/r 开根号 辆汽车
        """
        rank2cnt = Counter(ranks)

        def check(t: int) -> bool:
            total = 0
            for rank, cnt in rank2cnt.items():
                total += int(math.sqrt(t / rank)) * cnt
                if total >= cars:
                    return True
            return False

        # 最多就是让能力值最小的机械工修完所有的汽车
        left, right = 1, min(ranks) * cars * cars
        while left < right:
            mid = (left + right) // 2
            if check(mid):
                right = mid
            else:
                left = mid + 1
        return left


if __name__ == '__main__':
    print(Solution().repairCars(ranks=[4, 2, 3, 1], cars=10))
