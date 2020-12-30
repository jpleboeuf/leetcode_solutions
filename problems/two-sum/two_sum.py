from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        twoSum_rv: int = []
        i = 0
        for ni in nums:
            j = 0
            for nj in nums:
                if i == j:
                    continue
                if ni + nj == target:
                    twoSum_rv = [i, j]
                    break
                j += 1
            else:
                i += 1
                continue
            break
        return twoSum_rv


nums = [2, 7, 11, 15]
target = 9
print(nums, target)
solution = Solution()
print(solution.twoSum(nums, target))

nums = [2, 7, 11, 15]
target = 1
print(nums, target)
solution = Solution()
print(solution.twoSum(nums, target))

nums = [3,2,4]
target = 6
print(nums, target)
solution = Solution()
print(solution.twoSum(nums, target))
