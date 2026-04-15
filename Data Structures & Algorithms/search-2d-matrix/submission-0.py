class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0
        bottom = len(matrix) - 1

        while top <= bottom: 
            target_row = (top + bottom) // 2

            if target < matrix[target_row][0]:
                bottom = target_row - 1
            elif target > matrix[target_row][-1]: 
                top = target_row + 1
            else:
                break
        else: 
            return False
        
        # identified target row to search
        row = matrix[target_row]
        left = 0
        right = len(row) - 1


        while left <= right:
            mid = (left + right) // 2
            if row[mid] == target:
                return True
            elif row[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return False
        