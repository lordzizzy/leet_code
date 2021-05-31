# references to this popular interview question

# https://spencermortensen.com/articles/egg-problem/
# https://datagenetics.com/blog/july22012/index.html

from termcolor import colored


class Solution:
    def min_egg_drop_req(self, eggs: int, tries: int) -> int:
        if eggs <= 0 or tries <= 0:
            return 0
        if eggs == 1:
            return tries
        else:
            return (
                1
                + self.min_egg_drop_req(eggs - 1, tries - 1)
                + self.min_egg_drop_req(eggs, tries - 1)
            )


def check_solution(eggs: int, tries: int, expected: int):
    sln = Solution()
    r = sln.min_egg_drop_req(eggs, tries)
    if r == expected:
        print(
            colored(
                f"PASSED - {eggs} eggs require minimum of {tries} tries to cover {r} floors.",
                "green",
            )
        )
    else:
        print(
            colored(
                f"FAILED - {eggs} eggs require minimum of {tries} tries to cover {r} floors, but expected: {expected} floors",
                "red",
            )
        )


if __name__ == "__main__":
    check_solution(eggs=2, tries=14, expected=105)
