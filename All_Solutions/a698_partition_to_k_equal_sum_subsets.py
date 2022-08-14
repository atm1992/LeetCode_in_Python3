# -*- coding: UTF-8 -*-
"""
title: 划分为k个相等的子集
Given an integer array nums and an integer k, return true if it is possible to divide this array into k non-empty subsets whose sums are all equal.


Example 1:
Input: nums = [4,3,2,3,5,2,1], k = 4
Output: true
Explanation: It is possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.

Example 2:
Input: nums = [1,2,3,4], k = 3
Output: false


Constraints:
1 <= k <= nums.length <= 16
1 <= nums[i] <= 10^4
The frequency of each element is in the range [1, 4].
"""
from typing import List


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        """
        状态压缩 + 动态规划。因为题目只是要求返回是否可以划分，没要求应该怎样划分，所以没必要用回溯。
        因为1 <= k <= nums.length <= 16，所以可使用状态压缩来表示一个集合。假设nums的长度为n，那么只需使用n位二进制就能表示nums中的哪些元素被选中了(相应的二进制位为1)
        总共需要使用 2^n 个整数(0 ~ 2^n - 1)来表示所有的元素选中状态，其中，0 表示nums中的所有元素均未被选中；2^n - 1 表示nums中的所有元素均被选中。
        最终返回结果就是nums中的所有元素均被选中时的dp值，即 dp[-1] or dp[2^n - 1]
        dp[i] = True 表示整数i对应的选数办法是合法的，该选数办法可以凑成若干个已完成的分组，和一个未完成的分组；
        """
        if k == 1:
            return True
        total = sum(nums)
        if total % k != 0:
            return False
        target = total // k
        nums.sort()
        if nums[-1] > target:
            return False
        n = len(nums)
        size = 1 << n
        dp = [False] * size
        # dp[0] 表示不选中任何元素，此时的cur_sum[0]自然也为0，自然小于target，所以是合法的
        dp[0] = True
        # cur_sum 与 dp 是对应的，dp 表示整数i对应的选数办法是否合法，cur_sum 表示整数i对应的所有选中元素的累加和，用于判断将当前元素nums[j]加入集合后，是否合法
        # 如果 (cur_sum[i] % target) + nums[j] 小于等于 target，则表示可以将当前元素nums[j]加入集合
        # cur_sum[i] // target 表示已完成的分组数，cur_sum[i] % target 表示最后那个未完成的分组当前已累加的和，如果把当前元素nums[j]加入该分组，
        # 使得该分组的累加和恰好等于target，则该结果肯定是合法的。如果加入nums[j]使该分组的累加和大于target，则说明nums[j]不符合要求，因为一个元素只能属于一个分组，不能一部分属于a分组，另一部分属于b分组；
        # 如果加入nums[j]使该分组的累加和小于target，则可先将该元素加入进来，然后继续遍历nums，寻找下一个元素，使得累加和等于target。
        # 遍历到dp[2^n - 1]时，意味着所有元素都加入到了分组，此时的cur_sum一定等于total
        cur_sum = [0] * size
        for i in range(size):
            # 总是基于 dp[i] = True 的前提进行状态转移
            if not dp[i]:
                continue
            # 对于每个值为True的dp[i]，都会遍历一次nums中的所有元素，然后更新i之后的各个next_i
            # 各个next_i都是只比i多选中一个元素。next_i、i 对应的二进制表示中1的个数才是当前选中了多少个元素。
            # 3 (0011)、12 (1100) 都是表示当前选中了2个元素，只是各自选中的那2个元素在nums中的下标不一样而已。
            for j in range(n):
                # 表示在整数i中，当前元素nums[j]已经被选中了
                if i & (1 << j):
                    continue
                # 表示在整数i对应的选数办法的基础上，加入当前元素nums[j]后，新的选数办法所对应的整数为next_i，毫无疑问，next_i 大于 i
                next_i = i | (1 << j)
                # 如果整数next_i对应的选数办法已经是合法的，那么就没必要再计算dp[next_i]了
                if dp[next_i]:
                    continue
                # 判断是否可以将当前元素nums[j]加入到整数i对应的选数办法中
                if (cur_sum[i] % target) + nums[j] <= target:
                    dp[next_i] = True
                    cur_sum[next_i] = cur_sum[i] + nums[j]
                else:
                    # 因为nums是升序排列，加上nums[j]都会大于target，那么加上后面的元素，更会大于target
                    break
        return dp[size - 1]

    def canPartitionKSubsets_2(self, nums: List[int], k: int) -> bool:
        """回溯 + 记忆化。上一个方法没法知道各个分组分别包含哪些元素"""
        if k == 1:
            return True
        total = sum(nums)
        if total % k != 0:
            return False
        target = total // k
        n = len(nums)
        nums.sort()
        partition = [0] * (k + 1)
        # 记忆化
        memo = {}

        def backtrack(start_idx: int, k: int, used_idxs: int, path: list) -> bool:
            if k == 0:
                # res.append(tuple(path))

                tmp_res = []
                for i in range(len(path)):
                    idxs = path[i] if i == 0 else path[i] ^ path[i - 1]
                    tmp = []
                    j = 0
                    while idxs:
                        if idxs & 1:
                            tmp.append(nums[j])
                        idxs >>= 1
                        j += 1
                    tmp_res.append(tmp)
                res.append(tuple(tmp_res))

                return True
            if used_idxs in memo:
                return memo[used_idxs]
            if partition[k] == target:
                memo[used_idxs] = backtrack(0, k - 1, used_idxs, path + [used_idxs])
                return memo[used_idxs]
            for i in range(start_idx, n):
                if used_idxs & (1 << i):
                    continue
                if partition[k] + nums[i] > target:
                    break
                partition[k] += nums[i]
                # 一旦找到一种可行的分组方案，就立即返回。若要查找所有方案，则将所有的return bool改为return None，并且这里不要return
                # 例如：nums=[4, 3, 1, 2, 5, 1], k=2，有两种方案：([1, 1, 2, 4], [3, 5]) or ([1, 3, 4], [1, 2, 5])
                if backtrack(i + 1, k, used_idxs | (1 << i), path):
                    return True
                partition[k] -= nums[i]
            return False

        res = []
        tmp = backtrack(0, k, 0, [])
        print(res)
        return tmp


if __name__ == '__main__':
    print(Solution().canPartitionKSubsets_2(nums=[4, 3, 1, 2, 5, 1], k=2))
