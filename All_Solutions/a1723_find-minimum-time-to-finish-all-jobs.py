# -*- coding: UTF-8 -*-
"""
title: 完成所有工作的最短时间
You are given an integer array jobs, where jobs[i] is the amount of time it takes to complete the ith job.
There are k workers that you can assign jobs to. Each job should be assigned to exactly one worker. The working time of a worker is the sum of the time it takes to complete all jobs assigned to them. Your goal is to devise an optimal assignment such that the maximum working time of any worker is minimized.
Return the minimum possible maximum working time of any assignment.


Example 1:
Input: jobs = [3,2,3], k = 3
Output: 3
Explanation: By assigning each person one job, the maximum time is 3.

Example 2:
Input: jobs = [1,2,4,7,8], k = 2
Output: 11
Explanation: Assign the jobs the following way:
Worker 1: 1, 2, 8 (working time = 1 + 2 + 8 = 11)
Worker 2: 4, 7 (working time = 4 + 7 = 11)
The maximum working time is 11.


Constraints:
1 <= k <= jobs.length <= 12
1 <= jobs[i] <= 10^7
"""
from typing import List


class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        """二分查找 + 回溯 + 剪枝。推荐使用此方法"""

        def backtrack(workloads: List[int], i: int, limit: int) -> bool:
            """递归地枚举第i个job的分配方案，在此过程中，实时更新workloads数组。每个工人最多可以分配的工作量为limit"""
            if i == n:
                return True
            cur_job = jobs[i]
            for j in range(k):
                if workloads[j] + cur_job <= limit:
                    workloads[j] += cur_job
                    if backtrack(workloads, i + 1, limit):
                        return True
                    # 若上面返回False，则进行回溯。把cur_job分配给下一个工人
                    workloads[j] -= cur_job
                # 剪枝条件1：
                #   因为是从0 ~ k-1给工人分配工作，如果第j个工人没有被分配工作，那么之后的工人肯定也没被分配工作，第j个工人在工作量为0的情况下，都无法完成cur_job，则之后的工人肯定也无法完成cur_job。
                # 剪枝条件2：            这个剪枝条件不写，其实也能通过
                #   如果第j个工人当前的工作量加上cur_job恰好等于limit，但后续的工人无法完成分配，backtrack返回False，那么后续的工人也无需再去尝试分配cur_job了，
                #   因为如果把当前的cur_job分配给后续某个工人后，最终能够返回True，那么说明给第j个工人分配了一个小于等于当前cur_job的job组合（注意：不一定是一个job，但是这些job的组合一定小于等于当前cur_job，因为必须小于等于limit），
                #   既然给第j个工人分配一个更小的job组合(剩余的job总和更大)能返回True，那为什么分配一个恰好合适的job(剩余的job总和更小)却会返回False，所以说明把当前的cur_job分配给后续某个工人，不可能返回True。
                # 为什么workloads[j] + cur_job < limit时，允许回溯？
                #   因为一个cur_job无法把workloads[j]填满，导致剩余的job总和无法被完全分配，然而workloads[j] + cur_job之后，workloads[j]还有些剩余空间，这部分空间没有被有效利用，
                #   所以需要通过回溯的方式来使用之后多个小的job来填满workloads[j]，虽然之后的job越来越小，单个job肯定无法填满workloads[j]，但是，多个小job还是有可能把workloads[j]填满的，从而减小剩余的job总和。
                if workloads[j] == 0 or workloads[j] + cur_job == limit:
                    break
            return False

        n = len(jobs)
        # 优先分配工作量大的工作
        jobs.sort(reverse=True)
        total = sum(jobs)
        left, right = max(jobs[0], total // k), total
        while left < right:
            mid = (left + right) // 2
            # 记录k个工人实时被分配的工作量
            workloads = [0] * k
            # 每次都是从第0个job开始分配
            if backtrack(workloads, 0, mid):
                right = mid
            else:
                left = mid + 1
        return left

    def minimumTimeRequired_2(self, jobs: List[int], k: int) -> int:
        """动态规划 + 状态压缩。注意：Python会运行超时，Java、C++ 能通过，主要是学习这种思想"""

        def get_first_1_idx(i: int) -> int:
            res = 0
            while i & 1 == 0:
                res += 1
                i >>= 1
            return res

        # 因为jobs.length <= 12，所以最多有 2^12 = 4096种状态，可用一个11位的二进制数(int数)来表示各种状态
        # 例如：10010 表示第1、4(0 ~ n-1)个job已被分配出去
        state_cnt = 1 << len(jobs)
        workloads = [0] * state_cnt
        # 状态0的总工作量为0，无需计算。计算各种状态下的总工作量
        for i in range(1, state_cnt):
            base, idx = i & (i - 1), get_first_1_idx(i)
            workloads[i] = workloads[base] + jobs[idx]
        # dp[i][j] 表示给前i个工人分配完工作，工作的分配状态为j，完成这些已分配工作的最短时间
        # dp[k-1][state_cnt-1] 即为最终结果，表示完成所有工作的最短时间
        # dp[0] 表示1个工人完成各种状态的最短时间，其实就是workloads
        dp = [workloads] + [[0] * state_cnt for _ in range(k - 1)]
        for i in range(1, k):
            # 状态0表示没有工作可分配，所以无论几个工人去完成，最短时间均为0
            for j in range(1, state_cnt):
                # dp[i-1][j] 表示将所有工作都分配给前i-1个工人，不给第i个工人分配任何工作。即 max(dp[i-1][j], 0)
                tmp = dp[i - 1][j]
                # 枚举状态j的所有子状态k，从所有工作均分配给第i个工人 到 不给第i个工人分配任何工作。剩余子集(状态j - 状态k)分配给前i-1个工人
                k = j
                while k:
                    tmp = min(tmp, max(dp[i - 1][j - k], workloads[k]))
                    # 注意：这里是 j & (k-1)，而不是 k & (k-1)。k & (k-1) 并不能枚举完所有的子状态
                    # 以 j = 6 为例，k的取值分别为：
                    # j & (k-1)：6(110)、4(100)、2(010)
                    # k & (k-1)：6(110)、4(100)
                    k = j & (k - 1)
                dp[i][j] = tmp
        return dp[-1][-1]

    def minimumTimeRequired_3(self, jobs: List[int], k: int) -> int:
        """动态规划 + 状态压缩。在方法二的基础上，使用一维滚动数组代替二维dp数组。
        注意：Python会运行超时，Java、C++ 能通过，主要是学习这种思想"""

        def get_first_1_idx(i: int) -> int:
            res = 0
            while i & 1 == 0:
                res += 1
                i >>= 1
            return res

        # 因为jobs.length <= 12，所以最多有 2^12 = 4096种状态，可用一个11位的二进制数(int数)来表示各种状态
        # 例如：10010 表示第1、4(0 ~ n-1)个job已被分配出去
        state_cnt = 1 << len(jobs)
        workloads = [0] * state_cnt
        # 状态0的总工作量为0，无需计算。计算各种状态下的总工作量
        for i in range(1, state_cnt):
            base, idx = i & (i - 1), get_first_1_idx(i)
            workloads[i] = workloads[base] + jobs[idx]
        dp = workloads.copy()
        for _ in range(1, k):
            for j in range(state_cnt - 1, 0, -1):
                k = j
                while k:
                    dp[j] = min(dp[j], max(dp[j - k], workloads[k]))
                    k = j & (k - 1)
        return dp[-1]
