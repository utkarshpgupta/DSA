#128. Longest Consecutive Sequence


class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        longest = 0
        n = len(nums)
        numSet = set(nums)
        for i in range(n):
            if nums[i]-1 not in numSet:
                length = 0
                while(nums[i]+length in numSet):
                    length += 1
                longest = max(length,longest)

        return longest
        
