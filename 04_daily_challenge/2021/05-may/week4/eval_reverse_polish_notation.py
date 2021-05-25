# https://leetcode.com/explore/challenge/card/may-leetcoding-challenge-2021/601/week-4-may-22nd-may-28th/3755/

# Evaluate Reverse Polish Notation
# Evaluate the value of an arithmetic expression in Reverse Polish Notation.

# Valid operators are +, -, *, and /. Each operand may be an integer or another
# expression.

# Note that division between two integers should truncate toward zero.

# It is guaranteed that the given RPN expression is always valid. That means
# the expression would always evaluate to a result, and there will not be any
# division by zero operation.

# Example 1:
# Input: tokens = ["2","1","+","3","*"]
# Output: 9
# Explanation: ((2 + 1) * 3) = 9

# Example 2:
# Input: tokens = ["4","13","5","/","+"]
# Output: 6
# Explanation: (4 + (13 / 5)) = 6

# Example 3:
# Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
# Output: 22
# Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
# = ((10 * (6 / (12 * -11))) + 17) + 5
# = ((10 * (6 / -132)) + 17) + 5
# = ((10 * 0) + 17) + 5
# = (0 + 17) + 5
# = 17 + 5
# = 22


# Constraints:
# 1 <= tokens.length <= 10⁴
# tokens[i] is either an operator: "+", "-", "*", or "/", or an integer in the
# range [-200, 200].

from typing import Callable, Dict, List
from termcolor import colored


MathOp = Callable[[int, int], int]


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        return self.evalRPN_stack(tokens)

    def evalRPN_stack(self, tokens: List[str]) -> int:
        operators: Dict[str, MathOp] = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: int(a / b),
        }
        stack: List[int] = []

        for token in tokens:
            op = operators.get(token)
            if op:
                r = stack.pop()
                l = stack.pop()
                stack.append(op(l, r))
            else:
                stack.append(int(token))

        return stack.pop()


SolutionFunc = Callable[[List[str]], int]


def test_solution(tokens: List[str], expected: int) -> None:
    def test_impl(func: SolutionFunc, tokens: List[str], expected: int) -> None:
        r = func(tokens)
        if r == expected:
            print(
                colored(
                    f"PASSED {func.__name__} => RPN expression {tokens} evaluate to {r}",
                    "green",
                )
            )
        else:
            print(
                colored(
                    f"FAILED {func.__name__} => RPN expression {tokens} evaluate to {r} but expected {expected}",
                    "red",
                )
            )

    sln = Solution()
    test_impl(sln.evalRPN, tokens, expected)


if __name__ == "__main__":
    test_solution(tokens=["2", "1", "+", "3", "*"], expected=9)
    test_solution(tokens=["4", "13", "5", "/", "+"], expected=6)
    test_solution(
        tokens=["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"],
        expected=22,
    )
