from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    r: int = []
    i = 0
    for ni in nums:
        j = 0
        for nj in nums:  # for-else loop!
            if i == j:
                pass
            elif ni + nj == target:
                r = [i, j]
                break  # break from inner loop, jump to break from outer loop
            j += 1
        else:          # when the current step of the inner loop is over,
            i += 1     #  do some stuff,
            continue   #  and continue with the next step of the outer loop.
        break          # break from outer loop
    return r


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        return two_sum(nums, target)


def main():

    solution = Solution()

    for nums, target in [
                ([2, 7, 11, 15], 9),  # Example 1
                ([2, 7, 11, 15], 1),
                ([3, 2, 4], 6),       # Example 2
                ([3, 3], 6),          # Example 3
            ]:
        print(f"nums={nums}, target={target} ⇒ solution={solution.twoSum(nums, target)}")

if __name__ == '__main__':
    main()
