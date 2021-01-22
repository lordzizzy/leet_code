# https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/581/week-3-january-15th-january-21st/3610/

# Valid Parentheses
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.

# Example 1:
# Input: s = "()"
# Output: true

# Example 2:
# Input: s = "()[]{}"
# Output: true

# Example 3:
# Input: s = "(]"
# Output: false

# Example 4:
# Input: s = "([)]"
# Output: false

# Example 5:
# Input: s = "{[]}"
# Output: true


# Constraints:
# 1 <= s.length <= 10^4
# s consists of parentheses only '()[]{}'.


# 8ms solution
# class Solution:
#     def isValid(self, s: str) -> bool:
#         ob = []
#         brackets = {'(':')', '{':'}', '[':']'}
#         for bracket in s:
#             if bracket in brackets:
#                 ob.append(bracket)
#                 continue
#             if not ob:
#                 return False
#             b = ob.pop()
#             if bracket != brackets[b]:
#                 return False
#         return not ob

class Solution:

    def isValid(self, s: str) -> bool:
        parens = {"(": 1, ")": -1, "{": 2, "}": -2, "[": 3, "]": -3}
        stack = [0] * len(s)
        ptr = -1

        for c in s:
            val = parens.get(c)
            if val is None:
                # not a parenthese
                continue

            if ptr == -1:
                if val < 0:
                    return False
                else:                
                    ptr = 0
                    stack[0] = val
                continue

            result = stack[ptr] + val
            if result == 0:
                ptr -= 1
            elif result > 0:
                ptr += 1
                stack[ptr] = val
            else:
                return False

        return ptr == -1


def checkSolution(s: str, expected: bool):
    sln = Solution()
    r = sln.isValid(s)
    assert r == expected, f"Result is {r} but expected is {expected}"
    print(f"Passed: {s} has valid parentheses is {expected}")


if __name__ == "__main__":
    checkSolution(s="()", expected=True)
    checkSolution(s="()[]{}", expected=True)
    checkSolution(s="(]", expected=False)
    checkSolution(s="([)", expected=False)
    checkSolution(s="{[]}", expected=True)
    checkSolution(s="({[]})", expected=True)
    checkSolution(s="}{", expected=False)
    checkSolution(s="(){}{", expected=False)
    
