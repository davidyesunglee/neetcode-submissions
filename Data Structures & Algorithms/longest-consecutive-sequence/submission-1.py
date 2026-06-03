class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        streak = 0

        for num in numSet:
            if num - 1 in numSet:
                continue
            current = num
            while current in numSet:
                streak += 1
                current = current + 1
            longest = max(longest, streak)
            streak = 0

        return longest