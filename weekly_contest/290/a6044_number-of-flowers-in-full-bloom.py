# -*- coding: UTF-8 -*-
"""
title: 花期内花的数目
You are given a 0-indexed 2D integer array flowers, where flowers[i] = [starti, endi] means the ith flower will be in full bloom from starti to endi (inclusive). You are also given a 0-indexed integer array persons of size n, where persons[i] is the time that the ith person will arrive to see the flowers.
Return an integer array answer of size n, where answer[i] is the number of flowers that are in full bloom when the ith person arrives.


Example 1:
Input: flowers = [[1,6],[3,7],[9,12],[4,13]], persons = [2,3,7,11]
Output: [1,2,2,2]
Explanation: The figure above shows the times when the flowers are in full bloom and when the people arrive.
For each person, we return the number of flowers in full bloom during their arrival.

Example 2:
Input: flowers = [[1,10],[3,3]], persons = [3,3,2]
Output: [2,2,1]
Explanation: The figure above shows the times when the flowers are in full bloom and when the people arrive.
For each person, we return the number of flowers in full bloom during their arrival.


Constraints:
1 <= flowers.length <= 5 * 10^4
flowers[i].length == 2
1 <= starti <= endi <= 10^9
1 <= persons.length <= 5 * 10^4
1 <= persons[i] <= 10^9
"""
from typing import List


class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], persons: List[int]) -> List[int]:
        flowers_and_persons = []
        n = len(persons)
        for start, end in flowers:
            # 假设对于时间点t，某朵花start，另一朵花end，同时某个person正好过来，那么这个person是可以看到这两朵花的。
            # 所以 -1 < 0 ~ n-1 < n，sort() 先按第一个字段升序，第一个字段相同的情况下，会再按第二个字段升序
            flowers_and_persons.append((start, -1))
            flowers_and_persons.append((end, n))
        for idx, val in enumerate(persons):
            flowers_and_persons.append((val, idx))
        flowers_and_persons.sort()
        res = [0] * n
        # 统计当前有多少朵花正在开放
        cur = 0
        for _, flag in flowers_and_persons:
            if flag == -1:
                cur += 1
            elif flag == n:
                # 一朵花只有先开放，才能再凋谢，所以cur不可能为负数
                cur -= 1
            else:
                res[flag] = cur
        return res


if __name__ == '__main__':
    print(Solution().fullBloomFlowers(flowers=[[1, 6], [3, 7], [9, 12], [4, 13]], persons=[2, 3, 7, 11]))
