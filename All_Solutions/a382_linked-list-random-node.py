# -*- coding: UTF-8 -*-
"""
title: 链表随机节点
Given a singly linked list, return a random node's value from the linked list. Each node must have the same probability of being chosen.
Implement the Solution class:
    Solution(ListNode head) Initializes the object with the head of the singly-linked list head.
    int getRandom() Chooses a node randomly from the list and returns its value. All the nodes of the list should be equally likely to be chosen.


Example 1:
Input
["Solution", "getRandom", "getRandom", "getRandom", "getRandom", "getRandom"]
[[[1, 2, 3]], [], [], [], [], []]
Output
[null, 1, 3, 2, 2, 3]
Explanation
Solution solution = new Solution([1, 2, 3]);
solution.getRandom(); // return 1
solution.getRandom(); // return 3
solution.getRandom(); // return 2
solution.getRandom(); // return 2
solution.getRandom(); // return 3
// getRandom() should return either 1, 2, or 3 randomly. Each element should have equal probability of returning.


Constraints:
The number of nodes in the linked list will be in the range [1, 10^4].
-10^4 <= Node.val <= 10^4
At most 10^4 calls will be made to getRandom.

Follow up:
What if the linked list is extremely large and its length is unknown to you?
Could you solve this efficiently without using extra space?
"""
from random import choice, randrange
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """先用列表存储所有节点的值，然后随机返回其中一个值"""

    def __init__(self, head: Optional[ListNode]):
        self.vals = []
        while head:
            self.vals.append(head.val)
            head = head.next

    def getRandom(self) -> int:
        return choice(self.vals)


class Solution2:
    """
    进阶问题：水塘抽样(蓄水池抽样)，适用于大数据流中的随机抽样。
    每次getRandom时，都从head开始遍历整个链表，对于遍历到的第i个节点(i从1开始，head为第1个节点)，从[0,i)中随机选择一个整数，
    若选出的这个整数等于0，则将当前第i个节点的值暂时作为res，之后若再次随机选出了0，则将那个节点的值作为新的res，直到遍历完整个链表。
    可以证明每个节点的值成为最终res的概率是相等的，均为 1/n
    P(第i个节点的值成为最终res)
    = P(第i次随机选出的整数为0) * P(第i+1次随机选出的整数 不 为0) * …… * P(第n次随机选出的整数 不 为0)
    = 1/i * (1 - 1/(i+1)) * …… * (1 - 1/n)
    = 1/i * i/(i+1) * …… * (n-1)/n
    = 1/n
    之所以叫水塘抽样(蓄水池抽样)，可理解为当水塘(蓄水池)满了时，之后每进入一滴水，就同样会有一滴水溢出水塘(蓄水池)，就类似于上面的替换操作。
    水塘抽样除了可以等概率(1/n)的随机从n个元素中选出1个元素；也可以等概率(k/n)的随机从n个元素中选出k个元素, k > 1。
    """

    def __init__(self, head: Optional[ListNode]):
        self.head = head

    def getRandom(self) -> int:
        node, i, res = self.head, 1, 0
        # 初始时，res的值肯定为head.val，因为head作为第1个元素，从[0,1)中随机选择一个整数，选出的整数只能是0，所以res是肯定能取到值的。
        while node:
            if randrange(i) == 0:
                res = node.val
            i += 1
            node = node.next
        return res

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
