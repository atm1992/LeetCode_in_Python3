# -*- coding: UTF-8 -*-
"""
title: 最短单词距离 II
Design a data structure that will be initialized with a string array, and then it should answer queries of the shortest distance between two different strings from the array.
Implement the WordDistance class:
    WordDistance(String[] wordsDict) initializes the object with the strings array wordsDict.
    int shortest(String word1, String word2) returns the shortest distance between word1 and word2 in the array wordsDict.


Example 1:
Input
["WordDistance", "shortest", "shortest"]
[[["practice", "makes", "perfect", "coding", "makes"]], ["coding", "practice"], ["makes", "coding"]]
Output
[null, 3, 1]
Explanation
WordDistance wordDistance = new WordDistance(["practice", "makes", "perfect", "coding", "makes"]);
wordDistance.shortest("coding", "practice"); // return 3
wordDistance.shortest("makes", "coding");    // return 1


Constraints:
1 <= wordsDict.length <= 3 * 10^4
1 <= wordsDict[i].length <= 10
wordsDict[i] consists of lowercase English letters.
word1 and word2 are in wordsDict.
word1 != word2
At most 5000 calls will be made to shortest.
"""
from collections import defaultdict
from typing import List


class WordDistance:
    """哈希表 + 双指针"""

    def __init__(self, wordsDict: List[str]):
        self.word2idxs = defaultdict(list)
        for idx, word in enumerate(wordsDict):
            self.word2idxs[word].append(idx)

    def shortest(self, word1: str, word2: str) -> int:
        # wordsDict.length <= 3 * 10^4
        res = 30000
        idxs1, idxs2 = self.word2idxs[word1], self.word2idxs[word2]
        i1 = i2 = 0
        n1, n2 = len(idxs1), len(idxs2)
        while i1 < n1 and i2 < n2:
            if idxs1[i1] < idxs2[i2]:
                res = min(res, idxs2[i2] - idxs1[i1])
                i1 += 1
            else:
                res = min(res, idxs1[i1] - idxs2[i2])
                i2 += 1
            if res == 1:
                break
        return res


if __name__ == '__main__':
    obj = WordDistance(["practice", "makes", "perfect", "coding", "makes"])
    print(obj.shortest("makes", "coding"))
