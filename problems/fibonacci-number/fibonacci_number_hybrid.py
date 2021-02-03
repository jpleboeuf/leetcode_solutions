from typing import List
from typing import Final
import sys


def static_var(*vars_dec):
    def static_var_decorator(func):
        # In the local scope,
        #  the decorated function is known as `func`.
        # To be able to have static variables initialized
        #  with the value of other static variables,
        #  add a reference in the local scope
        #  to `func` using its real name.
        # For that purpose, get the current frame object,
        #  retrieve the locals, and add the reference.
        sys._getframe().f_locals[func.__name__] = func
        for var_dec_idx, var_dec in enumerate(vars_dec):
            # Warning: just a proof-of-concept‼
            #  For the code to be bulleproof,
            #  some sanity check of each variable declaration should be done!
            # --- First,
            #  declare the future (simulated) static variable
            #  so that it ends in the locals.
            # For speed, compile the source code beforehand into a code object.
            var_dec_co = compile(var_dec, '', 'exec')
            exec(var_dec_co)
            # --- Second,
            #  retrieve the name of the newly created variable.
            # @todo For now (1 static), it is the only attribute available.
            var_name = list(locals()['__annotations__'])[var_dec_idx]
            # --- Finally,
            #  add thid newly created variable
            #  as an attribute of the decorated function.
            setattr(func, var_name, locals()[var_name])
        return func
    return static_var_decorator


# Using function attributes to emulate static variables,
#  implemented through a decorator.
# Each static-like variable used by the function
#  has to be declared in a string
#  and passed as an argument of the static var decorator.
@static_var(
    'f0: Final[int] = 0',
    'f1: Final[int] = 1',
    'f: List[int] = [fib.f0, fib.f1]'
)
def fib(n: int) -> int:
    if n == 0:
        return fib.f0
    elif n == 1:
        return fib.f1
    if n >= len(fib.f):
        fib.f.append(fib(n - 1) + fib(n - 2))
    return fib.f[n]


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
