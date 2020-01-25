from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp_dic = {}

        for i in range(len(nums)):
            if nums[i] in temp_dic:
                return [temp_dic[nums[i]], i]
            else:
                temp_dic[nums[i]] = i
                if target - nums[i] in temp_dic and target - nums[i] != nums[i]:
                    return [temp_dic[target - nums[i]], i]

def main():
    nums = [2,7,11,15]
    #nums = [3, 3]
    target = 17
    test = Solution()
    print(test.twoSum(nums, target))

main()
