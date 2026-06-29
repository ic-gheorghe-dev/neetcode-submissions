class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        memory = {}

        for i in range(len(nums)):
            current_number = nums[i]
            needed_number = target - current_number
            if needed_number in memory:
                return [memory[needed_number], i]
            memory[current_number] = i