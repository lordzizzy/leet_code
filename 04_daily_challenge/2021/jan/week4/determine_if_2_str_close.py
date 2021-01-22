
# https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/582/week-4-january-22nd-january-28th/3613/

# Determine if Two Strings Are Close

# Two strings are considered close if you can attain one from the other using the following operations:

# Operation 1: Swap any two existing characters.
# For example, abcde -> aecdb

# Operation 2: Transform every occurrence of one existing character into another existing character, and do the same with the other character.
# For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)

# You can use the operations on either string as many times as necessary.
# Given two strings, word1 and word2, return true if word1 and word2 are close, and false otherwise.

# Example 1:
# Input: word1 = "abc", word2 = "bca"
# Output: true
# Explanation: You can attain word2 from word1 in 2 operations.
# Apply Operation 1: "abc" -> "acb"
# Apply Operation 1: "acb" -> "bca"

# Example 2:
# Input: word1 = "a", word2 = "aa"
# Output: false
# Explanation: It is impossible to attain word2 from word1, or vice versa, in any number of operations.

# Example 3:
# Input: word1 = "cabbba", word2 = "abbccc"
# Output: true
# Explanation: You can attain word2 from word1 in 3 operations.
# Apply Operation 1: "cabbba" -> "caabbb"
# Apply Operation 2: "caabbb" -> "baaccc"
# Apply Operation 2: "baaccc" -> "abbccc"

# Example 4:
# Input: word1 = "cabbba", word2 = "aabbss"
# Output: false
# Explanation: It is impossible to attain word2 from word1, or vice versa, in any amount of operations.


# Constraints:
# 1 <= word1.length, word2.length <= 10^5
# word1 and word2 contain only lowercase English letters.

from termcolor import colored


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2): 
            return False

        map1 = self.buildMap(word1)
        map2 = self.buildMap(word2)

        # for any operation 1s, both map should have the same keys
        r1 = (map1.keys() == map2.keys())

        values1 = list(map1.values())
        values1.sort()
        values2 = list(map2.values())
        values2.sort()
        
        # for any operation 2s, the unordered numbers in the value list must be the same        
        r2 = values1 == values2

        return r1 and r2

    def buildMap(self, word: str) -> dict:
        map = {}
        for char in word:
            if count := map.get(char):
                map[char] = count + 1
            else:
                map[char] = 1
        return map


def test_Solution(word1: str, word2: str, expected: bool):
    sln = Solution()
    r = sln.closeStrings(word1, word2)
    if r == expected:
        print(colored(f"PASSED - {word1} is close to {word2}: {r}", "green"))
    else:
        print(colored(
            f"FAILED - {word1} is close to {word2}: {r} but expected: {expected}", "red"))


if __name__ == "__main__":
    test_Solution(word1="abc", word2="bca", expected=True)
    test_Solution(word1="a", word2="aa", expected=False)
    test_Solution(word1="cabbba", word2="abbccc", expected=True)
    test_Solution(word1="abbzccca", word2="babzzczc", expected=True)
