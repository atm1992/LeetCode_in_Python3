# -*- coding: UTF-8 -*-
"""
title: 公司命名
You are given an array of strings ideas that represents a list of names to be used in the process of naming a company. The process of naming a company is as follows:
    Choose 2 distinct names from ideas, call them ideaA and ideaB.
    Swap the first letters of ideaA and ideaB with each other.
    If both of the new names are not found in the original ideas, then the name ideaA ideaB (the concatenation of ideaA and ideaB, separated by a space) is a valid company name.
    Otherwise, it is not a valid name.
Return the number of distinct valid names for the company.


Example 1:
Input: ideas = ["coffee","donuts","time","toffee"]
Output: 6
Explanation: The following selections are valid:
- ("coffee", "donuts"): The company name created is "doffee conuts".
- ("donuts", "coffee"): The company name created is "conuts doffee".
- ("donuts", "time"): The company name created is "tonuts dime".
- ("donuts", "toffee"): The company name created is "tonuts doffee".
- ("time", "donuts"): The company name created is "dime tonuts".
- ("toffee", "donuts"): The company name created is "doffee tonuts".
Therefore, there are a total of 6 distinct company names.
The following are some examples of invalid selections:
- ("coffee", "time"): The name "toffee" formed after swapping already exists in the original array.
- ("time", "toffee"): Both names are still the same after swapping and exist in the original array.
- ("coffee", "toffee"): Both names formed after swapping already exist in the original array.

Example 2:
Input: ideas = ["lack","back"]
Output: 0
Explanation: There are no valid selections. Therefore, 0 is returned.


Constraints:
2 <= ideas.length <= 5 * 10^4
1 <= ideas[i].length <= 10
ideas[i] consists of lowercase English letters.
All the strings in ideas are unique.
"""
from collections import defaultdict
from typing import List


class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        """
        考虑哪些单词是不能互换首字母的？
        1、拥有相同首字母的两个单词，即 这两个单词在同一分组，互换首字母没有意义
        2、假设单词a、单词b在不同分组，但如果 去除了首字母后的单词a 与 去除了首字母后的单词b 在同一分组，则此时也不能互换首字母
        """
        group = defaultdict(set)
        # 将所有ideas按首字母进行分组
        for idea in ideas:
            group[idea[0]].add(idea[1:])
        res = 0
        all_sets = group.values()
        for s1 in all_sets:
            for s2 in all_sets:
                # 拼接后，s1中的单词在前，s2中的单词在后，即 'word1 word2'。'word2 word1' 同样也是有效的
                common_size = len(s1 & s2)
                res += (len(s1) - common_size) * (len(s2) - common_size)
        return res


if __name__ == '__main__':
    print(Solution().distinctNames(ideas=["coffee", "donuts", "time", "toffee"]))
