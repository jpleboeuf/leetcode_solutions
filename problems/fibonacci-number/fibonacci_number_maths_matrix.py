from typing import Final


def fib(n: int) -> int:
    """Return the Fibonacci number for n.
    This version uses Binet's formula,
     whose value for n is computed by rounding.
    Binet's formula:
     Fₙ = ( ɸⁿ - ψⁿ ) / √5
      where:
       ɸ = ( 1 + √5 ) / 2  (golden ratio)
       ψ = ( 1 - √5 ) / 2
    Since | ψⁿ / √5 | < ½ for all n ≥ 0,
     Fₙ is the closest integer to ɸⁿ / √5.
    Therefore Fₙ = [ ɸⁿ / √5 ].
    """
    # typing.Final not supported by pylint at this time
    #  https://github.com/PyCQA/pylint/issues/3197
    phi: Final[float] = ( 1 + 5 ** 0.5 ) / 2  # pylint: disable=unsubscriptable-object
    return int( round( phi ** n / 5 ** 0.5 ) )


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
