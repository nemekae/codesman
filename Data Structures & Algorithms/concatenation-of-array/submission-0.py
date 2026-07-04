class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        joined = [*nums, *nums[:]]
        return joined