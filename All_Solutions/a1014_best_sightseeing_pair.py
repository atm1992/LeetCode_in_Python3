# -*- coding: UTF-8 -*-
"""
title: 最佳观光组合
You are given an integer array values where values[i] represents the value of the ith sightseeing spot. Two sightseeing spots i and j have a distance j - i between them.
The score of a pair (i < j) of sightseeing spots is values[i] + values[j] + i - j: the sum of the values of the sightseeing spots, minus the distance between them.
Return the maximum score of a pair of sightseeing spots.


Example 1:
Input: values = [8,1,5,2,6]
Output: 11
Explanation: i = 0, j = 2, values[i] + values[j] + i - j = 8 + 5 + 0 - 2 = 11

Example 2:
Input: values = [1,2]
Output: 2


Constraints:
2 <= values.length <= 5 * 10^4
1 <= values[i] <= 1000
"""
from typing import List


class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        """
        一次遍历
        从前往后遍历j，对于每个j，都找出最大的组合(i < j)得分值，这些组合得分值的最大值就是最终结果
        values[i] + values[j] + i - j = values[i] + i + values[j] - j
        其中，values[j] - j 对于每个j而言，是确定值。因此需要让values[i] + i尽可能大，
        在从前往后遍历j的过程中，可以使用一个变量max_i_score来记录当前最大的values[i] + i
        """
        res = max_i_score = 0
        for j in range(1, len(values)):
            max_i_score = max(max_i_score, values[j - 1] + j - 1)
            res = max(res, max_i_score + values[j] - j)
        return res


if __name__ == '__main__':
    print(Solution().maxScoreSightseeingPair([8, 1, 5, 2, 6]))
