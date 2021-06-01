# https://leetcode.com/explore/challenge/card/may-leetcoding-challenge-2021/602/week-5-may-29th-may-31st/3762/

# Search Suggestions System
# Given an array of strings products and a string searchWord. We want to design
# a system that suggests at most three product names from products after each
# character of searchWord is typed. Suggested products should have common
# prefix with the searchWord. If there are more than three products with a
# common prefix return the three lexicographically minimums products.

# Return list of lists of the suggested products after each character of
# searchWord is typed.

# Example 1:
# Input: products = ["mobile","mouse","moneypot","monitor","mousepad"],
# searchWord = "mouse"
# Output: [
# ["mobile","moneypot","monitor"],
# ["mobile","moneypot","monitor"],
# ["mouse","mousepad"],
# ["mouse","mousepad"],
# ["mouse","mousepad"]
# ]
# Explanation: products sorted lexicographically =
# ["mobile","moneypot","monitor","mouse","mousepad"]
# After typing m and mo all products match and we show user
# ["mobile","moneypot","monitor"]
# After typing mou, mous and mouse the system suggests ["mouse","mousepad"]

# Example 2:
# Input: products = ["havana"], searchWord = "havana"
# Output: [["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]

# Example 3:
# Input: products = ["bags","baggage","banner","box","cloths"], searchWord =
# "bags"
# Output:
# [["baggage","bags","banner"],["baggage","bags","banner"],["baggage","bags"],["bags"]]

# Example 4:
# Input: products = ["havana"], searchWord = "tatiana"
# Output: [[],[],[],[],[],[],[]]

# Constraints:
# 1 <= products.length <= 1000
# There are no repeated elements in products.
# 1 <= Σ products[i].length <= 2 * 10^4
# All characters of products[i] are lower-case English letters.
# 1 <= searchWord.length <= 1000
# All characters of searchWord are lower-case English letters.

from typing import Callable, List, Optional
from termcolor import colored
from bisect import bisect_left


class Trie:
    def __init__(self) -> None:
        self.next: List[Optional[Trie]] = [None] * 26
        self.words: List[int] = []


class Solution:
    def suggestedProducts(
        self, products: List[str], searchWord: str
    ) -> List[List[str]]:
        return self.suggestedProducts_trie(products, searchWord)

    # use a specially crafted trie class that keeps the list of indexes of
    # words at every node starting from first character
    # NOTE: this is a trade off for memory vs dfs searching to the end of each
    # word. we store the index to the sorted words to save memory.
    # based on idea from:
    # https://leetcode.com/problems/search-suggestions-system/discuss/440474/Java-trie-explained-clean-code-14ms
    def suggestedProducts_trie(
        self, products: List[str], searchWord: str
    ) -> List[List[str]]:
        words = sorted(products)
        root = Trie()
        for i, word in enumerate(words):
            node = root
            for c in word:
                idx = ord(c) - ord("a")
                if node.next[idx] is None:
                    node.next[idx] = Trie()
                node = node.next[idx]
                if len(node.words) < 3:
                    node.words.append(i)

        # search
        res: List[List[str]] = []
        node = root
        for i, c in enumerate(searchWord):
            idx = ord(c) - ord("a")
            node: Optional[Trie] = node.next[idx]
            if node is not None:
                res.append([words[i] for i in node.words])
            else:
                # means no more matches possible so just extend with empty lists
                res.extend([[] for _ in range(len(searchWord) - i)])
                break
        return res

    def suggestedProducts_binarysearch(
        self, products: List[str], searchWord: str
    ) -> List[List[str]]:
        words = sorted(products)
        i = 0
        prefix = ""
        res: List[List[str]] = []
        for c in searchWord:
            prefix += c
            i = bisect_left(words, prefix, i)
            res.append([w for w in words[i : i + 3] if w.startswith(prefix)])
        return res


SolutionFunc = Callable[[List[str], str], List[List[str]]]


def test_solution(
    products: List[str], searchWord: str, expected: List[List[str]]
) -> None:
    def test_impl(
        func: SolutionFunc,
        products: List[str],
        searchWord: str,
        expected: List[List[str]],
    ) -> None:
        r = func(products, searchWord)
        if r == expected:
            print(
                colored(
                    f"PASSED {func.__name__} => Search suggestions for {searchWord} in {products} are {r}",
                    "green",
                )
            )
        else:
            print(
                colored(
                    f"FAILED {func.__name__} => Search suggestions for {searchWord} in {products} are {r} but expected {expected}",
                    "red",
                )
            )

    sln = Solution()
    test_impl(sln.suggestedProducts_trie, products, searchWord, expected)
    test_impl(sln.suggestedProducts_binarysearch, products, searchWord, expected)


if __name__ == "__main__":
    test_solution(
        products=["mobile", "mouse", "moneypot", "monitor", "mousepad"],
        searchWord="mouse",
        expected=[
            ["mobile", "moneypot", "monitor"],
            ["mobile", "moneypot", "monitor"],
            ["mouse", "mousepad"],
            ["mouse", "mousepad"],
            ["mouse", "mousepad"],
        ],
    )

    test_solution(
        products=["havana"],
        searchWord="havana",
        expected=[
            ["havana"],
            ["havana"],
            ["havana"],
            ["havana"],
            ["havana"],
            ["havana"],
        ],
    )

    test_solution(
        products=["bags", "baggage", "banner", "box", "cloths"],
        searchWord="bags",
        expected=[
            ["baggage", "bags", "banner"],
            ["baggage", "bags", "banner"],
            ["baggage", "bags"],
            ["bags"],
        ],
    )

    test_solution(
        products=["havana"],
        searchWord="tatiana",
        expected=[[], [], [], [], [], [], []],
    )
