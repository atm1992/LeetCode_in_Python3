# -*- coding: UTF-8 -*-
"""
title: 字符串的排列
输入一个字符串，打印出该字符串中字符的所有排列。
你可以以任意顺序返回这个字符串数组，但里面不能有重复元素。


示例:
输入：s = "abc"
输出：["abc","acb","bac","bca","cab","cba"]


限制：
1 <= s 的长度 <= 8
"""
from typing import List


class Solution:
    def permutation(self, s: str) -> List[str]:
        """回溯"""

        def backtrack(cnt: int = 0, path: List[str] = []) -> None:
            if cnt == n:
                res.append(''.join(path))
                return
            for i in range(n):
                # 若当前字符与上个字符相同，并且上个字符还没被使用，则当前字符也不能被使用。
                # 对于相同的多个字符，必须先使用前面的，只有在前面的都被使用了之后，才允许使用下一个
                if visited[i] or (i > 0 and ch_sorted[i] == ch_sorted[i - 1] and not visited[i - 1]):
                    continue
                visited[i] = True
                path.append(ch_sorted[i])
                backtrack(cnt + 1, path)
                path.pop()
                visited[i] = False

        n = len(s)
        ch_sorted = sorted(s)
        # 标记ch_sorted中的每个字符是否被使用过。因为字符可能重复，所以不能用哈希表
        visited = [False] * n
        res = []
        backtrack()
        return res

    def permutation_2(self, s: str) -> List[str]:
        """不断计算下一个更大的排列，直到不存在更大的排列为止，参考LeetCode题 31。此方法不需要考虑去重问题"""

        def next_permutation(ch_sorted: List[str]) -> bool:
            # 从倒数第二个字符开始往前遍历ch_sorted
            i = n - 2
            # 找到第一个i，满足 ch_sorted[i] < ch_sorted[i + 1]
            while i >= 0 and ch_sorted[i] >= ch_sorted[i + 1]:
                i -= 1
            if i < 0:
                return False
            j = n - 1
            # 找到第一个大于ch_sorted[i]的字符，由上可知，ch_sorted[i + 1] 一定符合要求，所以j >= i+1
            while j >= i + 1 and ch_sorted[i] >= ch_sorted[j]:
                j -= 1
            ch_sorted[i], ch_sorted[j] = ch_sorted[j], ch_sorted[i]
            start, end = i + 1, n - 1
            # 对 [start, end] 范围内的字符反转
            while start < end:
                ch_sorted[start], ch_sorted[end] = ch_sorted[end], ch_sorted[start]
                start += 1
                end -= 1
            return True

        n = len(s)
        ch_sorted = sorted(s)
        # 初始时的排列，是最小的排列，所有字符均升序。之后不断对ch_sorted进行重排序
        res = [''.join(ch_sorted)]
        # 最大的排列为所有字符均降序
        while next_permutation(ch_sorted):
            res.append(''.join(ch_sorted))
        return res


if __name__ == '__main__':
    print(Solution().permutation_2('abcde'))
