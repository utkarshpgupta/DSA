# 11. Container With Most Water  https://www.youtube.com/watch?v=UuiTKBwPgAo

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l, r = 0, len(height)-1
        output = 0
        while l<r:
            area = (r-l)*min(height[l],height[r])
            output = max(area, output)
            
            if height[l]<height[r]:
                l += 1
            elif height[l]>height[r]:
                r -= 1
            else:
                r -= 1
                

                
        return output