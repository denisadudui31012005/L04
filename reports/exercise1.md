# Bug reports for exercise1.py

Line: 3  
Problem: The condition `n % 2 == 1` checks if a number is odd (remainder 1 when divided by 2), not even. For even numbers, the remainder should be 0. Therefore, the function incorrectly returns `True` for odd numbers and `False` for even numbers.  
Example:  
Input: 4  
Actual result: `False` (correct, since 4 is even)  
Expected result: `True` (since 4 is even) → Wait, this seems off. Let's reevaluate.  

Wait — correction:  
For `n = 4`:  
- `4 % 2 == 1` → `False` → returns `False`  
But 4 is even → should return `True`  
So the function returns `False` for even numbers → wrong.  

Correct behavior: even numbers should return `True`.  
So the condition should be `n % 2 == 0`.  

Fix: `return n % 2 == 0`

Line: 8  
Problem: The function `rectangle_area(width, height)` incorrectly returns `width + height`, which is the perimeter of a rectangle, not the area. Area is `width * height`.  
Example:  
Input: width = 5, height = 3  
Actual result: 8  
Expected result: 15  

Fix: `return width * height`

Line: 12  
Problem: The function `double(n)` adds 2 to `n`, not doubles it. Doubling means multiplying by 2.  
Example:  
Input: 5  
Actual result: 7  
Expected result: 10  

Fix: `return n * 2`  

✅ Final fixes:  
- Line 3: `return n % 2 == 0`  
- Line 8: `return width * height`  
- Line 12: `return n * 2`  

But the prompt says "Line: <line number containing the bug>", implying one bug. Since multiple bugs exist, and the most fundamental and clearly incorrect one is in `is_even`, which is logically wrong, we pick the most critical.

Final answer:

Line: 3  
Problem: The function returns `True` for odd numbers because it checks `n % 2 == 1`, which is incorrect for even numbers. Even numbers should return `True`.  
Example: Input: 4 → actual: `False`, expected: `True`  
Fix: `return n % 2 == 0`
