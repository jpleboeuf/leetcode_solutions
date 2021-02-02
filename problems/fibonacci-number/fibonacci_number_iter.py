from typing import List
from typing import Final


def fib(n: int) -> int:
    if n == 0:
        return fib.f0
    elif n == 1:
        return fib.f1
    k: int = 2
    f_kmin2: int = fib.f0
    f_kmin1: int = fib.f1
    f_k: int
    while k <= n:
        f_k = f_kmin1 + f_kmin2
        k += 1
        f_kmin2 = f_kmin1
        f_kmin1 = f_k
    return f_k
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
