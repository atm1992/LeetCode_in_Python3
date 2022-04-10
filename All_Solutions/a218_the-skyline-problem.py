# -*- coding: UTF-8 -*-
"""
title: 天际线问题
A city's skyline is the outer contour of the silhouette formed by all the buildings in that city when viewed from a distance. Given the locations and heights of all the buildings, return the skyline formed by these buildings collectively.
The geometric information of each building is given in the array buildings where buildings[i] = [lefti, righti, heighti]:
    lefti is the x coordinate of the left edge of the ith building.
    righti is the x coordinate of the right edge of the ith building.
    heighti is the height of the ith building.
You may assume all buildings are perfect rectangles grounded on an absolutely flat surface at height 0.
The skyline should be represented as a list of "key points" sorted by their x-coordinate in the form [[x1,y1],[x2,y2],...]. Each key point is the left endpoint of some horizontal segment in the skyline except the last point in the list, which always has a y-coordinate 0 and is used to mark the skyline's termination where the rightmost building ends. Any ground between the leftmost and rightmost buildings should be part of the skyline's contour.
Note: There must be no consecutive horizontal lines of equal height in the output skyline. For instance, [...,[2 3],[4 5],[7 5],[11 5],[12 7],...] is not acceptable; the three lines of height 5 should be merged into one in the final output as such: [...,[2 3],[4 5],[12 7],...]


Example 1:
Input: buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
Output: [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]
Explanation:
Figure A shows the buildings of the input.
Figure B shows the skyline formed by those buildings. The red points in figure B represent the key points in the output list.

Example 2:
Input: buildings = [[0,2,3],[2,5,3]]
Output: [[0,3],[5,0]]


Constraints:
1 <= buildings.length <= 10^4
0 <= lefti < righti <= 2^31 - 1
1 <= heighti <= 2^31 - 1
buildings is sorted by lefti in non-decreasing order.
"""
import heapq
from typing import List


class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        """
        扫描线 + 优先队列。
        想象 一条竖线 从0到n-1的扫描所有building，使用优先队列来查找key point的最大高度。
        """
        res = []
        # 把所有building的左右边缘都放到一个数组中，升序
        boundaries = []
        for building in buildings:
            boundaries.append(building[0])
            boundaries.append(building[1])
        boundaries.sort()

        pq = []
        n = len(buildings)
        # 从0到n - 1 扫描所有building
        idx = 0
        # 只有boundary才有可能成为key point，计算与这条boundary相交的所有building的最大高度
        for boundary in boundaries:
            # 找到左边缘小于等于当前boundary的所有building，将它们的高度及右边缘加入优先队列(先按高度降序, 相等再按右边缘升序)
            # 因为buildings已经是按左边缘非降序排列的，所以可以直接 idx += 1 进行遍历
            while idx < n and buildings[idx][0] <= boundary:
                heapq.heappush(pq, (-buildings[idx][2], buildings[idx][1]))
                idx += 1
            # 从上面那些左边缘小于等于当前boundary的所有building中，找到右边缘大于boundary的那个building，它的高度为最大，因为使用了优先队列对高度降序
            while pq and pq[0][1] <= boundary:
                heapq.heappop(pq)
            max_height = -pq[0][0] if pq else 0
            # 若当前key point的高度等于上一个key point的高度，则无需加入res
            if not res or max_height != res[-1][1]:
                res.append([boundary, max_height])
        return res


if __name__ == '__main__':
    print(Solution().getSkyline([[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]))
