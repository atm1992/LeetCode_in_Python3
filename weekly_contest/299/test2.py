# -*- coding: UTF-8 -*-


class Solution:
    def countHousePlacements(self, n: int) -> int:
        mod = 10 ** 9 + 7
        a, b = 1, 2
        for i in range(1, n):
            a = b - a
            b = b + a
        return b * b % mod


if __name__ == '__main__':
    print(Solution().countHousePlacements(3))
