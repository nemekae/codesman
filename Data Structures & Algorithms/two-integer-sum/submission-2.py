class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashset = {}

        for i,num in enumerate(nums):
            addon = target - num

            if addon in hashset:
                return [hashset[addon], i]
            
            hashset[num] = i

