Two Pointer Technique

The two pointer technique is a common approach where you use two variables (pointers or indices) to traverse a data structure, usually an array or string, from different positions. 
Instead of looping through everything with nested loops, two pointers can often reduce time complexity from O(n²) to O(n).

When to Use Two Pointers:
1. The data is sorted or can be treated in a sorted way
   Sorting allows you to move the pointers intelligently (e.g., left increases, right decreases) instead of checking all pairs.
2. You need to find a pair or group of elements that meet a condition
   Examples:
   - Find two numbers that add up to a target sum.
   - Find the closest pair to a target.
   - Remove duplicates from a sorted array.
3. You need to scan from both ends or move through a range
   Pointers can start:
   - Both at the beginning (fast/slow pointers)
   - One at the start and one at the end (shrinking window)
   - One leading and one trailing (sliding window)
4. You want to avoid extra memory
   This method usually works in-place, no need for additional data structures.

Types of Two-Pointer Patterns:
1. Opposite Ends (Converging)
   Start with one pointer at the beginning and one at the end.
   Move them towards each other depending on conditions.
   Example:
   - Given a sorted array, find two numbers whose sum equals a target.

2. Same Direction (Fast/Slow or Sliding Window)
   Both pointers move forward, but at different speeds or one adjusts to maintain a window.
   Example:
   - Detect a cycle in a linked list (Floyd’s algorithm) or find the longest substring without repeating characters.

Why It Works:
Instead of brute forcing every combination, two pointers exploit structure (like sorting or the contiguous nature of a string) to skip unnecessary work.

When Not to Use It:
If the data isn’t sorted and can’t be made sorted without breaking the problem.
If the relationship between elements isn’t order-based (e.g., arbitrary graphs).

Example: Pair sum in a sorted array
Problem: Given a sorted array, find if there are two numbers that add up to a target.

def has_pair_with_sum(arr, target):
    left = 0
    right = len(arr) - 1

    while left < right:
        s = arr[left] + arr[right]
        if s == target:
            return True
        elif s < target:
            left += 1  # need a bigger sum
        else:
            right -= 1  # need a smaller sum
    return False
This runs in O(n) instead of O(n²).

Key advantages:
- Efficiency: Often reduces time complexity from quadratic to linear.
- Simplicity: Straightforward to implement once you see the pattern.
