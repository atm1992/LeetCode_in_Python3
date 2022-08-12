# -*- coding: UTF-8 -*-
"""
title: 坐上公交的最晚时间
You are given a 0-indexed integer array buses of length n, where buses[i] represents the departure time of the ith bus. You are also given a 0-indexed integer array passengers of length m, where passengers[j] represents the arrival time of the jth passenger. All bus departure times are unique. All passenger arrival times are unique.
You are given an integer capacity, which represents the maximum number of passengers that can get on each bus.
The passengers will get on the next available bus. You can get on a bus that will depart at x minutes if you arrive at y minutes where y <= x, and the bus is not full. Passengers with the earliest arrival times get on the bus first.
Return the latest time you may arrive at the bus station to catch a bus. You cannot arrive at the same time as another passenger.
Note: The arrays buses and passengers are not necessarily sorted.


Example 1:
Input: buses = [10,20], passengers = [2,17,18,19], capacity = 2
Output: 16
Explanation:
The 1st bus departs with the 1st passenger.
The 2nd bus departs with you and the 2nd passenger.
Note that you must not arrive at the same time as the passengers, which is why you must arrive before the 2nd passenger to catch the bus.

Example 2:
Input: buses = [20,30,10], passengers = [19,13,26,4,25,11,21], capacity = 2
Output: 20
Explanation:
The 1st bus departs with the 4th passenger.
The 2nd bus departs with the 6th and 2nd passengers.
The 3rd bus departs with the 1st passenger and you.


Constraints:
n == buses.length
m == passengers.length
1 <= n, m, capacity <= 10^5
2 <= buses[i], passengers[i] <= 10^9
Each element in buses is unique.
Each element in passengers is unique.
"""
from typing import List


class Solution:
    def latestTimeCatchTheBus(self, buses: List[int], passengers: List[int], capacity: int) -> int:
        """
        脑筋急转弯。
        若最后一班车还有空位，则上车时间为最后一班车的到达时间；这里是从最后一班车的到达时间开始往前找
        若没有空位，则从最后一位乘客的上车时间开始从后往前找，找到第一个空闲时间。
        无论是上述哪种情况，都需要从后往前找。哪怕最后一班车还有空位，但最后一位乘客的上车时间也有可能恰好就是最后一班车的到达时间，
        所以此时返回的结果不能是最后一班车的到达时间。
        因为题目给定 2 <= buses[i], passengers[i]，所以即使乘客把所有时间都占满了，也是有答案的，可以返回1
        """
        buses.sort()
        passengers.sort()
        m = len(passengers)
        j = 0
        # 用于之后判断最后一班车是否还有空位
        cnt = 0
        for bus in buses:
            cnt = 0
            while j < m and passengers[j] <= bus and cnt < capacity:
                j += 1
                cnt += 1
        j -= 1
        res = buses[-1] if cnt < capacity else passengers[j]
        while j >= 0 and passengers[j] == res:
            res -= 1
            j -= 1
        return res
