class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest = min(strs, key=len)

        for i, char in enumerate(shortest):
            for word in strs:
                if word[i] != char:
                    return shortest[:i]

        return shortest