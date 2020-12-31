from typing import List


def fib(n: int) -> int:
    f0: int = 0
    f1: int = 1
    f: List[int] = [f0, f1]
    i = 2
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
