from typing import Final


def fib(n: int) -> int:
    if n == 0:
        return fib.f0
    elif n == 1:
        return fib.f1
    return fib(n - 1) + fib(n - 2)
# Using function attributes to emulate static variables:
# typing.Final not supported by pylint at this time
#  https://github.com/PyCQA/pylint/issues/3197
fib.f0: Final[int] = 0  # pylint: disable=unsubscriptable-object
fib.f1: Final[int] = 1  # pylint: disable=unsubscriptable-object


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
