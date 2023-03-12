# -*- coding: UTF-8 -*-
"""
title: 递枕头
There are n people standing in a line labeled from 1 to n. The first person in the line is holding a pillow initially. Every second, the person holding the pillow passes it to the next person standing in the line. Once the pillow reaches the end of the line, the direction changes, and people continue passing the pillow in the opposite direction.
    For example, once the pillow reaches the nth person they pass it to the n - 1th person, then to the n - 2th person and so on.
Given the two positive integers n and time, return the index of the person holding the pillow after time seconds.


Example 1:
Input: n = 4, time = 5
Output: 2
Explanation: People pass the pillow in the following way: 1 -> 2 -> 3 -> 4 -> 3 -> 2.
Afer five seconds, the pillow is given to the 2nd person.

Example 2:
Input: n = 3, time = 2
Output: 3
Explanation: People pass the pillow in the following way: 1 -> 2 -> 3.
Afer two seconds, the pillow is given to the 3rd person.


Constraints:
2 <= n <= 1000
1 <= time <= 1000
"""


class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        """数学。找规律，每2n - 2为一个周期"""
        time %= (2 * n - 2)
        return 2 * n - time - 1 if time >= n else time + 1

    def passThePillow_2(self, n: int, time: int) -> int:
        """数学。找规律，一个完整周期是2n - 2，其中的前n-1是递增，后n-1是递减。若time//(n-1)为偶数，则表示处于递增段；否则处于递减段。"""
        div, mod = divmod(time, n - 1)
        return mod + 1 if div % 2 == 0 else n - mod


if __name__ == '__main__':
    print(Solution().passThePillow_2(3, 2))
