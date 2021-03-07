# https:#leetcode.com/explore/challenge/card/march-leetcoding-challenge-2021/588/week-1-march-1st-march-7th/3663/

#  Design HashMap
# Design a HashMap without using any built-in hash table libraries.

# To be specific, your design should include these functions:

# put(key, value) : Insert a (key, value) pair into the HashMap. If the value
# already exists in the HashMap, update the value.

# get(key): Returns the value to which the specified key is mapped, or -1 if
# this map contains no mapping for the key.

# remove(key) : Remove the mapping for the value key if this map contains the
# mapping for the key.

# Example:
# MyHashMap hashMap = new MyHashMap()
# hashMap.put(1, 1)
# hashMap.put(2, 2)
# hashMap.get(1)            # returns 1
# hashMap.get(3)            # returns -1 (not found)
# hashMap.put(2, 1)          # update the existing value
# hashMap.get(2)            # returns 1
# hashMap.remove(2)          # remove the mapping for 2
# hashMap.get(2)            # returns -1 (not found)

# Note:
# All keys and values will be in the range of [0, 1000000].
# The number of operations will be in the range of [1, 10000].
# Please do not use the built-in HashMap library.

from typing import Dict, List, Optional, Protocol, Tuple
from termcolor import colored


class MyHashMap(Protocol):
    def put(self, key: int, value: int) -> None:
        ...

    def get(self, key: int) -> int:
        ...

    def remove(self, key: int) -> None:
        ...


class MyHashMap_simple_arr:
    def __init__(self) -> None:
        INITIAL_CAP = 8
        self.arr: List[Optional[int]] = []
        self.arr.extend([None] * INITIAL_CAP)

    def put(self, key: int, value: int) -> None:
        assert key >= 0, f"key must be greater or equals to 0"
        if key < len(self.arr):
            self.arr[key] = value
        else:
            size = int(key * 1.6) - len(self.arr)
            # extend arr, then add key
            self.arr.extend([None] * size)
            self.arr[key] = value

    def get(self, key: int) -> int:
        assert key >= 0, f"key must be greater or equals to 0"
        if key < len(self.arr):
            v = self.arr[key]
            return v if v is not None else -1
        else:
            return -1

    def remove(self, key: int) -> None:
        assert key >= 0, f"key must be greater or equals to 0"
        if key < len(self.arr):
            self.arr[key] = None

    def __repr__(self) -> str:
        return self.arr.__repr__()


class MyHashMap_dict:
    def __init__(self) -> None:
        self.dic: Dict[int, int] = {}

    def put(self, key: int, value: int) -> None:
        self.dic[key] = value

    def get(self, key: int) -> int:
        try:
            return self.dic[key]
        except KeyError:
            return -1

    def remove(self, key: int) -> None:
        self.dic.pop(key, None)


def test_solution() -> None:
    def test_impl(hashmap: MyHashMap) -> None:
        # hashmap.put(1, 1)
        # hashmap.put(2, 2)
        # assert 1 == hashmap.get(1)  # returns 1
        # assert -1 == hashmap.get(3)  # returns -1 (not found)
        # hashmap.put(2, 1)  # update the existing value
        # assert 1 == hashmap.get(2)  # returns 1
        # hashmap.remove(2)  # remove the mapping for 2
        # assert -1 == hashmap.get(2)  # returns -1 (not found)

        hashmap.remove(2)
        hashmap.put(3, 11)
        hashmap.put(4, 13)
        hashmap.put(15, 6)
        hashmap.put(6, 15)
        hashmap.put(8, 8)
        hashmap.put(11, 0)
        hashmap.get(11)
        hashmap.put(1, 10)
        hashmap.put(12, 14)
        print(hashmap)
    
    test_impl(MyHashMap_simple_arr())


if __name__ == "__main__":
    test_solution()
