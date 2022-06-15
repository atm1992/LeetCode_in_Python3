# -*- coding: UTF-8 -*-
"""
title: 链表排序
给定链表的头结点 head ，请将其按 升序 排列并返回 排序后的链表 。


示例 1：
输入：head = [4,2,1,3]
输出：[1,2,3,4]

示例 2：
输入：head = [-1,5,3,4,0]
输出：[-1,0,3,4,5]

示例 3：
输入：head = []
输出：[]


提示：
链表中节点的数目在范围 [0, 5 * 10^4] 内
-10^5 <= Node.val <= 10^5

进阶：你可以在 O(nlogn) 时间复杂度和常数级空间复杂度下，对链表进行排序吗？


解题思路：归并排序。
对数组做归并排序的空间复杂度为 O(n)，分别由新开辟数组O(n)和递归函数调用O(logn)组成，而根据链表特性：
数组额外空间：链表可以通过修改引用来更改节点顺序，无需像数组一样开辟额外空间；
递归额外空间：递归调用函数将带来O(logn)的空间复杂度，因此若希望达到O(1)空间复杂度，则不能使用递归。

方法一为递归版的归并排序，时间复杂度为O(nlogn)，空间复杂度为O(logn)，因为这里使用了递归来不断地切分链表，
而递归需要使用到栈，递归算法的空间复杂度为：递归深度O(logn) * 每次递归所需的辅助空间O(1)

方法二为非递归版的归并排序，时间复杂度为O(nlogn)，空间复杂度为O(1)
此方法不先使用递归切分链表，而是直接在原始链表上(1——>2——>4 ……)两两合并有序链表
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        """递归版的归并排序"""
        # 递归终止条件。少于两个节点
        if not head or not head.next:
            return head
        slow, fast = head, head
        # 退出循环时，若链表长度为奇数，则链表的中心点只有一个，slow正好指向它；若链表长度为偶数，则链表的中心点有两个，slow指向的是这两个中的前一个。
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        # 将链表分为左右两段。若链表长度为奇数，则左侧长度 == 右侧长度 + 1；若链表长度为偶数，则左侧长度 == 右侧长度。
        right_head = slow.next
        slow.next = None
        left = self.sortList(head)
        right = self.sortList(right_head)
        dummy_head = ListNode()
        tmp = dummy_head
        while left and right:
            if left.val <= right.val:
                tmp.next = left
                left = left.next
            else:
                tmp.next = right
                right = right.next
            tmp = tmp.next
        tmp.next = left if left else right
        return dummy_head.next

    def sortList_2(self, head: ListNode) -> ListNode:
        """非递归版的归并排序"""
        size = 0
        node = head
        while node:
            size += 1
            node = node.next
        dummy_head = ListNode(-1, head)
        # 初始时，两两合并长度为1的有序链表
        merge_size = 1
        while merge_size < size:
            pre, cur = dummy_head, dummy_head.next
            while cur:
                # h1 指向两个待合并有序链表中的前一个的头节点，h2 指向后一个的头节点
                h1 = cur
                cnt = merge_size
                while cnt > 0 and cur:
                    cur = cur.next
                    cnt -= 1
                # 若前一个链表的长度不满merge_size，则无需合并
                if cnt > 0:
                    break
                # 后一个有序链表的头节点。注意：这里并没有将前一个链表截断，前一个链表 与 后一个链表是连着的
                h2 = cur
                cnt = merge_size
                while cnt > 0 and cur:
                    cur = cur.next
                    cnt -= 1
                # 前、后两个链表的长度，后一个链表的长度可能不足merge_size
                l1, l2 = merge_size, merge_size - cnt
                while l1 > 0 and l2 > 0:
                    if h1.val <= h2.val:
                        pre.next = h1
                        h1 = h1.next
                        l1 -= 1
                    else:
                        pre.next = h2
                        h2 = h2.next
                        l2 -= 1
                    pre = pre.next
                # 注意：这里是判断 if l1 > 0，而不是 if h1
                pre.next = h1 if l1 > 0 else h2
                # 将pre移动到已合并链表中的最后一个节点。此时的l1、l2中，有一个为0
                for _ in range(l1 + l2):
                    pre = pre.next
                # 加上这行代码的原因：如果之后的链表长度不满merge_size(只有待合并链表中的前一个)，那么就会break出去，最后这一小段链表就不会被连接到pre的后边
                pre.next = cur
            merge_size *= 2
        return dummy_head.next
