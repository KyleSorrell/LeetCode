Problem:
Given a linked list, reverse the nodes of the list k at a time and return its head.

- k is a positive integer.
- If the number of nodes is not a multiple of k, leave the remaining nodes as is.
- Do not modify node values — only change pointers.

Time Complexity Requirement:

- Each node is visited exactly once → O(n) time.
- Reversing nodes in-place → O(1) extra space.

Key Idea:

- Use a dummy node to simplify head swaps and edge cases.
- Iterate through the list in groups of k nodes.
- For each group:
  - Identify the k-th node (kth) using a helper function.
  - Reverse the k nodes by changing next pointers.
  - Connect the reversed group to the previous and next parts of the list.
- Move to the next group and repeat until fewer than k nodes remain.

Pointer Roles:

- dummy → points to the head; simplifies swaps at the front.
- groupPrev → node before the current k-group.
- curr → node currently being reversed.
- prev → tracks the reversed portion within the k-group.
- groupNext → node after the current k-group (used to stop reversal and reconnect).

Transition Logic (Iterative / Pointer Manipulation):

1. Find kth node after groupPrev. If less than k nodes remain → stop.
2. Set groupNext = kth.next.
3. Reverse nodes from groupPrev.next up to groupNext:

- For each node curr in the group:
  - temp = curr.next
  - curr.next = prev
  - prev = curr
  - curr = temp

4. Reconnect the reversed group:
   - temp = groupPrev.next
   - groupPrev.next = kth
   - groupPrev = temp
5. Repeat for the next group.
