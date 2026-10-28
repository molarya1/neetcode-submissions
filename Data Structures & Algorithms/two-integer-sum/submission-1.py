class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}

        for i, number in enumerate(nums):
            difference = target - number

            if difference in d:
                return [d[difference], i]
            
            d[number] = i
