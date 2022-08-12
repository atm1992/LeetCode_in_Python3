# -*- coding: UTF-8 -*-
"""
title: 排列序列
The set [1, 2, 3, ..., n] contains a total of n! unique permutations.
By listing and labeling all of the permutations in order, we get the following sequence for n = 3:
"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.


Example 1:
Input: n = 3, k = 3
Output: "213"

Example 2:
Input: n = 4, k = 9
Output: "2314"

Example 3:
Input: n = 3, k = 1
Output: "123"


Constraints:
1 <= n <= 9
1 <= k <= n!
"""
from typing import List


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        """回溯。加上剪枝勉强通过，此题不适合用回溯"""

        def dfs(idx: int = 0, path: List[str] = []) -> None:
            nonlocal res, cnt
            if idx == n:
                cnt += 1
                if cnt == k:
                    res = ''.join(path)
                return
            for num in nums:
                if num in path:
                    continue
                path.append(num)
                dfs(idx + 1, path)
                path.pop(-1)
                if cnt == k:
                    return

        nums = [str(i) for i in range(1, n + 1)]
        res, cnt = '', 0
        dfs()
        return res

    def getPermutation_2(self, n: int, k: int) -> str:
        """数学 + 缩小问题规模。
        1~n 总共有n个元素，总共会有n!种排列，而其中每个元素作为排列的第一个元素a1，分别会有(n-1)!种。
        即第1 ~ (n-1)!种，是以1开头的；第(n-1)!+1 ~ 2*(n-1)!种，是以2开头的；…… 。k 的取值范围为1 ~ n!
        然后以1开头的这(n-1)!种之中，第二个元素a2为2的有(n-2)!种，即第1 ~ (n-2)!种；…… 。
        为方便计算，将上述范围都减1，即 k 的取值范围变为0 ~ n!-1，排列以1开头的范围变为0 ~ (n-1)!-1，它们整除(n-1)!的结果都为0；
        排列以2开头的范围变为(n-1)! ~ 2*(n-1)!-1，它们整除(n-1)!的结果都为1；…… 。因此，可通过 k // (n-1)! 来确定a1在nums中的下标，
        确定了以后，将该值从nums中pop掉，k %= (n-1)!。
        同理，可通过 k // (n-2)! 来确定a2在nums中的下标；…… 。"""
        # 0的阶乘为1。数组factorial将会记录0 ~ n-1的阶乘，总共n个元素
        factorial = [1]
        for i in range(1, n):
            factorial.append(factorial[i - 1] * i)

        k -= 1
        nums = [str(i) for i in range(1, n + 1)]
        res = ''
        # 依次确定a1、a2、……、an的值
        for i in range(1, n + 1):
            idx = k // factorial[n - i]
            res += nums.pop(idx)
            k %= factorial[n - i]
        return res


if __name__ == '__main__':
    print(Solution().getPermutation_2(n=4, k=9))
