class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        walk_the_array = 0

        for index in range(len(nums)):
            if nums[index] != val:
                nums[walk_the_array] = nums[index]
                walk_the_array += 1

        return walk_the_array