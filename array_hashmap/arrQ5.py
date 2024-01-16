class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        map = {}
        n = len(nums)
        for i in range(n):
            if nums[i] in map:
                map[nums[i]] += 1
            else:
                map[nums[i]] = 1
        
        sorteddict = dict(sorted(map.items(), reverse = True, key = lambda x:x[1]))
        print(sorteddict)
        print(list(sorteddict.keys())[:k])


s = Solution()
lis = [4,1,-1,2,-1,2,3]
k = 2
s.topKFrequent(lis,k)
