class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        occur = {}

        for n in nums:
            occur[n] = occur.get(n, 0) + 1

            if occur[n] > 1:
                return True

        return False