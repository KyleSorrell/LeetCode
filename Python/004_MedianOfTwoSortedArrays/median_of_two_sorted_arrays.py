# https://leetcode.com/problems/median-of-two-sorted-arrays/submissions/1715028496/

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(A) + len(B)
        half = total//2
        if len(B) < len(A):
            A, B = B, A # sets A as the smallest array
        left, right = 0, len(A) - 1
        while True:
            middleA = (left + right) // 2
            middleB = half - middleA - 2

            leftA = A[middleA] if middleA >= 0 else float("-infinity")
            rightA = A[middleA + 1] if (middleA + 1) < len(A) else float("infinity")
            leftB = B[middleB] if middleB >= 0 else float("-infinity")
            rightB = B[middleB + 1] if (middleB + 1) < len(B) else float("infinity")

            # correct partition
            if leftA <= rightB and leftB <= rightA:
                # odd total
                if total % 2:
                    return min(rightA, rightB)
                # even total
                return (max(leftA, leftB) + min(rightA, rightB)) / 2
            elif leftA > rightB:
                right = middleA - 1
            else:
                left = middleA + 1
