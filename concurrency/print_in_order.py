# https://leetcode.com/problems/print-in-order/

# Print in Order
# Suppose we have a class:

# public class Foo {
#   public void first() { print("first"); }
#   public void second() { print("second"); }
#   public void third() { print("third"); }
# }

# The same instance of Foo will be passed to three different threads. Thread A
# will call first(), thread B will call second(), and thread C will call
# third(). Design a mechanism and modify the program to ensure that second() is
# executed after first(), and third() is executed after second().

# Example 1:
# Input: [1,2,3]
# Output: "firstsecondthird"
# Explanation: There are three threads being fired asynchronously. The input
# [1,2,3] means thread A calls first(), thread B calls second(), and thread C
# calls third(). "firstsecondthird" is the correct output.

# Example 2:
# Input: [1,3,2]
# Output: "firstsecondthird"
# Explanation: The input [1,3,2] means thread A calls first(), thread B calls
# third(), and thread C calls second(). "firstsecondthird" is the correct
# output.


# Note:
# We do not know how the threads will be scheduled in the operating system,
# even though the numbers in the input seems to imply the ordering. The input
# format you see is mainly to ensure our tests' comprehensiveness.


# full credits from
# https://leetcode.com/problems/print-in-order/discuss/335939/5-Python-threading-solutions-(Barrier-Lock-Event-Semaphore-Condition)-with-explanation

# 5 Python threading solutions (Barrier, Lock, Event, Semaphore, Condition)
# with explanation


from typing import Callable
from threading import Barrier, Lock, Event, Semaphore, Condition


class Foo_Barrier:
    def __init__(self):
        self._first = Barrier(2)
        self._second = Barrier(2)

    def first(self, printFirst: Callable[[], None]) -> None:
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self._first.wait()

    def second(self, printSecond: Callable[[], None]) -> None:
        # printSecond() outputs "second". Do not change or remove this line.
        self._first.wait()
        printSecond()
        self._second.wait()

    def third(self, printThird: Callable[[], None]) -> None:
        # printThird() outputs "third". Do not change or remove this line.
        self._second.wait()
        printThird()


class Foo_Locks:
    def __init__(self):
        self._locks = (Lock(), Lock())
        self._locks[0].acquire()
        self._locks[1].acquire()

    def first(self, printFirst: Callable[[], None]) -> None:
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self._locks[0].release()

    def second(self, printSecond: Callable[[], None]) -> None:
        # printSecond() outputs "second". Do not change or remove this line.
        with self._locks[0]:
            printSecond()
            self._locks[1].release()

    def third(self, printThird: Callable[[], None]) -> None:
        # printThird() outputs "third". Do not change or remove this line.
        with self._locks[1]:
            printThird()


class Foo_Event:
    def __init__(self):
        self._done = (Event(), Event())

    def first(self, printFirst: Callable[[], None]) -> None:
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self._done[0].set()

    def second(self, printSecond: Callable[[], None]) -> None:
        # printSecond() outputs "second". Do not change or remove this line.
        self._done[0].wait()
        printSecond()
        self._done[1].set()

    def third(self, printThird: Callable[[], None]) -> None:
        # printThird() outputs "third". Do not change or remove this line.
        self._done[1].wait()
        printThird()


class Foo_Semaphore:
    def __init__(self):
        self._gates = (Semaphore(0), Semaphore(0))

    def first(self, printFirst: Callable[[], None]) -> None:
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self._gates[0].release()

    def second(self, printSecond: Callable[[], None]) -> None:
        # printSecond() outputs "second". Do not change or remove this line.
        with self._gates[0]:
            printSecond()
            self._gates[1].release()

    def third(self, printThird: Callable[[], None]) -> None:
        # printThird() outputs "third". Do not change or remove this line.
        with self._gates[1]:
            printThird()


class Foo_Condition:
    def __init__(self):
        self._exec_condition = Condition()
        self._order = 0
        self._first_finish = lambda: self._order == 1
        self._second_finish = lambda: self._order == 2
        pass

    def first(self, printFirst: Callable[[], None]) -> None:
        # printFirst() outputs "first". Do not change or remove this line.
        with self._exec_condition:
            printFirst()
            self._order = 1
            self._exec_condition.notify(2)

    def second(self, printSecond: Callable[[], None]) -> None:
        # printSecond() outputs "second". Do not change or remove this line.
        with self._exec_condition:
            self._exec_condition.wait_for(self._first_finish)
            printSecond()
            self._order = 2
            self._exec_condition.notify()

    def third(self, printThird: Callable[[], None]) -> None:
        # printThird() outputs "third". Do not change or remove this line.
        with self._exec_condition:
            self._exec_condition.wait_for(self._second_finish)
            printThird()
