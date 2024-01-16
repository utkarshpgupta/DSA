# 238. Product of Array Except Self


class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """   
        n = len(nums)
        op = [1]*n
        
        prefix = 1
        for i in range(n):
            op[i] = prefix
            prefix *= nums[i]
        
        postfix = 1
        for i in range(n-1,-1,-1):
            op[i] *= postfix
            postfix *= nums[i]

        return op
        