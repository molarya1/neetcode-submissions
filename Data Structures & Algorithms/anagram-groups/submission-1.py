class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}

        for word in strs:
            freq = [0] * 26

            for i in range(len(word)):
                freq[ord(word[i]) - ord('a')] += 1

            key = tuple(freq)
            d.setdefault(key, []).append(word)


        return list(d.values())