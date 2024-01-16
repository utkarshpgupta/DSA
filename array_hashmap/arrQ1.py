class Solution(object):

# solution 1 o(n^2) 35ms

    # def containsDuplicate(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: bool
    #     """
    #     n = len(nums)
    #     for i in range(n-1):
    #         for j in range(i+1,n):
    #             if(nums[i] == nums[j]):
    #                 return True
    #     return False

# solution 2 o(n)  
    def containsDuplicate(self, nums):
        n = len(nums)
        d = {}
        for i in range(n):
            if nums[i] not in d:
                d[nums[i]] = 1
            else:
                d[nums[i]] += 1
                # return True 
                #(will exit out of the loop and won't  count other encounters)
        
        for j in d.values():
            if j > 1:
                return True
            else:
                return False