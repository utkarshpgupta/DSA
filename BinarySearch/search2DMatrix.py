#74. Search a 2D Matrix

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        l, r = 0, (m*n)-1

        while(l <= r):
            mid = (l+r)//2
            m1, m2 = (mid//n), (mid%n)
            if matrix[m1][m2] == target:
                return True
            elif matrix[m1][m2] < target:
                l = mid + 1
            elif matrix[m1][m2] > target:
                r = mid - 1
            
        return False