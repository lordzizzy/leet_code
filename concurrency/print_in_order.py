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

import random

from typing import Callable, List, Protocol
from threading import Barrier, Lock, Event, Semaphore, Condition, Thread

from termcolor import colored


class Foo(Protocol):
    def first(self, printFirst: Callable[[], None]) -> None:
        ...

    def second(self, printSecond: Callable[[], None]) -> None:
        ...

    def third(self, printThird: Callable[[], None]) -> None:
        ...


class Foo_Unsynched(Foo):
    def __init__(self):
        pass

    def first(self, printFirst: Callable[[], None]) -> None:
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()

    def second(self, printSecond: Callable[[], None]) -> None:
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()

    def third(self, printThird: Callable[[], None]) -> None:
        # printThird() outputs "third". Do not change or remove this line.
        printThird()


class Foo_Barrier(Foo):
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


class Foo_Locks(Foo):
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


class Foo_Event(Foo):
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


class Foo_Semaphore(Foo):
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


class Foo_Condition(Foo):
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


global_data: List[str] = []


def printFirst():
    global_data.extend(list("first"))


def printSecond():
    global_data.extend(list("second"))


def printThird():
    global_data.extend(list("third"))


def test_solution(orders: List[int], expected: str) -> None:
    def test_impl(foo: Foo, input: List[int], expected: str) -> None:
        threads: List[Thread] = []
        funcs = [
            (foo.first, printFirst),
            (foo.second, printSecond),
            (foo.third, printThird),
        ]
        global_data.clear()

        for i in orders:
            if 0 > i or i > len(funcs):
                raise AssertionError(
                    f"Order must be great or equal to 1 and less than {len(funcs)} intead of {i}"
                )
            func, arg = funcs[i - 1]
            t = Thread(target=func, args=(arg,))
            threads.append(t)
            t.start()

        for _, t in enumerate(threads):
            t.join()

        output = "".join(global_data)
        if output == expected:
            print(
                colored(
                    f"PASSED {foo} => print orders {orders} output is {output}", "green"
                )
            )
        else:
            print(
                colored(
                    f"FAILED {foo} => print orders {orders} output is {output}, but expected: {expected}",
                    "red",
                )
            )

    test_impl(
        Foo_Unsynched(), orders, expected
    )  # this will pass ocasionally because of race conditions

    test_impl(Foo_Barrier(), orders, expected)


if __name__ == "__main__":
    test_solution(orders=[1, 2, 3], expected="firstsecondthird")
    test_solution(orders=[1, 3, 2], expected="firstsecondthird")
    test_solution(orders=[2, 1, 3], expected="firstsecondthird")
    test_solution(orders=[3, 2, 1], expected="firstsecondthird")
