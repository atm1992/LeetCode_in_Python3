# -*- coding: UTF-8 -*-
class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch not in word:
            return word
        idx = word.index(ch)
        tmp = word[0:idx + 1]
        return tmp[::-1] + word[idx + 1:]


if __name__ == '__main__':
    word = "abcdefd"
    ch = "d"
    print(Solution().reversePrefix(word, ch))
