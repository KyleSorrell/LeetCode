Stacks

A stack is a linear data structure that follows LIFO (Last In, First Out) order: the last element added is the first one removed.

Core Operations:
- Push: Add an element to the top of the stack. O(1)
- Pop: Remove the element from the top. O(1)
- Peek/Top: Look at the element at the top without removing it. O(1)
- IsEmpty: Check if the stack has no elements. O(1)

Types of Stacks:
1. Simple Stack
- Standard LIFO stack
- Fixed size with arrays, dynamic with linked lists
2. Dynamic Stack
- Automatically grows when implemented with dynamic arrays or linked lists
- Avoids overflow issues of fixed-size arrays
3. Specialized Stacks
- Min/Max Stack: Supports retrieving the minimum/maximum in O(1)
- Undo Stack: Used in applications like text editors

Implementation Approaches:
1. Array-Based Stack
- Use an array to store elements
- Track the top index
- May need to resize dynamically if full
2. Linked List-Based Stack
- Each element is a node pointing to the next
- Top points to head of the list
- No fixed size limit

Use Cases:
- Function call management (call stack)
- Expression evaluation (infix → postfix conversion)
- Undo/Redo operations in editors
- Depth-First Search (DFS) in graphs or trees
- Browser back/forward navigation history

Pros:
- Simple and intuitive to use
- Efficient for LIFO operations
- Dynamic size possible with linked lists

Cons:
- Fixed-size arrays can overflow
- Random access is not possible; must pop elements sequentially
