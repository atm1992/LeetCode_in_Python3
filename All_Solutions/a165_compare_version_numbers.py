# -*- coding: UTF-8 -*-
"""
title: 比较版本号
Given two version numbers, version1 and version2, compare them.
Version numbers consist of one or more revisions joined by a dot '.'. Each revision consists of digits and may contain leading zeros. Every revision contains at least one character. Revisions are 0-indexed from left to right, with the leftmost revision being revision 0, the next revision being revision 1, and so on. For example 2.5.33 and 0.1 are valid version numbers.
To compare version numbers, compare their revisions in left-to-right order. Revisions are compared using their integer value ignoring any leading zeros. This means that revisions 1 and 001 are considered equal. If a version number does not specify a revision at an index, then treat the revision as 0. For example, version 1.0 is less than version 1.1 because their revision 0s are the same, but their revision 1s are 0 and 1 respectively, and 0 < 1.
Return the following:
    If version1 < version2, return -1.
    If version1 > version2, return 1.
    Otherwise, return 0.


Example 1:
Input: version1 = "1.01", version2 = "1.001"
Output: 0
Explanation: Ignoring leading zeroes, both "01" and "001" represent the same integer "1".

Example 2:
Input: version1 = "1.0", version2 = "1.0.0"
Output: 0
Explanation: version1 does not specify revision 2, which means it is treated as "0".

Example 3:
Input: version1 = "0.1", version2 = "1.1"
Output: -1
Explanation: version1's revision 0 is "0", while version2's revision 0 is "1". 0 < 1, so version1 < version2.


Constraints:
1 <= version1.length, version2.length <= 500
version1 and version2 only contain digits and '.'.
version1 and version2 are valid version numbers.
All the given revisions in version1 and version2 can be stored in a 32-bit integer.
"""
from itertools import zip_longest


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = list(map(int, version1.split('.')))
        v2 = list(map(int, version2.split('.')))
        min_len = min(len(v1), len(v2))
        i = 0
        while i < min_len:
            if v1[i] > v2[i]:
                return 1
            elif v1[i] < v2[i]:
                return -1
            i += 1
        if sum(v1[i:]) > sum(v2[i:]):
            return 1
        elif sum(v1[i:]) < sum(v2[i:]):
            return -1
        else:
            return 0

    def compareVersion_2(self, version1: str, version2: str) -> int:
        for v1, v2 in zip_longest(version1.split('.'), version2.split('.'), fillvalue=0):
            v1, v2 = int(v1), int(v2)
            if v1 != v2:
                return 1 if v1 > v2 else -1
        return 0

    def compareVersion_3(self, version1: str, version2: str) -> int:
        """双指针。将空间复杂度降低为O(1)"""
        m, n = len(version1), len(version2)
        i, j = 0, 0
        while i < m or j < n:
            x = 0
            while i < m and version1[i] != '.':
                x = x * 10 + ord(version1[i]) - ord('0')
                i += 1
            # 跳过 '.'
            i += 1

            y = 0
            while j < n and version2[j] != '.':
                y = y * 10 + ord(version2[j]) - ord('0')
                j += 1
            # 跳过 '.'
            j += 1

            if x != y:
                return 1 if x > y else -1
        return 0


if __name__ == '__main__':
    print(Solution().compareVersion_2(version1="0.1", version2="1.1"))
