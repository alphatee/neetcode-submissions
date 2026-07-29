class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [0] * 2 * len(nums)
        
        for index, value in enumerate(2*nums):
            ans[index] = value

        return ans