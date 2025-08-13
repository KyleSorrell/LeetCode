Problem:
Given an integer array nums and an integer target, return all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

- 0 <= a, b, c, d < len(nums)
- all four indices are distinct
- nums[a] + nums[b] + nums[c] + nums[d] == target
- You may return the answer in any order.

Time Complexity Requirement:
No explicit complexity given, but:

- Brute force (four nested loops) = O(n⁴) → too slow for large input.
- We can reduce to O(n³) by fixing two pointers and then using a two-pointer scan for the remaining two, just like 3-sum but with one extra loop.

Key Idea:
This is an extension of 3-sum:

- In 3-sum: Fix i → scan with left/right for pairs.
- In 4-sum: Fix two numbers (i and j) → scan with left/right for the remaining pair.
  We sort nums first to enable:
- Two-pointer approach for the last two numbers
- Easy duplicate skipping for unique quadruplets

Pointer Roles:

- i → outermost loop: first number
- j → second loop: second number
- left → starts at j+1, moves rightward
- right → starts at end of array, moves leftward
  Once i and j are fixed, we run the standard 2-pointer check on left/right.

Duplicate Skipping:

- Skip duplicate values for i and j before entering their respective loops.
- Skip duplicate values for left and right after finding a valid quadruplet.

Transition Logic:
For each (i, j) pair:

1. Calculate total = nums[i] + nums[j] + nums[left] + nums[right].
2. If total == target → record quadruplet, move both left and right past duplicates.
3. If total < target → move left rightward.
4. If total > target → move right leftward.
