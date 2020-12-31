from typing import List


class Solution:
    def fib(self, N: int) -> int:
        F0: int = 0
        F1: int = 1
        f: List[int] = [F0, F1]
        i = 2
        while i <= N:
            f.append(f[i - 1] + f[i - 2])
            i += 1
        return f[N]


N = 2
solution = Solution()
print(solution.fib(N))

N = 3
solution = Solution()
print(solution.fib(N))

N = 4
solution = Solution()
print(solution.fib(N))
