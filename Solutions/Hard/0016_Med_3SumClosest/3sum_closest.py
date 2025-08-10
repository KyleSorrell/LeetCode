# https://leetcode.com/problems/3sum-closest/description/

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = nums[0] + nums[1] + nums[2]
        closest_diff = abs(res - target)

        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]
                diff = abs(total - target)

                if diff < closest_diff:
                    closest_diff = diff
                    res = total

                if total < target:
                    left += 1
                elif total > target:
                    right -= 1
                else:
                    return total

        return res