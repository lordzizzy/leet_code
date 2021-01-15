
from typing import List
from termcolor import colored

import termplotlib as tpl
import numpy as np


class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1

        nums = [0] * (n+1)
        nums[0], nums[1] = 0, 1
        maxNum = 1
        for i in range(2, len(nums)):
            if i % 2:
                #odd
                nums[i] = nums[(i-1)//2] + nums[(i+1)//2]
            else:
                #even
                nums[i] = nums[i//2]
            maxNum = max(maxNum, nums[i])
        return maxNum


def genArray(n: int) -> List[int]:
    if n == 0:
        return []
    if n == 1:
        return [0]

    nums = [0] * (n+1)
    nums[0], nums[1] = 0, 1

    for i in range(2, len(nums)):
        if i % 2:
            #odd
            nums[i] = nums[(i-1)//2] + nums[(i+1)//2]
        else:
            #even
            nums[i] = nums[i//2]

    return nums


def printArray(nums: List[int]):
    for i, num in enumerate(nums, 0):
        if i % 2:
            print(colored(f'idx-{i}= {num}', 'red'))
        else:
            print(f'idx-{i}= {num}')


def printArrayOneLine(nums: List[int]):
    for i, num in enumerate(nums, 0):
        if i % 2:
            print(colored(f'{num},', 'red'), end=" ")
        else:
            print(f'{num},', end=" ")


def plotArrayGraph(nums: List[int]):
    x = np.arange(0, len(nums))
    y = nums
    fig = tpl.figure()
    fig.plot(x, y, width=150, height=20)
    fig.show()


def checkArray(nums: List[int]):
    for i, num in enumerate(nums, 0):
        if (i > 0) and (i % 2 == 0):
            assert nums[i] <= nums[i-1], \
                "even element is bigger than the odd element preceding it!"


def checkSolution(n: int, expected: int):
    s = Solution()
    maxNum = s.getMaximumGenerated(n)
    assert expected == maxNum, f"wrong value:{maxNum}, expected value: {expected}"


if __name__ == "__main__":
    checkSolution(n=0, expected=0)
    checkSolution(n=1, expected=1)
    checkSolution(n=2, expected=1)
    checkSolution(n=3, expected=2)
    checkSolution(n=7, expected=3)
    checkSolution(n=100, expected=21)

    # printArrayOneLine(genArray(100))
    printArray(genArray(100))
