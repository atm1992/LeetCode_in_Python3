# -*- coding: UTF-8 -*-


class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        """暴力"""
        max_num = '0'
        for i in range(len(number)):
            if number[i] == digit:
                max_num = max(max_num, number[:i] + number[i + 1:])
        return max_num

    def removeDigit_2(self, number: str, digit: str) -> str:
        """贪心"""
        last_idx = 0
        n = len(number)
        for i in range(n):
            if number[i] == digit:
                if i == n - 1 or number[i] < number[i + 1]:
                    return number[:i] + number[i + 1:]
                last_idx = i
        return number[:last_idx] + number[last_idx + 1:]


if __name__ == '__main__':
    print(Solution().removeDigit(number="3619552534", digit="5"))
