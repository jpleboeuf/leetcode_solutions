from typing import Final


def matrix22_pow(mat_m: list, n: int) -> list:
    """
    Return a new 2×2 matrix,
     result of the exponentiation of the 2×2 matrix mat_m by n. 
    """
    if n <= 1:
        return mat_m
    mat_m_sq = matrix22_mul(mat_m, mat_m)
    if n % 2 == 0:  # n is even
        return matrix22_pow(mat_m_sq, n // 2)
    else:           # n is odd
        return matrix22_mul(mat_m, matrix22_pow(mat_m_sq, (n - 1) // 2))

def matrix22_mul(mat_m1: list, mat_m2: list) -> list:
    """
    Return a new 2×2 matrix,
     result of the multiplication of the two 2×2 matrices mat_m1 and mat_m2.
    """
    mm_00 = mat_m1[0][0] * mat_m2[0][0] + mat_m1[0][1] * mat_m2[1][0]
    mm_01 = mat_m1[0][0] * mat_m2[0][1] + mat_m1[0][1] * mat_m2[1][1]
    mm_10 = mat_m1[1][0] * mat_m2[0][0] + mat_m1[1][1] * mat_m2[1][0]
    mm_11 = mat_m1[1][0] * mat_m2[0][1] + mat_m1[1][1] * mat_m2[1][1]
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
    vec_f0 = [
            [1],
            [0],
        ]
    mat_a = [
            [1, 1],
            [1, 0],
        ]
    if n <= 1:
        return vec_f0[1 - n][-1]
    mat_a_exp_nmin1 = matrix22_pow(mat_a, n - 1)
    """
    vec_fn = mat_a_exp_nmin1[0][0] * vec_f0[0][0] + mat_a_exp_nmin1[0][-1] * vec_f0[1][-1]
    Since vec_f0[0][0] = 1 and vec_f0[1][-1] = 0,
     we have vec_fn = mat_a_exp_nmin1[0][0].
    """
    return mat_a_exp_nmin1[0][0]


class Solution:
    def fib(self, n: int) -> int:
        return fib(n)


def main():

    solution = Solution()

    for n in [
                 0,
                 1,
                 2,  # Example 1
                 3,  # Example 2
                 4,  # Example 3
                30,
            ]:
        print(f"n={n} ⇒ solution={solution.fib(n)}")

if __name__ == '__main__':
    main()
