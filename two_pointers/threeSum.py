# 15. 3Sum https://www.youtube.com/watch?v=jzZsG8n2R9A

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        op = []
        l,r = 0, len(nums)-1
        for i in range(len(nums)):
            l,r = i+1, len(nums)-1
            if i>0 and nums[i] == nums[i-1]:
                continue
            while l<r:
                sum = nums[i]+nums[l]+nums[r]
            
                if sum > 0:
                    r -= 1
                elif sum < 0:
                    l += 1
                else:
                    op.append([nums[i],nums[l],nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l<r:
                        l += 1
        return op