# -*- coding: UTF-8 -*-
"""
title: 用栈实现队列
Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).
Implement the MyQueue class:
    void push(int x) Pushes element x to the back of the queue.
    int pop() Removes the element from the front of the queue and returns it.
    int peek() Returns the element at the front of the queue.
    boolean empty() Returns true if the queue is empty, false otherwise.
Notes:
    You must use only standard operations of a stack, which means only push to top, peek/pop from top, size, and is empty operations are valid.
    Depending on your language, the stack may not be supported natively. You may simulate a stack using a list or deque (double-ended queue) as long as you use only a stack's standard operations.


Example 1:
Input:
["MyQueue", "push", "push", "peek", "pop", "empty"]
[[], [1], [2], [], [], []]
Output:
[null, null, null, 1, 1, false]
Explanation:
MyQueue myQueue = new MyQueue();
myQueue.push(1); // queue is: [1]
myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)
myQueue.peek(); // return 1
myQueue.pop(); // return 1, queue is [2]
myQueue.empty(); // return false


Constraints:
1 <= x <= 9
At most 100 calls will be made to push, pop, peek, and empty.
All the calls to pop and peek are valid.

Follow-up: Can you implement the queue such that each operation is amortized O(1) time complexity? In other words, performing n operations will take overall O(n) time even if one of those operations may take longer.
"""


class MyQueue:

    def __init__(self):
        self.stack_1 = []
        self.stack_2 = []

    def push(self, x: int) -> None:
        while self.stack_1:
            self.stack_2.append(self.stack_1.pop())
        self.stack_1.append(x)
        while self.stack_2:
            self.stack_1.append(self.stack_2.pop())

    def pop(self) -> int:
        return self.stack_1.pop()

    def peek(self) -> int:
        return self.stack_1[-1]

    def empty(self) -> bool:
        return not self.stack_1


class MyQueue2:

    def __init__(self):
        # 一个做输入栈，一个做输出栈。若输出栈为空，则将输入栈中的所有元素 pop -> append 到输出栈
        self.in_stack = []
        self.out_stack = []

    def push(self, x: int) -> None:
        self.in_stack.append(x)

    def pop(self) -> int:
        if not self.out_stack:
            self._in2out()
        return self.out_stack.pop()

    def peek(self) -> int:
        if not self.out_stack:
            self._in2out()
        return self.out_stack[-1]

    def empty(self) -> bool:
        return len(self.in_stack) == len(self.out_stack) == 0

    def _in2out(self) -> None:
        while self.in_stack:
            self.out_stack.append(self.in_stack.pop())


if __name__ == '__main__':
    obj = MyQueue2()
    obj.push(3)
    obj.push(-1)
    print(obj.pop())
    print(obj.peek())
    print(obj.empty())
