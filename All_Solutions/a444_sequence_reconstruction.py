# -*- coding: UTF-8 -*-
"""
title: 序列重建
You are given an integer array nums of length n where nums is a permutation of the integers in the range [1, n]. You are also given a 2D integer array sequences where sequences[i] is a subsequence of nums.
Check if nums is the shortest possible and the only supersequence. The shortest supersequence is a sequence with the shortest length and has all sequences[i] as subsequences. There could be multiple valid supersequences for the given array sequences.
    For example, for sequences = [[1,2],[1,3]], there are two shortest supersequences, [1,2,3] and [1,3,2].
    While for sequences = [[1,2],[1,3],[1,2,3]], the only shortest supersequence possible is [1,2,3]. [1,2,3,4] is a possible supersequence but not the shortest.
Return true if nums is the only shortest supersequence for sequences, or false otherwise.
A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.


Example 1:
Input: nums = [1,2,3], sequences = [[1,2],[1,3]]
Output: false
Explanation: There are two possible supersequences: [1,2,3] and [1,3,2].
The sequence [1,2] is a subsequence of both: [1,2,3] and [1,3,2].
The sequence [1,3] is a subsequence of both: [1,2,3] and [1,3,2].
Since nums is not the only shortest supersequence, we return false.

Example 2:
Input: nums = [1,2,3], sequences = [[1,2]]
Output: false
Explanation: The shortest possible supersequence is [1,2].
The sequence [1,2] is a subsequence of it: [1,2].
Since nums is not the shortest supersequence, we return false.

Example 3:
Input: nums = [1,2,3], sequences = [[1,2],[1,3],[2,3]]
Output: true
Explanation: The shortest possible supersequence is [1,2,3].
The sequence [1,2] is a subsequence of it: [1,2,3].
The sequence [1,3] is a subsequence of it: [1,2,3].
The sequence [2,3] is a subsequence of it: [1,2,3].
Since nums is the only shortest supersequence, we return true.


Constraints:
n == nums.length
1 <= n <= 10^4
nums is a permutation of all the integers in the range [1, n].
1 <= sequences.length <= 10^4
1 <= sequences[i].length <= 10^4
1 <= sum(sequences[i].length) <= 10^5
1 <= sequences[i][j] <= n
All the arrays of sequences are unique.
sequences[i] is a subsequence of nums.
"""
from typing import List


class Solution:
    def sequenceReconstruction(self, nums: List[int], sequences: List[List[int]]) -> bool:
        """拓扑排序 + BFS"""
        n = len(nums)
        graph = [[] for _ in range(n + 1)]
        in_degree = [0] * (n + 1)
        for s in sequences:
            pre = s[0]
            for cur in s[1:]:
                graph[pre].append(cur)
                in_degree[cur] += 1
                pre = cur
        # 若nums中的元素个数比sequences中出现的元素个数多，则多出来的那些元素，它们的入度为0。若存在多个入度为0的节点，则下面会返回False
        queue = [i for i in range(1, n + 1) if in_degree[i] == 0]
        # BFS的起始节点有且只能有一个，否则拓扑序列就不是唯一的
        if len(queue) != 1:
            return False
        idx = 0
        for u in queue:
            # 若nums中的元素个数比sequences中出现的元素个数少，则这里会返回False
            if not (idx < n and nums[idx] == u):
                return False
            idx += 1
            next_cnt = 0
            for v in graph[u]:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    queue.append(v)
                    next_cnt += 1
                    # 若当前节点u的下一层节点存在多个，则拓扑序列不唯一
                    if next_cnt > 1:
                        return False
        return True
