# Bug reports for exercise3.py

Line: 13  
Problem: The function `percent(part, total)` will raise a `ZeroDivisionError` when `total` is 0, even though the docstring states that "If total is 0, the result is 0". The current code does not handle this edge case.  
Example:  
Input: `percent(5, 0)`  
Actual result: `ZeroDivisionError`  
Expected result: `0`  
Fix:  
```python
def percent(part, total):
    """part as a percentage of total. If total is 0, the result is 0"""
    if total == 0:
        return 0
    return part / total * 100
```
