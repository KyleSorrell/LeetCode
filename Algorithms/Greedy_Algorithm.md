Greedy Algorithm

The greedy algorithm is an algorithm where, at each step, you make the locally optimal choice—picking the best option available right now—without worrying about the bigger picture. 
You continue this process until you reach a complete solution. It’s called “greedy” because it always grabs the largest or most favorable option first. 
Greedy algorithms work best when the problem structure guarantees that the best local step leads to the best global result—like choosing the largest Roman numeral that fits at each stage until nothing’s left.

When to Use Greedy Algorithms:
1. The problem can be broken into subproblems that can each be solved optimally in isolation.
2. Choosing the locally best option leads to a globally optimal solution (this is not always guaranteed).
3. You don’t need to backtrack or revise earlier choices.

Common Characteristics:
1. Greedy Choice Property: Making a local optimum leads to a global optimum.
2. No Reconsideration: Once a choice is made, it’s never changed.

Often Used In:
- Coin change problems (when denominations allow)
- Scheduling (e.g., earliest finish time first)
- Huffman encoding
- Activity selection
- Roman numeral conversion

When Not to Use It:
If the locally optimal choices don’t lead to a globally correct solution (e.g., greedy won’t solve the coin change problem optimally with denominations like [1, 3, 4] and target = 6).
Problems requiring backtracking, dynamic programming, or exploring multiple combinations.

Example: Roman Numeral Conversion
Problem: Convert an integer to Roman numerals.

def intToRoman(num):
    val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    syms = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    result = ""
    for i in range(len(val)):
        while num >= val[i]:
            result += syms[i]
            num -= val[i]
    return result
This loop always picks the largest value that fits, subtracts it, and appends the corresponding symbol—classic greedy behavior.

Key Advantages:
- Efficiency: Simple and fast—usually O(n) or better.
- Simplicity: Easy to write and understand.
- No overhead: No recursion, no extra data structures unless needed.
