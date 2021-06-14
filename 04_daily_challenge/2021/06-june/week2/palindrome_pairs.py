# https://leetcode.com/explore/challenge/card/june-leetcoding-challenge-2021/604/week-2-june-8th-june-14th/3777/

# Palindrome Pairs

# Solution
# Given a list of unique words, return all the pairs of the distinct indices
# (i, j) in the given list, so that the concatenation of the two words words[i]
# + words[j] is a palindrome.

# Example 1:
# Input: words = ["abcd","dcba","lls","s","sssll"]
# Output: [[0,1],[1,0],[3,2],[2,4]]
# Explanation: The palindromes are ["dcbaabcd","abcddcba","slls","llssssll"]

# Example 2:
# Input: words = ["bat","tab","cat"]
# Output: [[0,1],[1,0]]
# Explanation: The palindromes are ["battab","tabbat"]

# Example 3:
# Input: words = ["a",""]
# Output: [[0,1],[1,0]]

# Constraints:
# 1 <= words.length <= 5000
# 0 <= words[i].length <= 300
# words[i] consists of lower-case English letters.

from __future__ import annotations

from typing import Callable, List, Optional

from termcolor import colored


class TrieNode:
    def __init__(self) -> None:
        self.next: List[Optional[TrieNode]] = [None] * 26
        self.index = -1
        self.candidate_indexes: List[int] = []


class Solution:
    # Time complexity: O(N^2*K), Space complexity O(1)
    def palindromePairs_bruteforce(self, words: List[str]) -> List[List[int]]:
        def is_palindrome(word: str) -> bool:
            l, r = 0, len(word) - 1
            while l < r:
                if word[l] != word[r]:
                    return False
                l += 1
                r -= 1
            return True

        res: List[List[int]] = []

        for i, w1 in enumerate(words):
            for j, w2 in enumerate(words):
                if i != j:
                    if is_palindrome(w1 + w2):
                        res.append([i, j])

        return res

    # References
    # https://leetcode.com/problems/palindrome-pairs/discuss/79195/O(n-*-k2)-java-solution-with-Trie-structure
    # http://www.allenlipeng47.com/blog/index.php/2016/03/15/palindrome-pairs/
    # 
    # Time complexity: O(N * K^2), Space complexity: O(N*26K^2)
    def palindromePairs_reverse_trie(self, words: List[str]) -> List[List[int]]:
        def is_palindrome(word: str) -> bool:
            l, r = 0, len(word) - 1
            while l < r:
                if word[l] != word[r]:
                    return False
                l += 1
                r -= 1
            return True

        def add_word(root: TrieNode, word: str, index: int) -> None:
            for i in reversed(range(len(word))):
                c = ord(word[i]) - ord("a")
                if not root.next[c]:
                    root.next[c] = TrieNode()
                if is_palindrome(word[:i]):
                    root.candidate_indexes.append(index)
                root = root.next[c]

            root.index = index
            root.candidate_indexes.append(index)

        def search(root: TrieNode, index: int) -> None:
            nonlocal res
            candidate = words[index]
            for j in range(len(candidate)):
                if (
                    root.index >= 0
                    and root.index != index
                    and is_palindrome(candidate[j:])
                ):
                    res.append([index, root.index])

                c = ord(candidate[j]) - ord("a")
                root = root.next[c]
                if not root:
                    return

            for j in root.candidate_indexes:
                if j == index:
                    continue
                res.append([index, j])

        res: List[List[int]] = []
        root = TrieNode()

        for i, word in enumerate(words):
            add_word(root, word, i)

        for i, word in enumerate(words):
            search(root, i)

        return res


SolutionFunc = Callable[[List[str]], List[List[int]]]


def test_solution(words: List[str], expected: List[List[int]]) -> None:
    def test_impl(
        func: SolutionFunc, words: List[str], expected: List[List[int]]
    ) -> None:
        r = func(words)
        if sorted(r) == sorted(expected):
            print(
                colored(
                    f"PASSED {func.__name__} => Pairs of distinct indices in {words} is {r}",
                    "green",
                )
            )
        else:
            print(
                colored(
                    f"FAILED {func.__name__} => Pairs of distinct indices in {words} is {r} but expected {expected}",
                    "red",
                )
            )

    sln = Solution()
    test_impl(sln.palindromePairs_bruteforce, words, expected)
    test_impl(sln.palindromePairs_reverse_trie, words, expected)


if __name__ == "__main__":
    test_solution(
        words=["abcd", "dcba", "lls", "s", "sssll"],
        expected=[[0, 1], [1, 0], [3, 2], [2, 4]],
    )
    test_solution(words=["bat", "tab", "cat"], expected=[[0, 1], [1, 0]])
    test_solution(words=["a", ""], expected=[[0, 1], [1, 0]])
