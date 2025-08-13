Queues

A queue is a linear data structure that follows FIFO (First In, First Out) order: First element added → first element removed

Core Operations:
- Enqueue: Add an element to the rear of the queue. O(1)
- Dequeue: Remove an element from the front. O(1)
- Peek/Front: Look at the element at the front without removing. O(1)
- IsEmpty: Check if the queue has no elements. O(1)

Types of Queues:
1. Simple Queue
- Standard FIFO queue
- Fixed size in arrays, dynamic in linked lists
2. Circular Queue
- Rear wraps around to the front when space is available
- Efficient memory usage
- Avoids “wasted space” in fixed-size array implementation
3. Double-Ended Queue (Deque)
- Insert or remove elements from both ends
- Can function as both queue and stack
4. Priority Queue
- Elements are dequeued based on priority, not just order
- Can be implemented with heaps

Implementation Approaches:
1. Array-Based Queue
- Use an array to store elements
- Track front and rear indices
- Can be circular to optimize space
2. Linked List-Based Queue
- Each element is a node with a pointer to the next
- Front points to head, rear points to tail
- No fixed size limit

Use Cases:
- Task Scheduling (e.g., CPU process scheduling)
- Breadth-First Search (BFS) in graphs or trees
- Printing Jobs in a printer queue
- Handling Requests in servers or messaging systems

Pros:
- Simple to understand and implement
- Efficient for FIFO operations
- Flexible with dynamic size (linked list)

Cons:
- Fixed-size array queues may waste space
- Circular arrays require careful index handling

