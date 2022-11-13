# -*- coding: UTF-8 -*-
"""
title: 不同整数的最少数目
Given an array of integers arr and an integer k. Find the least number of unique integers after removing exactly k elements.


Example 1:
Input: arr = [5,5,4], k = 1
Output: 1
Explanation: Remove the single 4, only 5 is left.
Example 2:
Input: arr = [4,3,1,1,3,3,2], k = 3
Output: 2
Explanation: Remove 4, 2 and either one of the two 1s or three 3s. 1 and 3 will be left.


Constraints:
1 <= arr.length <= 10^5
1 <= arr[i] <= 10^9
0 <= k <= arr.length
"""
from collections import Counter
from typing import List


class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        """排序 + 贪心。优先删除出现次数少的数字"""
        cnts = sorted(Counter(arr).values())
        for i, cnt in enumerate(cnts):
            k -= cnt
            if k < 0:
                return len(cnts) - i
            elif k == 0:
                return len(cnts) - i - 1


if __name__ == '__main__':
    print(Solution().findLeastNumOfUniqueInts(arr=[4, 3, 1, 1, 3, 3, 2], k=3))
