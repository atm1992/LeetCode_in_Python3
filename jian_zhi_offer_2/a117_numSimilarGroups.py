# -*- coding: UTF-8 -*-
"""
title: 相似的字符串
如果交换字符串 X 中的两个不同位置的字母，使得它和字符串 Y 相等，那么称 X 和 Y 两个字符串相似。如果这两个字符串本身是相等的，那它们也是相似的。
例如，"tars" 和 "rats" 是相似的 (交换 0 与 2 的位置)； "rats" 和 "arts" 也是相似的，但是 "star" 不与 "tars"，"rats"，或 "arts" 相似。
总之，它们通过相似性形成了两个关联组：{"tars", "rats", "arts"} 和 {"star"}。注意，"tars" 和 "arts" 是在同一组中，即使它们并不相似。形式上，对每个组而言，要确定一个单词在组中，只需要这个词和该组中至少一个单词相似。
给定一个字符串列表 strs。列表中的每个字符串都是 strs 中其它所有字符串的一个 字母异位词 。请问 strs 中有多少个相似字符串组？
字母异位词（anagram），一种把某个字符串的字母的位置（顺序）加以改换所形成的新词。


示例 1：
输入：strs = ["tars","rats","arts","star"]
输出：2

示例 2：
输入：strs = ["omv","ovm"]
输出：1


提示：
1 <= strs.length <= 300
1 <= strs[i].length <= 300
strs[i] 只包含小写字母。
strs 中的所有单词都具有相同的长度，且是彼此的字母异位词。
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
