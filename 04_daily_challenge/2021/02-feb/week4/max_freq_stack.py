# https://leetcode.com/problems/maximum-frequency-stack/discuss/1086287/Python-2-solutions%3A-O(log-n)-and-O(1)-explained

from typing import DefaultDict, List, Tuple


class FreqStack_logN_push_pop_time:
    def __init__(self):
        self._stack: List[Tuple[int, int, int]] = []
        self._places = DefaultDict[int, List[int]](
            lambda: []
        )  # num -> list of indexes for that num
        self._cnt = 0

    def push(self, x: int) -> None:
        freq = len(self._places[x])
        if freq > 0:
            self._stack.remove((freq, self._places[x][-1], x))
        self._stack.append((freq + 1, self._cnt, x))
        self._stack.sort()
        self._places[x].append(self._cnt)
        self._cnt += 1

    def pop(self) -> int:
        freq, _, num = self._stack.pop()
        self._places[num].pop()
        if freq > 1:
            self._stack.append((freq - 1, self._places[num][-1], num))
        self._stack.sort()
        return num

class FreqStack_optimized_o_1_time:
    def __init__(self):
        self._freqs = DefaultDict[int, int](lambda: 0)
        self._groups = DefaultDict[int, List[int]](lambda: [])
        self._maxFreq = 0 
        
    def push(self, num: int) -> None:
        freq = self._freqs[num] + 1
        self._freqs[num] = freq
        if freq > self._maxFreq:
            self._maxFreq = freq
        self._groups[freq].append(num)
        
    def pop(self) -> int:
        if self._maxFreq <= 0:
            raise ValueError()
        num = self._groups[self._maxFreq].pop()
        self._freqs[num] -= 1
        if not self._groups[self._maxFreq]:
            self._maxFreq -=1
        return num


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()