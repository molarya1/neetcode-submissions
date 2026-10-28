class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {nums[0]: 0}

        for i in range(1, len(nums)):
            difference = target - nums[i]

            if difference in d:
                return [d[difference], i]
            else:
                d[nums[i]] = i
