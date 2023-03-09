# -*- coding: UTF-8 -*-
"""
title: 句子相似性 III
A sentence is a list of words that are separated by a single space with no leading or trailing spaces. For example, "Hello World", "HELLO", "hello world hello world" are all sentences. Words consist of only uppercase and lowercase English letters.
Two sentences sentence1 and sentence2 are similar if it is possible to insert an arbitrary sentence (possibly empty) inside one of these sentences such that the two sentences become equal. For example, sentence1 = "Hello my name is Jane" and sentence2 = "Hello Jane" can be made equal by inserting "my name is" between "Hello" and "Jane" in sentence2.
Given two sentences sentence1 and sentence2, return true if sentence1 and sentence2 are similar. Otherwise, return false.


Example 1:
Input: sentence1 = "My name is Haley", sentence2 = "My Haley"
Output: true
Explanation: sentence2 can be turned to sentence1 by inserting "name is" between "My" and "Haley".

Example 2:
Input: sentence1 = "of", sentence2 = "A lot of words"
Output: false
Explanation: No single sentence can be inserted inside one of the sentences to make it equal to the other.

Example 3:
Input: sentence1 = "Eating right now", sentence2 = "Eating"
Output: true
Explanation: sentence2 can be turned to sentence1 by inserting "right now" at the end of the sentence.


Constraints:
1 <= sentence1.length, sentence2.length <= 100
sentence1 and sentence2 consist of lowercase and uppercase English letters and spaces.
The words in sentence1 and sentence2 are separated by a single space.
"""


class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        """
        双指针。
        假设sentence2是更短的那个，因此要往sentence2中加入一句话，这句话要么加在开头、要么加在结尾、要么加在中间。
        因此可以用两个指针(l2, r2)分别从sentence2的开头和结尾进行遍历，最终若l2 - r2 == 1，则返回True
        """
        if len(sentence1) < len(sentence2):
            return self.areSentencesSimilar(sentence2, sentence1)
        words1, words2 = sentence1.split(' '), sentence2.split(' ')
        l1, r1 = 0, len(words1) - 1
        l2, r2 = 0, len(words2) - 1
        while l2 <= r2 and words2[l2] == words1[l1]:
            l2 += 1
            l1 += 1
        while r2 >= l2 and words2[r2] == words1[r1]:
            r2 -= 1
            r1 -= 1
        return l2 - r2 == 1


if __name__ == '__main__':
    print(Solution().areSentencesSimilar(sentence1="qbaVXO Msgr aEWD v ekcb", sentence2="Msgr aEWD ekcb"))
