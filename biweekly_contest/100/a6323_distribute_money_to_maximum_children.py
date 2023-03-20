# -*- coding: UTF-8 -*-
"""
title: 将钱分给最多的儿童
You are given an integer money denoting the amount of money (in dollars) that you have and another integer children denoting the number of children that you must distribute the money to.
You have to distribute the money according to the following rules:
    All money must be distributed.
    Everyone must receive at least 1 dollar.
    Nobody receives 4 dollars.
Return the maximum number of children who may receive exactly 8 dollars if you distribute the money according to the aforementioned rules. If there is no way to distribute the money, return -1.


Example 1:
Input: money = 20, children = 3
Output: 1
Explanation:
The maximum number of children with 8 dollars will be 1. One of the ways to distribute the money is:
- 8 dollars to the first child.
- 9 dollars to the second child.
- 3 dollars to the third child.
It can be proven that no distribution exists such that number of children getting 8 dollars is greater than 1.

Example 2:
Input: money = 16, children = 2
Output: 2
Explanation: Each child can be given 8 dollars.


Constraints:
1 <= money <= 200
2 <= children <= 30
"""


class Solution:
    def distMoney(self, money: int, children: int) -> int:
        """数学"""
        money -= children
        if money < 0:
            return -1
        div, mod = divmod(money, 7)
        if div > children:
            # 最后一个人会大于8元
            res = children - 1
        elif div == children:
            # 若mod == 0，则说明刚好所有人都分到8元，否则最后一个人会大于8元
            res = children if mod == 0 else children - 1
        elif div == children - 1 and mod == 3:
            # 若最后一个人刚好是分到4元，则可以让最后一个人加1元或减1元，加减的部分分给倒数第二个人，从而导致倒数第二个人也不是8元
            res = children - 2
        else:
            res = div
        return res


if __name__ == '__main__':
    print(Solution().distMoney(money=16, children=2))
