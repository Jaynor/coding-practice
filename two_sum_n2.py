from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if target == (nums[i] + nums[j]):
                    rnums = [i, j]
                    return rnums


def main():
    #nums = [2,7,11,15]
    nums = [3, 3]
    target = 6
    test = Solution()
    print(test.twoSum(nums, target))

main()
