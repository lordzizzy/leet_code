# Peeking Iterator
# Given an Iterator class interface with methods: next() and hasNext(), design and implement a PeekingIterator that support the peek() operation -- it essentially peek() at the element that will be returned by the next call to next().

# Example:
# Assume that the iterator is initialized to the beginning of the list: [1,2,3].
# Call next() gets you 1, the first element in the list.
# Now you call peek() and it returns 2, the next element. Calling next() after that still return 2.
# You call next() the final time and it returns 3, the last element.
# Calling hasNext() after that should return false.
# Follow up: How would you extend your design to be generic and work with all types, not just integer?

# Below is the interface for Iterator, which is already defined for you.
#

from typing import List
from termcolor import colored


class Iterator:
    def __init__(self, nums: List[int]):
        """
        Initializes an iterator object to the beginning of a list.
        :type nums: List[int]
        """
        self._idx = 0
        self._nums = nums

    def hasNext(self):
        """
        Returns true if the iteration has more elements.
        :rtype: bool
        """
        return self._idx < len(self._nums)

    def next(self):
        """
        Returns the next element in the iteration.
        :rtype: int
        """
        if self.hasNext():
            res = self._nums[self._idx]
            self._idx += 1
            return res
        else:
            raise StopIteration()


class PeekingIterator:
    def __init__(self, iterator: Iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self._it = iterator
        self._peeked = False
        self._peekElem = None

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if not self._peeked:
            self._peekElem = self._it.next()
            self._peeked = True
        return self._peekElem

    def next(self):
        """
        :rtype: int
        """
        if not self._peeked:
            return self._it.next()
        res = self._peekElem
        self._peeked = False
        self._peekElem = None
        return res

    def hasNext(self):
        """
        :rtype: bool
        """
        return self._peeked or self._it.hasNext()


# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].

def test_solution():
    nums = [1, 2, 3]
    iter: PeekingIterator = PeekingIterator(Iterator(nums))
    while iter.hasNext():
        # Get the next element but not advance the iterator.
        peeked = iter.peek()
        next = iter.next()         # Should return the same value as [val].
        if peeked == next:
            print(colored(
                f"PASSED => peek value({peeked}) is same as next value({next})", "green"))
        else:
            print(
                colored(f"FAILED: peek value {peeked} is different from next value: {next}.", "red"))


if __name__ == "__main__":
    test_solution()
