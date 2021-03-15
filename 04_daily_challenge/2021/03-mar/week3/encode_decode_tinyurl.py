# https://leetcode.com/explore/challenge/card/march-leetcoding-challenge-2021/590/week-3-march-15th-march-21st/3673/

#  Encode and Decode TinyURL
# Note: This is a companion problem to the System Design problem: Design
# TinyURL.

# TinyURL is a URL shortening service where you enter a URL such as
# https://leetcode.com/problems/design-tinyurl and it returns a short URL such
# as http://tinyurl.com/4e9iAk.


# Design the encode and decode methods for the TinyURL service. There is no
# restriction on how your encode/decode algorithm should work. You just need to
# ensure that a URL can be encoded to a tiny URL and the tiny URL can be
# decoded to the original URL.

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))


from typing import Dict, Protocol
from termcolor import colored

import random


class Codec(Protocol):
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL."""
        ...

    def decode(self, shortUrl: str) -> str:
        ...


# https://leetcode.com/problems/encode-and-decode-tinyurl/discuss/1110575/(Python)-Simple-and-Easy-Solution
class Codec_random:
    def __init__(self) -> None:
        self.map: Dict[str, str] = {}
        self.primary = 1

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL."""
        chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        key = ""
        for _ in range(6):
            key += chars[random.randint(0, len(chars) - 1)]

        if key in self.map:
            key += str(self.primary)
            self.primary += 1

        self.map[key] = longUrl
        return key

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL."""
        return self.map[shortUrl]


def test_solution(url: str) -> None:
    def test_impl(codec: Codec, url: str) -> None:
        r = codec.encode(url)
        if codec.decode(r) == url:
            print(
                colored(f"PASSED {codec.__class__} => {url} shortened to {r}", "green")
            )
        else:
            print(
                colored(
                    f"FAILED {codec.__class__} => {url} shortened to {r} but failed decode",
                    "red",
                )
            )

    test_impl(Codec_random(), url)


if __name__ == "__main__":
    test_solution(url="http://google.com.sg")
    test_solution(url="http://leetcode.com")
