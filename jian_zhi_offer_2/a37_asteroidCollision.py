# -*- coding: UTF-8 -*-
"""
title: 小行星碰撞
给定一个整数数组 asteroids，表示在同一行的小行星。
对于数组中的每一个元素，其绝对值表示小行星的大小，正负表示小行星的移动方向（正表示向右移动，负表示向左移动）。每一颗小行星以相同的速度移动。
找出碰撞后剩下的所有小行星。碰撞规则：两个行星相互碰撞，较小的行星会爆炸。如果两颗行星大小相同，则两颗行星都会爆炸。两颗移动方向相同的行星，永远不会发生碰撞。


示例 1：
输入：asteroids = [5,10,-5]
输出：[5,10]
解释：10 和 -5 碰撞后只剩下 10 。 5 和 10 永远不会发生碰撞。

示例 2：
输入：asteroids = [8,-8]
输出：[]
解释：8 和 -8 碰撞后，两者都发生爆炸。

示例 3：
输入：asteroids = [10,2,-5]
输出：[10]
解释：2 和 -5 发生碰撞后剩下 -5 。10 和 -5 发生碰撞后剩下 10 。

示例 4：
输入：asteroids = [-2,-1,1,2]
输出：[-2,-1,1,2]
解释：-2 和 -1 向左移动，而 1 和 2 向右移动。 由于移动方向相同的行星不会发生碰撞，所以最终没有行星发生碰撞。


提示：
2 <= asteroids.length <= 10^4
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


if __name__ == '__main__':
    print(Solution().asteroidCollision([-2, -1, 1, 2]))
