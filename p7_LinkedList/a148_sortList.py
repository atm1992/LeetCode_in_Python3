# -*- coding: UTF-8 -*-
"""
排序链表。
在 O(nlogn) 时间复杂度和常数级空间复杂度下，对链表进行排序。
示例 1:
输入: 4->2->1->3
输出: 1->2->3->4
示例 2:
输入: -1->5->3->4->0
输出: -1->0->3->4->5

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
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        # 递归终止条件
        if not head or not head.next:
            return head
        slow, fast = head, head.next
        # 跳出循环时，fast或fast.next为None，若链表长度为奇数，则中心点只有一个，slow正好指向该中心点；
        # 若链表长度为偶数，则中心点有两个，slow指向的是左边的这个中心点
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # 将链表分为两段，head为前一段链表的头结点，mid为后一段链表的头结点
        mid = slow.next
        slow.next = None
        # 通过递归来不断地切分链表，直到每段链表的长度为0或1
        # 递归返回的left、right分别为前一段有序链表(head)的头结点、后一段有序链表(mid)的头结点
        left = self.sortList(head)
        right = self.sortList(mid)
        # 将前一段有序链表 与 后一段有序链表进行合并
        # 新建一个空节点，作为返回结果的前一个结点
        res = ListNode(0)
        tmp = res
        while left and right:
            if left.val <= right.val:
                tmp.next = left
                left = left.next
            else:
                tmp.next = right
                right = right.next
            tmp = tmp.next
        tmp.next = left if left else right
        return res.next

    def sortList_2(self, head: ListNode) -> ListNode:
        tmp = head
        length = 0
        # 获取原始链表的长度。这里的时间复杂度为O(n)
        while tmp:
            length += 1
            tmp = tmp.next
        # 新建一个空节点，作为返回结果的前一个结点
        res = ListNode(0)
        res.next = head
        # 刚开始两两合并长度为1的有序链表
        intv = 1
        # 外层while intv < length循环的时间复杂度为O(logn)；内层while cur循环的时间复杂度为O(n)，因此总的时间复杂度为O(nlogn)
        # 不先使用递归切分链表，而是直接在原始链表上(1——>2——>4 ……)两两合并有序链表
        while intv < length:
            pre, cur = res, res.next
            # cur指针一直在向后移。移动到整个链表的最末尾时跳出循环
            while cur:
                # h1为前一段待合并链表的头结点，h2为后一段待合并链表的头结点
                h1 = cur
                i = intv
                # 退出循环时，i==0 或 cur为None
                while i > 0 and cur:
                    cur = cur.next
                    i -= 1
                # 若退出上一个while循环时，i>0，说明前一段待合并链表的长度不足intv，则后一段待合并链表直接为空，此时无需合并两段链表
                if i > 0:
                    break
                h2 = cur
                i = intv
                # cur指针移动到当前次待合并链表的后一个节点上，也是下一次待合并链表的第一个节点
                while i > 0 and cur:
                    cur = cur.next
                    i -= 1
                # 接下来，合并两段有序链表
                # 前一段待合并链表的长度肯定为intv，而后一段待合并链表的长度可能不足intv
                l1, l2 = intv, intv - i
                # 跳出循环时，l1、l2中至少一个为0
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
                # 在pre的后面接上剩余部分
                pre.next = h1 if l1 > 0 else h2
                # 将pre指针移动到已合并链表的最后一个节点上
                for _ in range(l1 + l2):
                    pre = pre.next
                # cur当前指向的是下一次待合并链表的第一个节点
                pre.next = cur
            intv *= 2
        return res.next
