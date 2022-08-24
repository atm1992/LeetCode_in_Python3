# -*- coding: UTF-8 -*-
"""
title: 交替打印 FooBar
Suppose you are given the following code:
    class FooBar {
      public void foo() {
        for (int i = 0; i < n; i++) {
          print("foo");
        }
      }

      public void bar() {
        for (int i = 0; i < n; i++) {
          print("bar");
        }
      }
    }
The same instance of FooBar will be passed to two different threads:
    thread A will call foo(), while
    thread B will call bar().
Modify the given program to output "foobar" n times.


Example 1:
Input: n = 1
Output: "foobar"
Explanation: There are two threads being fired asynchronously. One of them calls foo(), while the other calls bar().
"foobar" is being output 1 time.

Example 2:
Input: n = 2
Output: "foobarfoobar"
Explanation: "foobar" is being output 2 times.


Constraints:
1 <= n <= 1000
"""


class FooBar:
    """交替锁"""

    def __init__(self, n):
        from threading import Lock
        self.n = n
        self.foo_lock = Lock()
        self.bar_lock = Lock()
        self.bar_lock.acquire()

    def foo(self, printFoo: 'Callable[[], None]') -> None:
        for i in range(self.n):
            self.foo_lock.acquire()
            # printFoo() outputs "foo". Do not change or remove this line.
            printFoo()
            self.bar_lock.release()

    def bar(self, printBar: 'Callable[[], None]') -> None:
        for i in range(self.n):
            self.bar_lock.acquire()
            # printBar() outputs "bar". Do not change or remove this line.
            printBar()
            self.foo_lock.release()


class FooBar2:
    """计数信号量"""

    def __init__(self, n):
        from threading import Semaphore
        self.n = n
        self.foo_sema = Semaphore(1)
        self.bar_sema = Semaphore(0)

    def foo(self, printFoo: 'Callable[[], None]') -> None:
        for i in range(self.n):
            self.foo_sema.acquire()
            # printFoo() outputs "foo". Do not change or remove this line.
            printFoo()
            self.bar_sema.release()

    def bar(self, printBar: 'Callable[[], None]') -> None:
        for i in range(self.n):
            self.bar_sema.acquire()
            # printBar() outputs "bar". Do not change or remove this line.
            printBar()
            self.foo_sema.release()
