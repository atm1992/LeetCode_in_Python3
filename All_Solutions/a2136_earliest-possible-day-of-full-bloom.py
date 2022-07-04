# -*- coding: UTF-8 -*-
"""
title: 全部开花的最早一天
You have n flower seeds. Every seed must be planted first before it can begin to grow, then bloom. Planting a seed takes time and so does the growth of a seed. You are given two 0-indexed integer arrays plantTime and growTime, of length n each:
    plantTime[i] is the number of full days it takes you to plant the ith seed. Every day, you can work on planting exactly one seed. You do not have to work on planting the same seed on consecutive days, but the planting of a seed is not complete until you have worked plantTime[i] days on planting it in total.
    growTime[i] is the number of full days it takes the ith seed to grow after being completely planted. After the last day of its growth, the flower blooms and stays bloomed forever.
From the beginning of day 0, you can plant the seeds in any order.
Return the earliest possible day where all seeds are blooming.


Example 1:
Input: plantTime = [1,4,3], growTime = [2,3,1]
Output: 9
Explanation: The grayed out pots represent planting days, colored pots represent growing days, and the flower represents the day it blooms.
One optimal way is:
On day 0, plant the 0th seed. The seed grows for 2 full days and blooms on day 3.
On days 1, 2, 3, and 4, plant the 1st seed. The seed grows for 3 full days and blooms on day 8.
On days 5, 6, and 7, plant the 2nd seed. The seed grows for 1 full day and blooms on day 9.
Thus, on day 9, all the seeds are blooming.

Example 2:
Input: plantTime = [1,2,3,2], growTime = [2,1,2,1]
Output: 9
Explanation: The grayed out pots represent planting days, colored pots represent growing days, and the flower represents the day it blooms.
One optimal way is:
On day 1, plant the 0th seed. The seed grows for 2 full days and blooms on day 4.
On days 0 and 3, plant the 1st seed. The seed grows for 1 full day and blooms on day 5.
On days 2, 4, and 5, plant the 2nd seed. The seed grows for 2 full days and blooms on day 8.
On days 6 and 7, plant the 3rd seed. The seed grows for 1 full day and blooms on day 9.
Thus, on day 9, all the seeds are blooming.

Example 3:
Input: plantTime = [1], growTime = [1]
Output: 2
Explanation: On day 0, plant the 0th seed. The seed grows for 1 full day and blooms on day 2.
Thus, on day 2, all the seeds are blooming.


Constraints:
n == plantTime.length == growTime.length
1 <= n <= 10^5
1 <= plantTime[i], growTime[i] <= 10^4
"""
from functools import cmp_to_key
from typing import List


class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        """
        贪心
        假设有两颗种子1、2，播种所需天数分别为p1、p2，生长所需天数分别为g1、g2.
        对比 播种完1再播种2、播种完2再播种1、 交叉播种1/2 这3种方式：
        1、播种完1再播种2：播种完1的时间为第p1天，播种完2的时间为第p1 + p2天
        2、播种完2再播种1：播种完2的时间为第p2天，播种完1的时间为第p1 + p2天
        3、交叉播种1/2：交叉播种也有个播种完成时间的先后顺序，要么是1先播种完，要么是2先播种完
            3.1、1先播种完：播种完1的时间范围：[p1 + 1, p1 + p2 - 1]，播种完2的时间为第p1 + p2天
            3.2、2先播种完：播种完2的时间范围：[p2 + 1, p1 + p2 - 1]，播种完1的时间为第p1 + p2天
        由上可知，无论采用哪种播种方式，总的最短播种耗时都是p1 + p2天
        播种完1再播种2 优于 交叉播种1/2(1先播种完)，因为对于1来说，前一种方式可以留有更多的时间来生长
        播种完2再播种1 优于 交叉播种1/2(2先播种完)，因为对于2来说，前一种方式可以留有更多的时间来生长
        至于选择 播种完1再播种2 还是 播种完2再播种1，需要对比g1、g2
        若 g1 >= g2，则：
        情况一、播种完1再播种2 的最晚开花时间：max(p1 + g1, p1 + p2 + g2)
        情况二、播种完2再播种1 的最晚开花时间：max(p2 + g2, p2 + p1 + g1)
        对于情况二来说，因为 g1 >= g2、1 <= plantTime[i], growTime[i]，所以 p2 + g2 <= p2 + g1 < p2 + p1 + g1，即 max(p2 + g2, p2 + p1 + g1) = p2 + p1 + g1
        对于情况一来说，因为 p1 + g1 < p1 + p2 + g1, p1 + p2 + g2 <= p1 + p2 + g1，所以 max(p1 + g1, p1 + p2 + g2) <= p1 + p2 + g1 = max(p2 + g2, p2 + p1 + g1)
        也就意味着，g1 >= g2 时，播种完1再播种2的最终耗时 <= 播种完2再播种1的最终耗时。当且仅当 g1 == g2 时，上式中的等号成立
        同理可以证明，g1 < g2 时，播种完1再播种2的最终耗时 > 播种完2再播种1的最终耗时。
        所以，最终结论为：最终耗时与播种所需天数无关，仅取决于生长所需天数，并且生长所需天数越长的，需要越先播种。
        """

        def cmp(i: int, j: int) -> int:
            """
            自定义排序。
            若要实现升序，则在i<j时返回负数(通常用-1表示)；i==j时返回0；i>j时返回正数(通常用1表示)。
            若要实现降序，则在i<j时返回正数(通常用1表示)；i==j时返回0；i>j时返回负数(通常用-1表示)。
            """
            # 实现了对growTime降序，因为growTime[i]、growTime[j]都是int，所以可以直接返回相减结果。若要实现升序，则 return growTime[i] - growTime[j]
            return growTime[j] - growTime[i]

        idxs = list(range(len(plantTime)))
        idxs.sort(key=cmp_to_key(cmp))
        plant_day = res = 0
        for i in idxs:
            plant_day += plantTime[i]
            res = max(res, plant_day + growTime[i])
        return res

    def earliestFullBloom_2(self, plantTime: List[int], growTime: List[int]) -> int:
        plant_day = res = 0
        for plant, grow in sorted(zip(plantTime, growTime), key=lambda x: -x[1]):
            plant_day += plant
            res = max(res, plant_day + grow)
        return res
