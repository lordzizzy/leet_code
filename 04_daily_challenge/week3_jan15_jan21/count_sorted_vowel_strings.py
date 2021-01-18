
class Solution:
    def __init__(self):
        self.cache = {}

    def countVowelStrings(self, n: int):
        r = self.count(n, 5)
        # print(self.cache)
        return r

    def count(self, n: int, c: int):
        if n == 1:
            return c
        # case of any string N that starts with "u" is always 1
        if c == 1:
            return 1
        total = 0
        n -= 1
        # we only need to loop from 2 <= c <= 5 because when c == 1, the result is just 1
        while (c > 1):
            key = n * 10 + c
            if r := self.cache.get(key):
                total += r
            else:
                r = self.cache[key] = self.count(n, c)
                total += r
            c -= 1
        # finally just add 1 for the c == 1 case
        return total + 1


def checkSolution(n: int, expected: int):
    s = Solution()
    count = s.countVowelStrings(n)
    assert count == expected, \
        f"count: {count} but expected: {expected}"


if __name__ == "__main__":
    checkSolution(n=1, expected=5)
    checkSolution(n=2, expected=15)
    checkSolution(n=33, expected=66045)
