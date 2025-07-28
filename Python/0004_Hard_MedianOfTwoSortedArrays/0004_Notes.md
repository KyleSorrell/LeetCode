Problem:
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).

Notes:
Since the required time complexity is O(log (m+n)), this problem is typically solved using binary search on the smaller array.

Suppose we are given:
A = [1, 2, 3, 4]
B = [1, 2, 3, 4, 5, 6, 7, 8]
Total elements = 12 → half = 6
We binary search on A (the smaller array)

Step 2: First partition
Pick m = 1.
Then n = 6 - (m+1) = 6 - 2 = 4.

Partitions:
A = [1, 2] | [3, 4]
B = [1, 2, 3, 4] | [5, 6, 7, 8]

Step 3: Check conditions
We need these two conditions to be true for a correct partition:
A[m] <= B[n]
B[n-1] <= A[m+1]

Substitute values:
A[m] = A[1] = 2
B[n] = B[4] = 5
B[n-1] = B[3] = 4
A[m+1] = A[2] = 3

Check:
A[m] <= B[n] → 2 <= 5 → True
B[n-1] <= A[m+1] → 4 <= 3 → False
Since the second condition fails, the partition in A is too far to the left.

Step 4: Move partition to the right
We shift the partition in A to the right:

New left = m + 1 = 2
Right stays = 3
New m = (2 + 3) // 2 = 2
New n = 6 - (m+1) = 6 - 3 = 3

Step 5: New partitions
A = [1, 2, 3] | [4]
B = [1, 2, 3] | [4, 5, 6, 7, 8]

Check conditions again:
A[m] = A[2] = 3
B[n] = B[3] = 4
B[n-1] = B[2] = 3
A[m+1] = A[3] = 4
A[m] <= B[n] → 3 <= 4 → True
B[n-1] <= A[m+1] → 3 <= 4 → True
Both conditions are satisfied.

Final partitions:
A = [1, 2, 3] | [4]
B = [1, 2, 3] | [4, 5, 6, 7, 8]

From these partitions, the median can be calculated from the largest elements of the left partitions and the smallest elements of the right partitions.
