from typing import Final


def matrix22_pow(M: list, n: int) -> list:
    """
    Return a new 2×2 matrix,
     result of the exponentiation of the 2×2 matrix M by n. 
    """
    if n <= 1:
        return M
    Msq = matrix22_mul(M, M)
    if n % 2 == 0:  # n is even
        return matrix22_pow(Msq, n // 2)
    else:           # n is odd
        return matrix22_mul(M, matrix22_pow(Msq, (n - 1) // 2))

def matrix22_mul(M1: list, M2: list) -> list:
    """
    Return a new 2×2 matrix,
     result of the multiplication of the two 2×2 matrices M1 and M2.
    """
    mm_00 = M1[0][0] * M2[0][0] + M1[0][1] * M2[1][0]
    mm_01 = M1[0][0] * M2[0][1] + M1[0][1] * M2[1][1]
    mm_10 = M1[1][0] * M2[0][0] + M1[1][1] * M2[1][0]
    mm_11 = M1[1][0] * M2[0][1] + M1[1][1] * M2[1][1]
    return [
            [ mm_00, mm_01 ],
            [ mm_10, mm_11 ],
        ]


def fib(n: int) -> int:
    # pylint: disable=anomalous-backslash-in-string
    """Return the Fibonacci number for n.
    This version uses the matrix form of the Fibonacci sequence.
    We have the following recurrence relation
     that describes the Fibonacci sequence:
     / Fₖ₊₂ \ = / 1 1 \ / Fₖ₊₁ \ ,
     \ Fₖ₊₁ /   \ 1 0 / \ Fₖ   /
     alternatively denoted F⃗ₖ₊₁ = A F⃗ₖ.
    Then:
     / Fₙ₊₁ \ = / 1 1 \ⁿ / F₁ \ ,
     \ Fₙ   /   \ 1 0 /  \ F₀ /
     also denoted F⃗ₙ = Aⁿ F⃗₀.
    """
    # pylint: enable=anomalous-backslash-in-string
    F0 = [
            [1],
            [0],
        ]
    A = [
            [1, 1],
            [1, 0],
        ]
    if n <= 1:
        return F0[n][-1]
    Aexpnmin1 = matrix22_pow(A, n - 1)
    """
    Fn = Aexpnmin1[0][0] * F0[0][0] + Aexpnmin1[0][-1] * F0[1][-1]
    Since F0[0][0] = 1 and F0[1][-1] = 0,
     we have Fn = Aexpnmin1[0][0].
    """
    return Aexpnmin1[0][0]


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
