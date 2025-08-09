Problem:
Given an array of k sorted linked lists, merge them into one sorted linked list and return its head.

Example:
Input: [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]

Key Points:

- Each input list is sorted in ascending order.
- Goal is to merge all lists into a single sorted linked list.
- Result list must preserve sorted order.
- Efficiently handle multiple lists simultaneously.
- If all lists are empty, return None or empty list.

Approach:
Use a dummy node and a current pointer to build the merged list easily, and repeatedly pick the smallest node from the heads of all lists.

Data Structures:

- A dummy node to simplify head management (avoids special cases for first node).
- A current pointer to track where to append the next smallest node.
- A min-heap (priority queue) to efficiently select the smallest node among all current heads.

Step-by-step idea:

1. Initialize a dummy node and set current pointer to dummy.
2. Insert the head node of each list into a min-heap keyed by node value.
3. While heap is not empty:
   - Extract the smallest node from the heap.
   - Append it to current.next.
   - Move current forward.
   - If extracted node has a next node, push that next node into the heap.
4. Return dummy.next as the head of the merged list.

Time Complexity:

- Let k = number of lists, n = total number of nodes across all lists.
- Each node is pushed and popped from the heap once.
- Heap operations cost O(log k).
- Overall complexity: O(n log k).

Space Complexity:

- Heap stores up to k nodes at a time → O(k).
- Result linked list uses existing nodes, no extra storage besides pointers.
