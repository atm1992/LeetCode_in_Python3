# -*- coding: UTF-8 -*-
"""
title: 俄罗斯套娃信封问题
You are given a 2D array of integers envelopes where envelopes[i] = [wi, hi] represents the width and the height of an envelope.
One envelope can fit into another if and only if both the width and height of one envelope are greater than the other envelope's width and height.
Return the maximum number of envelopes you can Russian doll (i.e., put one inside the other).
Note: You cannot rotate an envelope.


Example 1:
Input: envelopes = [[5,4],[6,4],[6,7],[2,3]]
Output: 3
Explanation: The maximum number of envelopes you can Russian doll is 3 ([2,3] => [5,4] => [6,7]).

Example 2:
Input: envelopes = [[1,1],[1,1],[1,1]]
Output: 1


Constraints:
1 <= envelopes.length <= 10^5
envelopes[i].length == 2
1 <= wi, hi <= 10^5
"""
from typing import List


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        """
        排序 + 贪心 + 二分查找。参考LeetCode题300
        假设先将envelopes按w升序，不考虑w严格单调递增的问题，此时可将问题转化为LeetCode题300的计算h序列中最长递增子序列的长度。
        在本题中要求w、h都是严格单调递增的，因此对于w相等的多个h，最多只能选择其中一个，此时可以选择先将envelopes按w升序、再按h降序。
        这样一来，对于w相等的多个h，它们是降序排列的，在h序列中查找最长递增子序列时，后面的h不会对前面选择的h产生影响。
        例如：[[1,4],[1,3],[1,2],[2,4],[2,3]]，若选择了[1,4]，则后面的[1,3],[1,2]就不可能会被选择了。
        """
        envelopes.sort(key=lambda item: (item[0], -item[1]))
        # d[i] 是所有长度为i的递增子序列中，h值最小的元素。
        d = []
        for _, h in envelopes:
            if not d or d[-1] < h:
                d.append(h)
                continue
            left, right = 0, len(d) - 1
            # 二分查找第一个大于等于当前h的元素，然后用当前h替换该元素，目的是使数组d中的元素尽量小，从而使得数组d的长度尽量长
            while left < right:
                mid = (left + right) >> 1
                if d[mid] >= h:
                    right = mid
                else:
                    left = mid + 1
            d[left] = h
        return len(d)


if __name__ == '__main__':
    print(Solution().maxEnvelopes(envelopes=[[5, 4], [6, 4], [6, 7], [2, 3]]))
