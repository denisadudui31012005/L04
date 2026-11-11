# Bug reports for exercise4.py

Line: 9  
Problem: The condition `ADMIN_PASSWORD != ""` is always true because `ADMIN_PASSWORD` is defined as `"admin123"`, which is a non-empty string. This check is redundant and logically incorrect — it does not validate whether the password is correct. Instead, it only checks if the password is non-empty, which is not sufficient for admin authentication. The correct logic should simply compare the input password to `ADMIN_PASSWORD`. Additionally, this condition could lead to a false sense of security or misbehavior if the password were ever set to an empty string (which it isn't here), but the logic is flawed in intent and structure.

Example:  
Input: `password = "admin123"`  
Actual result: `check_admin("admin123")` returns `True` (correct), but the condition `ADMIN_PASSWORD != ""` is irrelevant and doesn't contribute to correctness.  
Expected result: The function should return `True` only if the password matches `ADMIN_PASSWORD`, not based on whether the admin password is non-empty.

Fix:  
Replace line 9 with:  
```python
return password == ADMIN_PASSWORD
```
