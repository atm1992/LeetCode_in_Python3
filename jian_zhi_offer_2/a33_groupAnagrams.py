# -*- coding: UTF-8 -*-
"""
title: 变位词组
给定一个字符串数组 strs ，将 变位词 组合在一起。 可以按任意顺序返回结果列表。
注意：若两个字符串中每个字符出现的次数都相同，则称它们互为变位词。


示例 1:
输入: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
输出: [["bat"],["nat","tan"],["ate","eat","tea"]]

示例 2:
输入: strs = [""]
输出: [[""]]

示例 3:
输入: strs = ["a"]
输出: [["a"]]


提示：
1 <= strs.length <= 10^4
0 <= strs[i].length <= 100
strs[i] 仅包含小写字母
"""
from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """排序"""
        str2group = defaultdict(list)
        for s in strs:
            str2group[''.join(sorted(s))].append(s)
        return list(str2group.values())

    def groupAnagrams_2(self, strs: List[str]) -> List[List[str]]:
        """计数"""
        str2group = defaultdict(list)
        for s in strs:
            cnt = [0] * 26
            for ch in s:
                cnt[ord(ch) - ord('a')] += 1
            str2group[tuple(cnt)].append(s)
        return list(str2group.values())


if __name__ == '__main__':
    print(Solution().groupAnagrams(["a"]))
