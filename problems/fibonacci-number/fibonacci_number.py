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


N = 2
solution = Solution()
print(solution.fib(N))

N = 3
solution = Solution()
print(solution.fib(N))

N = 4
solution = Solution()
print(solution.fib(N))
