# -*- coding: UTF-8 -*-
"""
title: 猜数字游戏
You are playing the Bulls and Cows game with your friend.
You write down a secret number and ask your friend to guess what the number is. When your friend makes a guess, you provide a hint with the following info:
    The number of "bulls", which are digits in the guess that are in the correct position.
    The number of "cows", which are digits in the guess that are in your secret number but are located in the wrong position. Specifically, the non-bull digits in the guess that could be rearranged such that they become bulls.
Given the secret number secret and your friend's guess guess, return the hint for your friend's guess.
The hint should be formatted as "xAyB", where x is the number of bulls and y is the number of cows. Note that both secret and guess may contain duplicate digits.


Example 1:
Input: secret = "1807", guess = "7810"
Output: "1A3B"
Explanation: Bulls are connected with a '|' and cows are underlined:
"1807"
  |
"7810"

Example 2:
Input: secret = "1123", guess = "0111"
Output: "1A1B"
Explanation: Bulls are connected with a '|' and cows are underlined:
"1123"        "1123"
  |      or     |
"0111"        "0111"
Note that only one of the two unmatched 1s is counted as a cow since the non-bull digits can only be rearranged to allow one 1 to be a bull.


Constraints:
1 <= secret.length, guess.length <= 1000
secret.length == guess.length
secret and guess consist of digits only.
"""
from collections import defaultdict


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        secret_digit2cnt = defaultdict(int)
        guess_digit2cnt = defaultdict(int)
        cnt_A = cnt_B = 0
        for s, g in zip(secret, guess):
            if s == g:
                cnt_A += 1
            else:
                if guess_digit2cnt[s] > 0:
                    cnt_B += 1
                    guess_digit2cnt[s] -= 1
                else:
                    secret_digit2cnt[s] += 1
                if secret_digit2cnt[g] > 0:
                    cnt_B += 1
                    secret_digit2cnt[g] -= 1
                else:
                    guess_digit2cnt[g] += 1
        return f'{cnt_A}A{cnt_B}B'


if __name__ == '__main__':
    print(Solution().getHint(secret="1123", guess="0111"))
