# -*- coding: UTF-8 -*-
"""
title: 按序打印
Suppose we have a class:
     public class Foo {
       public void first() { print("first"); }
       public void second() { print("second"); }
       public void third() { print("third"); }
     }
The same instance of Foo will be passed to three different threads. Thread A will call first(), thread B will call second(), and thread C will call third(). Design a mechanism and modify the program to ensure that second() is executed after first(), and third() is executed after second().
Note:
We do not know how the threads will be scheduled in the operating system, even though the numbers in the input seem to imply the ordering. The input format you see is mainly to ensure our tests' comprehensiveness.


Example 1:
Input: nums = [1,2,3]
Output: "firstsecondthird"
Explanation: There are three threads being fired asynchronously. The input [1,2,3] means thread A calls first(), thread B calls second(), and thread C calls third(). "firstsecondthird" is the correct output.

Example 2:
Input: nums = [1,3,2]
Output: "firstsecondthird"
Explanation: The input [1,3,2] means thread A calls first(), thread B calls third(), and thread C calls second(). "firstsecondthird" is the correct output.


Constraints:
nums is a permutation of [1, 2, 3].
"""


class Foo:
    """交替锁"""

    def __init__(self):
        from threading import Lock
        self.first_job_done = Lock()
        self.second_job_done = Lock()
        self.first_job_done.acquire()
        self.second_job_done.acquire()

    def first(self, printFirst: 'Callable[[], None]') -> None:
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        # Notify the thread that is waiting for the first job to be done.
        self.first_job_done.release()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        # Wait for the first job to be done
        with self.first_job_done:
            # printSecond() outputs "second". Do not change or remove this line.
            printSecond()
            # Notify the thread that is waiting for the second job to be done.
            self.second_job_done.release()

    def third(self, printThird: 'Callable[[], None]') -> None:
        # Wait for the second job to be done.
        with self.second_job_done:
            # printThird() outputs "third". Do not change or remove this line.
            printThird()
