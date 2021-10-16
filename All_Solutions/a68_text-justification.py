# -*- coding: UTF-8 -*-
"""
title: 文本左右对齐
Given an array of strings words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.
You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.
Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line does not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.
For the last line of text, it should be left-justified and no extra space is inserted between words.

Note:
A word is defined as a character sequence consisting of non-space characters only.
Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
The input array words contains at least one word.


Example 1:
Input: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
Output:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]

Example 2:
Input: words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16
Output:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
Explanation: Note that the last line is "shall be    " instead of "shall     be", because the last line must be left-justified instead of fully-justified.
Note that the second line is also left-justified becase it contains only one word.

Example 3:
Input: words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], maxWidth = 20
Output:
[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]


Constraints:
1 <= words.length <= 300
1 <= words[i].length <= 20
words[i] consists of only English letters and symbols.
1 <= maxWidth <= 100
words[i].length <= maxWidth
"""
from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        """分情况讨论：
        一、当前行为最后一行：单词左对齐，单词之间只有一个空格，行末用空格填充；
        二、当前行不是最后一行，但只有一个单词：该单词左对齐，行末用空格填充；
        三、当前行不是最后一行，且不只是一个单词：word_num表示当前行的单词总数，space_num表示当前行的空格总数，
        则当前行每个单词之间的空格数为space_avg = space_num // (word_num-1)，多出来的空格space_extra = space_num % (word_num-1)
        应该放在左侧的space_extra+1个单词之间，因此，左侧的space_extra+1个单词之间的空格数为space_avg+1"""
        res = []
        # cur 表示当前单词在words中的下标
        cur, n = 0, len(words)
        while True:
            # start 表示当前行第一个单词在words中的下标
            start = cur
            # 统计当前行已填充单词的长度(不包含空格)
            row_width = 0
            # cur - start 表示已填充单词之间所需的空格数，因为每个单词之间至少要有一个空格。
            # 退出while循环时，若cur == n，则表示当前行为最后一行；否则cur表示下一行第一个单词在words中的下标
            while cur < n and row_width + len(words[cur]) + cur - start <= maxWidth:
                row_width += len(words[cur])
                cur += 1
            # word_num表示当前行的单词总数；space_num表示当前行的空格总数。单词之间的空格数为 word_num - 1
            word_num = cur - start
            space_num = maxWidth - row_width
            # 当前行为最后一行
            if cur == n:
                res.append(' '.join(words[start:cur]) + ' ' * (space_num - (word_num - 1)))
                return res
            # 当前行只有一个单词
            elif word_num == 1:
                res.append(words[start] + ' ' * space_num)
            else:
                # space_avg 表示当前行每个单词之间的平均间距；space_extra 表示多出来的空格，左侧的space_extra+1个单词之间需要再额外多一个空格
                space_avg = space_num // (word_num - 1)
                space_extra = space_num % (word_num - 1)
                tmp = (' ' * space_avg).join(words[start:cur])
                res.append(tmp.replace(' ' * space_avg, ' ' * (space_avg + 1), space_extra))


if __name__ == '__main__':
    print(Solution().fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16))
