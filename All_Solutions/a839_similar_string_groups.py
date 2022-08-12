# -*- coding: UTF-8 -*-
"""
title: 相似字符串组
Two strings X and Y are similar if we can swap two letters (in different positions) of X, so that it equals Y. Also two strings X and Y are similar if they are equal.
For example, "tars" and "rats" are similar (swapping at positions 0 and 2), and "rats" and "arts" are similar, but "star" is not similar to "tars", "rats", or "arts".
Together, these form two connected groups by similarity: {"tars", "rats", "arts"} and {"star"}.  Notice that "tars" and "arts" are in the same group even though they are not similar.  Formally, each group is such that a word is in the group if and only if it is similar to at least one other word in the group.
We are given a list strs of strings where every string in strs is an anagram of every other string in strs. How many groups are there?


Example 1:
Input: strs = ["tars","rats","arts","star"]
Output: 2

Example 2:
Input: strs = ["omv","ovm"]
Output: 1


Constraints:
1 <= strs.length <= 300
1 <= strs[i].length <= 300
strs[i] consists of lowercase letters only.
All words in strs have the same length and are anagrams of each other.
"""
from typing import List


class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        """并查集。将每个字符串看作是一个节点，若两个字符串相似，则认为这两个节点之间存在一条边"""

        def find_father(i: int) -> int:
            """查找输入节点的根节点"""
            # 只有根节点的父节点才为本身
            if i != father[i]:
                father[i] = find_father(father[i])
            return father[i]

        def check(a: str, b: str) -> bool:
            """检验两个字符串是否相似"""
            diff_cnt = 0
            for ch_a, ch_b in zip(a, b):
                if ch_a != ch_b:
                    diff_cnt += 1
                    # 题目已知：strs 中的所有单词都具有相同的长度，且是彼此的字母异位词。如果两个字符串本身是相等的，那它们也是相似的。
                    # 由于a、b这两个字符串的字符集是一样的，所以如果某个下标的字符不一样，那么一定会使得其它某个或某几个下标的字符也不一样。
                    # a、b这两个字符串相等的话，则diff_cnt == 0；不相等的话，则diff_cnt一定大于等于2，不可能会等于1
                    # diff_cnt 是有可能为奇数的。例如：'this' 与 'shti'的diff_cnt为3
                    # 只有当diff_cnt为0或2时，两个字符串才是相似的
                    if diff_cnt > 2:
                        return False
            return True

        n = len(strs)
        # 初始时，认为各个节点的父节点(根节点)为本身。通常命名为 father or parent
        father = list(range(n))
        for i in range(n - 1):
            for j in range(i + 1, n):
                # 注意：i_root = find_father(i) 这行代码不能写在当前for循环的外边，因为在当前for循环中会动态修改i的根节点，
                # 若写在当前for循环的外边，则i_root就变成静态的了
                i_root = find_father(i)
                j_root = find_father(j)
                if i_root == j_root:
                    continue
                # check & union
                if check(strs[i], strs[j]):
                    father[i_root] = j_root
        return sum(i == father[i] for i in range(n))
