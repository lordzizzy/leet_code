# https://medium.com/@rsinghal757/kadanes-algorithm-dynamic-programming-how-and-why-does-it-work-3fd8849ed73d

# Maximum subarray sum problem

from typing import Callable, List

from termcolor import colored


def maxSubarraySum_bruteforce(arr: List[int]) -> int:
    res, N = 0, len(arr)
    for i in range(N):
        for j in range(i + 1, N + 1):
            s = sum(arr[i:j])
            res = max(res, s)
    return res


# using kadane's algorithm:
# local_max[i] = max(arr[i], arr[i]+local_max[i-1])
#
# Time complexity: O(N)
# Space complexity: O(1)
def maxSubarraySum_kadanes_algo(arr: List[int]) -> int:
    if not arr:
        return 0

    N = len(arr)
    local_max, global_max, = (
        0,
        -1000,
    )

    for i in range(N):
        local_max = max(arr[i], arr[i] + local_max)
        global_max = local_max if local_max > global_max else global_max

    return global_max


SolutionFunc = Callable[[List[int]], int]


def test_solution(arr: List[int], expected: int) -> None:
    def test_impl(func: SolutionFunc, arr: List[int], expected: int) -> None:
        r = func(arr)
        if r == expected:
            print(
                colored(
                    f"PASSED {func.__name__} => Max subarray sum of {arr} is {r}",
                    "green",
                )
            )
        else:
            print(
                colored(
                    f"FAILED {func.__name__} => Max subarray sum of {arr} is {r} but expected {expected}",
                    "red",
                )
            )

    test_impl(maxSubarraySum_bruteforce, arr, expected)
    test_impl(maxSubarraySum_kadanes_algo, arr, expected)


if __name__ == "__main__":
    test_solution(arr=[], expected=0)
    test_solution(arr=[-2, 1, -3, 4, -1, 2, 1, -5, 4], expected=6)
