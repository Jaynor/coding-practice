# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# Example:
#
# Given nums = [2, 7, 11, 15], target = 9,
#
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i in range(len(nums)):
            if target - nums[i] not in dict:
                dict[nums[i]] = i
            else:
                return [dict[target - nums[i]], i]


def main():
    l1 = ["eat", "sleep", "repeat"]
    l2 = [1 ,2 ,3 ,4]
    # s1 = "geek"
    # obj1 = enumerate(l1)
    # obj2 = enumerate(s1)
    # for i, list in enumerate(l1, 12):
    #     print(i, list)
    # print(obj1)
    # print(obj2)
    # items = [1, 2, 3, 4, 5]
    # squared = list(map(lambda x: x ** 2, items))
    something = list(map(lambda x: '1' + x, l1))
    print(something)
#     nums = [0, 4, 3, 0]
#     #nums = [2, 7, 11, 15]
#     target = 0
#     test = Solution()
#     print(test.twoSum(nums, target))

main()

#
# j = 0
# for i in nums:
#     if i <= target:
#         if i in temp_dic:
#             if i + i == target:
#                 # print(j)
#                 # print(i)
#                 return [nums.index(i), j]
#     #print(j)
#     temp_dic[i] = j
#     j += 1
# # print(temp_dic)
# for key, value in temp_dic.items():
#     temp_value = target - key
#     #print(temp_value)
#     if temp_value == key:
#         continue
#     if temp_value in temp_dic:
#         result.append(value)
#         result.append(temp_dic[temp_value])
#         break
#
# return result
