# -*- coding: UTF-8 -*-
"""
title: 字母与数字
Given an array filled with letters and numbers, find the longest subarray with an equal number of letters and numbers.
Return the subarray. If there are more than one answer, return the one which has the smallest index of its left endpoint. If there is no answer, return an empty arrary.


Example 1:
Input: ["A","1","B","C","D","2","3","4","E","5","F","G","6","7","H","I","J","K","L","M"]
Output: ["A","1","B","C","D","2","3","4","E","5","F","G","6","7"]

Example 2:
Input: ["A","A"]
Output: []


Note:
array.length <= 100000
"""
from typing import List


class Solution:
    def findLongestSubarray(self, array: List[str]) -> List[str]:
        """前缀和 + 哈希表"""
        cur_sum, sum2idx = 0, {0: 0}
        start = end = 0
        for i, ch in enumerate(array, 1):
            cur_sum += 1 if ch.isdigit() else -1
            if cur_sum in sum2idx:
                if i - sum2idx[cur_sum] > end - start:
                    start, end = sum2idx[cur_sum], i
            else:
                sum2idx[cur_sum] = i
        return array[start: end]


if __name__ == '__main__':
    print(Solution().findLongestSubarray(
        ["A", "1", "B", "C", "D", "2", "3", "4", "E", "5", "F", "G", "6", "7", "H", "I", "J", "K", "L", "M"]))
