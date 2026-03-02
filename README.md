Inventory Management – Duplicate Zeros:

Problem Overview
In this inventory system, a value of 0 represents an out-of-stock product.
For every occurrence of 0, we must duplicate it (to represent a restock order) and shift the remaining elements to the right.

Constraints:
The array must be modified in place
The array size cannot increase
Elements that overflow past the original length are discarded

Diagram:
<img width="928" height="615" alt="Screenshot 2026-03-02 at 3 10 02 PM" src="https://github.com/user-attachments/assets/ea05a820-f2b9-448f-a829-9b215350e0d7" />

Test Coverage
Normal Cases
Multiple zeros in array
No zeros
Single zero in middle
Edge Cases
All zeros
Empty array
Zero at the end

