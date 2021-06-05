# https://leetcode.com/explore/challenge/card/june-leetcoding-challenge-2021/603/week-1-june-1st-june-7th/3767/

# Open the Lock
# You have a lock in front of you with 4 circular wheels. Each wheel has 10
# slots: '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'. The wheels can
# rotate freely and wrap around: for example we can turn '9' to be '0', or '0'
# to be '9'. Each move consists of turning one wheel one slot.

# The lock initially starts at '0000', a string representing the state of the 4
# wheels.

# You are given a list of deadends dead ends, meaning if the lock displays any
# of these codes, the wheels of the lock will stop turning and you will be
# unable to open it.

# Given a target representing the value of the wheels that will unlock the
# lock, return the minimum total number of turns required to open the lock, or
# -1 if it is impossible.


# Example 1:
# Input: deadends = ["0201","0101","0102","1212","2002"], target = "0202"
# Output: 6
# Explanation:
# A sequence of valid moves would be "0000" -> "1000" -> "1100" -> "1200" ->
# "1201" -> "1202" -> "0202".
# Note that a sequence like "0000" -> "0001" -> "0002" -> "0102" -> "0202"
# would be invalid,
# because the wheels of the lock become stuck after the display becomes the
# dead end "0102".

# Example 2:
# Input: deadends = ["8888"], target = "0009"
# Output: 1
# Explanation:
# We can turn the last wheel in reverse to move from "0000" -> "0009".

# Example 3:
# Input: deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"],
# target = "8888"
# Output: -1
# Explanation:
# We can't reach the target without getting stuck.

# Example 4:
# Input: deadends = ["0000"], target = "8888"
# Output: -1

# Constraints:
# 1 <= deadends.length <= 500
# deadends[i].length == 4
# target.length == 4
# target will not be in the list deadends.
# target and deadends[i] consist of digits only

from typing import Callable, List
from termcolor import colored
from collections import deque


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        return self.openLock_bfs(deadends, target)

    def openLock_bfs(self, deadends: List[str], target: str) -> int:
        def neighbours(seq: str) -> List[str]:
            res: List[str] = []
            for i, ch in enumerate(seq):
                num = int(ch)
                res.append(seq[:i] + str((num - 1) % 10) + seq[i + 1 :])
                res.append(seq[:i] + str((num + 1) % 10) + seq[i + 1 :])
            return res

        depth = -1
        visited, q = set(deadends), deque(["0000"])

        while q:
            depth += 1
            for _ in range(len(q)):
                node = q.popleft()
                if node == target:
                    return depth
                if node in visited:
                    continue
                visited.add(node)
                q.extend(neighbours(node))
        return -1

    def openLock_fast(self, deadends: List[str], target: str) -> int:
        def int_to_str(n: int) -> str:
            s = str(abs(n))
            zero = (4 - len(s)) * "0"
            return zero + s

        def next_n(current_lock):
            def dead_test(add_n):
                nonlocal update_lock
                idx = -(len(str(abs(add_n))))
                lock = 10 ** abs(idx + 1) * int(update_lock[idx])
                temp = lock + add_n
                temp = int_to_str(temp)

                test_lock = update_lock[:]
                test_lock[idx] = temp[idx]

                if "".join(test_lock) in deadends:
                    return False
                update_lock = test_lock
                self.count += 1
                return True

            def add_num(idx):
                nonlocal update_lock
                n = update_lock[idx]
                t = 10 ** abs(idx + 1) if n > "5" else -(10 ** abs(idx + 1))
                if n == "0":
                    if update_lock == current_lock:
                        hold.append(t)  # 暫存其他可以動的選擇
                        hold.append(-t)
                    return

                ok = dead_test(t)
                if not ok:
                    if update_lock == current_lock:
                        good_move.append(t)
                        hold.append(-t)
                return

            def clean_good_moves():
                nonlocal good_move
                while good_move:
                    pass_ = 0
                    for n in good_move:
                        ok = dead_test(n)
                        if ok:
                            pass_ += 1
                            good_move.remove(n)
                    if pass_ == 0:
                        break
                return

            # ----------------function code start
            # count = 0
            update_lock = current_lock[:]
            good_move = []
            hold = []
            for i in range(-4, 0):
                add_n = add_num(i)

            if update_lock != current_lock:
                clean_good_moves()
                return update_lock

            # print('not found good match, look for optional matches.')
            if not hold:
                return False

            while hold:
                add_n = hold.pop()
                ok = dead_test(add_n)
                if not ok:
                    continue

                clean_good_moves()

                if update_lock == current_lock:
                    return False
                return update_lock

        # ---------------start from target
        self.count = 0
        target = list(target)
        if "0000" in deadends:
            return -1

        while target != ["0"] * 4:
            target = next_n(target)
            if not target:
                return -1

        return self.count


SolutionFunc = Callable[[List[str], str], int]


def test_solution(deadends: List[str], target: str, expected: int) -> None:
    def test_impl(
        func: SolutionFunc, deadends: List[str], target: str, expected: int
    ) -> None:
        r = func(deadends, target)
        if r == expected:
            print(
                colored(
                    f"PASSED {func.__name__} => Min moves to open lock of target:{target} with deadends: {deadends} is {r}",
                    "green",
                )
            )
        else:
            print(
                colored(
                    f"FAILED {func.__name__} => Min moves to open lock of target:{target} with deadends: {deadends} is {r} but expected {expected}",
                    "red",
                )
            )

    sln = Solution()
    test_impl(sln.openLock_bfs, deadends, target, expected)
    
    test_impl(sln.openLock_fast, deadends, target, expected)


if __name__ == "__main__":
    test_solution(deadends=["8888"], target="0009", expected=1)
    test_solution(
        deadends=["8887", "8889", "8878", "8898", "8788", "8988", "7888", "9888"],
        target="8888",
        expected=-1,
    )
    test_solution(deadends=["0000"], target="8888", expected=-1)
