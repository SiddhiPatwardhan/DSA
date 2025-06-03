class solution:
    def containerWithMostWater(self , heights):
        max_area = 0
        left = 0
        right = len(heights) - 1

        while left < right:
            max_area = max(max_area, (right-left) * min(heights[left],heights[right]))

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return max_area
    
sol = solution()
result = sol.containerWithMostWater([1,8,6,2,5,4,8,3,7])
print(result)