from typing import List
from typing import Final


def fib(n: int) -> int:
    # typing.Final not supported by pylint at this time
    #  https://github.com/PyCQA/pylint/issues/3197
    f0: Final[int] = 0  # pylint: disable=unsubscriptable-object
    f1: Final[int] = 1  # pylint: disable=unsubscriptable-object
    f: List[int] = [f0, f1]
    i: int = 2
    while i <= n:
        f.append(f[i - 1] + f[i - 2])
        i += 1
    return f[n]


class Solution:
    def fib(self, n: int) -> int:
        return fib(n)


def main():

    solution = Solution()

    for n in [
                 2,  # Example 1
                 3,  # Example 2
                 4,  # Example 3
                30,
            ]:
        print(f"n={n} ⇒ solution={solution.fib(n)}")

if __name__ == '__main__':
    main()
