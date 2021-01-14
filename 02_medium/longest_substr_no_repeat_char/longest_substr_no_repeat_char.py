class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        count = 0
        dic = {}

        i = 0
        for j in range(n):
            if s[j] in dic:
                i = max(dic[s[j]], i)

            count = max(count, j - i + 1)
            dic[s[j]] = j + 1

        return count


if __name__ == "__main__":
    s = Solution()
    n = s.lengthOfLongestSubstring("abcabcbb")
    print(f"abcabcbb's longest substring is {n}")
