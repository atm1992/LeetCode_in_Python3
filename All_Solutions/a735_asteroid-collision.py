# -*- coding: UTF-8 -*-
"""
title: 行星碰撞
We are given an array asteroids of integers representing asteroids in a row.
For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.
Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.


Example 1:
Input: asteroids = [5,10,-5]
Output: [5,10]
Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.

Example 2:
Input: asteroids = [8,-8]
Output: []
Explanation: The 8 and -8 collide exploding each other.

Example 3:
Input: asteroids = [10,2,-5]
Output: [10]
Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.


Constraints:
2 <= asteroids.length <= 10^4
-1000 <= asteroids[i] <= 1000
asteroids[i] != 0
"""
from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        """栈"""
        res = []
        for item in asteroids:
            res.append(item)
            while len(res) >= 2 and res[-2] > 0 and res[-1] < 0:
                if res[-2] < -res[-1]:
                    tmp = res.pop()
                    res.pop()
                    res.append(tmp)
                elif res[-2] == -res[-1]:
                    res.pop()
                    res.pop()
                else:
                    res.pop()
        return res

    def asteroidCollision_2(self, asteroids: List[int]) -> List[int]:
        """栈。while …… else"""
        res = []
        for item in asteroids:
            while res and item < 0 < res[-1]:
                if res[-1] < -item:
                    res.pop()
                    continue
                elif res[-1] == -item:
                    res.pop()
                # break 之后不会再走下面的else
                break
            else:
                res.append(item)
        return res
