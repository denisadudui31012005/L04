# Bug reports for exercise2.py

Line: 13  
Problem: The line `return max(low, min(x, low))` is logically incorrect. It computes `min(x, low)`, which gives the smaller of `x` and `low`, and then takes `max(low, ...)` of that result. Since `min(x, low)` is already ≤ `low`, taking `max(low, min(x, low))` will always return `low`. This means the function will always return `low`, regardless of `x`.  

For example, if `x = 10`, `low = 5`, `high = 15`, then:
- `min(x, low)` → `min(10, 5)` → `5`
- `max(low, 5)` → `max(5, 5)` → `5`  
But it should return `min(x, high)` and `max(x, low)` — the correct clamping is to return `max(low, min(x, high))`.

Example:  
Input: x=3, low=1, high=10  
Actual result: `max(1, min(3, 1))` → `max(1, 1)` → `1` ✅ (correct)  
But if x=15, low=1, high=10:  
Actual result: `max(1, min(15, 1))` → `max(1, 1)` → `1` ❌ (should be 10)  

Expected result: should return `max(low, min(x, high))`  

Fix: `return max(low, min(x, high))`
