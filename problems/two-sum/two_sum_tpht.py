from typing import List
from typing import Dict


def two_sum(nums: List[int], target: int) -> List[int]:
    r: int = []
    nums_pos: Dict[int, int] = {}
    for i, ni in enumerate(nums):
        nums_pos[ni] = i
    for i, ni in enumerate(nums):
        if (nj := target - ni) in nums_pos.keys()\
         and (j := nums_pos[nj]) != i:
            r = [i, j]
            break
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
