# https://leetcode.com/problems/container-with-most-water/description/

class Solution:
    def maxArea(self, height: List[int]) -> int:
            left = 0
            right = len(height) - 1
            maxWater = 0
            s = 0
            while left < right:
                if min(height[left], height[right]) * (right - left) > maxWater:
                    maxWater = current_water = min(height[left], height[right]) * (right - left)
                if height[left] < height[right]:
                    left += 1
                else:
                    right -= 1
            return maxWater