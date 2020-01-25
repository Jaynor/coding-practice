from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dic = {}
        for i in range(len(nums)):
            if target - nums[i] not in num_dic:
                num_dic[nums[i]] = i
            else:
                return [target - nums[i], i]

def main():
    nums = [2,7,11,15]
    #nums = [3, 3]
    target = 13
    test = Solution()
    print(test.twoSum(nums, target))
main()
