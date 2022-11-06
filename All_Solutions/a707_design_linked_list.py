# -*- coding: UTF-8 -*-
"""
title: 设计链表
Design your implementation of the linked list. You can choose to use a singly or doubly linked list.
A node in a singly linked list should have two attributes: val and next. val is the value of the current node, and next is a pointer/reference to the next node.
If you want to use the doubly linked list, you will need one more attribute prev to indicate the previous node in the linked list. Assume all nodes in the linked list are 0-indexed.
Implement the MyLinkedList class:
    MyLinkedList() Initializes the MyLinkedList object.
    int get(int index) Get the value of the indexth node in the linked list. If the index is invalid, return -1.
    void addAtHead(int val) Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
    void addAtTail(int val) Append a node of value val as the last element of the linked list.
    void addAtIndex(int index, int val) Add a node of value val before the indexth node in the linked list. If index equals the length of the linked list, the node will be appended to the end of the linked list. If index is greater than the length, the node will not be inserted.
    void deleteAtIndex(int index) Delete the indexth node in the linked list, if the index is valid.


Example 1:
Input
["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get", "deleteAtIndex", "get"]
[[], [1], [3], [1, 2], [1], [1], [1]]
Output
[null, null, null, null, 2, null, 3]
Explanation
MyLinkedList myLinkedList = new MyLinkedList();
myLinkedList.addAtHead(1);
myLinkedList.addAtTail(3);
myLinkedList.addAtIndex(1, 2);    // linked list becomes 1->2->3
myLinkedList.get(1);              // return 2
myLinkedList.deleteAtIndex(1);    // now the linked list is 1->3
myLinkedList.get(1);              // return 3


Constraints:
0 <= index, val <= 1000
Please do not use the built-in LinkedList library.
At most 2000 calls will be made to get, addAtHead, addAtTail, addAtIndex and deleteAtIndex.
"""


class ListNode:
    def __init__(self, val: int):
        self.val = val
        self.pre = None
        self.nxt = None


class MyLinkedList:
    """双向链表"""
    def __init__(self):
        self.size = 0
        self.head, self.tail = ListNode(-1), ListNode(-1)
        self.head.nxt = self.tail
        self.tail.pre = self.head

    def __goto(self, index: int) -> ListNode:
        if 2 * index < self.size:
            cur_node = self.head
            for _ in range(index + 1):
                cur_node = cur_node.nxt
        else:
            cur_node = self.tail
            for _ in range(self.size - index):
                cur_node = cur_node.pre
        return cur_node

    def get(self, index: int) -> int:
        if index >= self.size:
            return -1
        cur_node = self.__goto(index)
        return cur_node.val

    def __addBefore(self, val: int, next_node: ListNode) -> None:
        cur_node = ListNode(val)
        cur_node.pre = next_node.pre
        cur_node.pre.nxt = cur_node
        next_node.pre = cur_node
        cur_node.nxt = next_node
        self.size += 1

    def addAtHead(self, val: int) -> None:
        self.__addBefore(val, self.head.nxt)

    def addAtTail(self, val: int) -> None:
        self.__addBefore(val, self.tail)

    def addAtIndex(self, index: int, val: int) -> None:
        if index <= self.size:
            self.__addBefore(val, self.__goto(index))

    def deleteAtIndex(self, index: int) -> None:
        if index < self.size:
            cur_node = self.__goto(index)
            cur_node.pre.nxt = cur_node.nxt
            cur_node.nxt.pre = cur_node.pre
            self.size -= 1


if __name__ == '__main__':
    obj = MyLinkedList()
    obj.addAtHead(1)
    obj.addAtTail(3)
    obj.addAtIndex(1, 2)
    print(obj.get(1))
    obj.deleteAtIndex(1)
    print(obj.get(1))
