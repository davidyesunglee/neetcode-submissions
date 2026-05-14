class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmapS = defaultdict(int)
        hashmapT = defaultdict(int)

        for char in s:
            hashmapS[char] += 1
        
        for char in t:
            hashmapT[char] += 1

        return hashmapS == hashmapT