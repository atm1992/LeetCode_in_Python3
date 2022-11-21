# -*- coding: UTF-8 -*-
"""
title: 最低加油次数
A car travels from a starting position to a destination which is target miles east of the starting position.
There are gas stations along the way. The gas stations are represented as an array stations where stations[i] = [positioni, fueli] indicates that the ith gas station is positioni miles east of the starting position and has fueli liters of gas.
The car starts with an infinite tank of gas, which initially has startFuel liters of fuel in it. It uses one liter of gas per one mile that it drives. When the car reaches a gas station, it may stop and refuel, transferring all the gas from the station into the car.
Return the minimum number of refueling stops the car must make in order to reach its destination. If it cannot reach the destination, return -1.
Note that if the car reaches a gas station with 0 fuel left, the car can still refuel there. If the car reaches the destination with 0 fuel left, it is still considered to have arrived.


Example 1:
Input: target = 1, startFuel = 1, stations = []
Output: 0
Explanation: We can reach the target without refueling.

Example 2:
Input: target = 100, startFuel = 1, stations = [[10,100]]
Output: -1
Explanation: We can not reach the target (or even the first gas station).

Example 3:
Input: target = 100, startFuel = 10, stations = [[10,60],[20,30],[30,30],[60,40]]
Output: 2
Explanation: We start with 10 liters of fuel.
We drive to position 10, expending 10 liters of fuel.  We refuel from 0 liters to 60 liters of gas.
Then, we drive from position 10 to position 60 (expending 50 liters of fuel),
and refuel from 10 liters to 50 liters of gas.  We then drive to and reach the target.
We made 2 refueling stops along the way, so we return 2.


Constraints:
1 <= target, startFuel <= 10^9
0 <= stations.length <= 500
1 <= positioni < positioni+1 < target
1 <= fueli < 10^9
"""
import heapq
from typing import List


class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        """
        贪心 + 优先队列(最大堆)。使用优先队列(最大堆)记录所有已路过的加油站的油量，若当前的剩余油量不足以到达下一个加油站(或目的地)，
        则从优先队列(最大堆)中pop最大的油量，补充进当前的剩余油量，此时的加油次数加1，直到能够到达下一个加油站(或目的地)，否则返回 -1
        """
        n = len(stations)
        res, remain_fuel, pre_pos, queue = 0, startFuel, 0, []
        for i in range(n + 1):
            cur_pos = stations[i][0] if i < n else target
            remain_fuel -= cur_pos - pre_pos
            while remain_fuel < 0 and queue:
                # 补充当前的剩余油量。最大堆中使用的是负数
                remain_fuel += -heapq.heappop(queue)
                # 加油次数加1
                res += 1
            if remain_fuel < 0:
                return -1
            if i < n:
                heapq.heappush(queue, -stations[i][1])
                pre_pos = cur_pos
        return res


if __name__ == '__main__':
    print(Solution().minRefuelStops(target=100, startFuel=10, stations=[[10, 60], [20, 30], [30, 30], [60, 40]]))
