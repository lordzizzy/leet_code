# https://leetcode.com/explore/challenge/card/june-leetcoding-challenge-2021/604/week-2-june-8th-june-14th/3774/

# You are implementing a program to use as your calendar. We can add a new
# event if adding the event will not cause a double booking.

# A double booking happens when two events have some non-empty intersection
# (i.e., some moment is common to both events.).

# The event can be represented as a pair of integers start and end that
# represents a booking on the half-open interval [start, end), the range of
# real numbers x such that start <= x < end.

# Implement the MyCalendar class:

# MyCalendar() Initializes the calendar object.
# boolean book(int start, int end) Returns true if the event can be added to
# the calendar successfully without causing a double booking. Otherwise, return
# false and do not add the event to the calendar.

# Example 1:
# Input
# ["MyCalendar", "book", "book", "book"]
# [[], [10, 20], [15, 25], [20, 30]]
# Output
# [None, true, false, true]

# Explanation
# MyCalendar myCalendar = new MyCalendar();
# myCalendar.book(10, 20); // return True
# myCalendar.book(15, 25); // return False, It can not be booked because time
# 15 is already booked by another event.
# myCalendar.book(20, 30); // return True, The event can be booked, as the
# first event takes every time less than 20, but not including 20.

# Constraints:
# 0 <= start < end <= 10⁹
# At most 1000 calls will be made to book.

from dataclasses import dataclass
from typing import List, Protocol, Tuple

from termcolor import colored


class MyCalendar(Protocol):
    def book(self, start: int, end: int) -> bool:
        ...


class MyCalendar_bruteforce(MyCalendar):
    def __init__(self):
        self.bookings: List[Tuple[int, int]] = []

    def book(self, start: int, end: int) -> bool:
        for s, e in self.bookings:
            if start < e and s < end:
                return False
        self.bookings.append((start, end))
        return True


@dataclass(order=True)
class CallInfo:
    start: int
    end: int
    expected: int


def test_solution(call_infos: List[CallInfo]) -> None:
    def test_impl(cal: MyCalendar, call_infos: List[CallInfo]) -> None:
        for c in call_infos:
            r = cal.book(c.start, c.end)
            if r == c.expected:
                print(
                    colored(
                        f"PASSED {type(cal).__name__}.{cal.book.__name__}(start={c.start}, end={c.end}) => bookable is {r}",
                        "green",
                    )
                )
            else:
                print(
                    colored(
                        f"FAILED {type(cal).__name__}.{cal.book.__name__}(start={c.start}, end={c.end}) => bookable is {r} but expected {c.expected}",
                        "red",
                    )
                )

    test_impl(MyCalendar_bruteforce(), call_infos)


if __name__ == "__main__":
    test_solution(
        call_infos=[
            CallInfo(start=10, end=20, expected=True),
            CallInfo(start=15, end=25, expected=False),
            CallInfo(start=20, end=30, expected=True),
        ]
    )
