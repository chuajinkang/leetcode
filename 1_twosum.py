"""Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order."""

class Solution:
    def twoSum(self, nums: [int], target: int) -> [int]:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    value = nums[i] + nums[j]
                    if value == target:
                        return [i, j]
        else:
            print('no sum')