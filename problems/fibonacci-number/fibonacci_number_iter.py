from typing import List


def fib(n: int) -> int:
    if n <= 1:
        return n
    k: int = 2
    f_kmin2: int = 0
    f_kmin1: int = 1
    f_k: int
    while k <= n:
        f_k = f_kmin1 + f_kmin2
        k += 1
        f_kmin2 = f_kmin1
        f_kmin1 = f_k
    return f_k


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
