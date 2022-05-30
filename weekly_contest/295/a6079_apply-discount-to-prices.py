# -*- coding: UTF-8 -*-


class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        discount = (100 - discount) / 100
        words = sentence.split(' ')
        for i in range(len(words)):
            word = words[i]
            if word.startswith('$') and word[1:].isdigit():
                num = int(word[1:]) * discount
                words[i] = f'${num:.2f}'
        return ' '.join(words)


if __name__ == '__main__':
    res = Solution().discountPrices(sentence="1 2 $3 4 $5 $6 7 8$ $9 $10$", discount=100)
    print(res == "1 2 $0.00 4 $0.00 $0.00 7 8$ $0.00 $10$")
