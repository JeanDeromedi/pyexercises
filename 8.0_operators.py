"""Exercise 8.0 — Operators (bonus, not graded)

WHAT THE PROGRAM MUST DO
    Take two values of your choice and display, as a readable table, the result of every
    comparison between them and of the logical combinations of those results.

ANSWER THESE FIRST, in comments
    1. What goes in? Two strings: "Ada" and "ada".
    2. What happens to it? Compare the two strings using ==, !=, <, <=, > and >=. Combine comparison results using and, or and not.
    3. What comes out? A readable table showing each operation and its result (True or False).
    4. Which two values did you pick, and which comparison result surprised you? I chose "Ada" and "ada". The surprising result is that "Ada" < "ada" is True, even though they contain the same letters apart from capitalization.

WHAT THE AI CANNOT KNOW
    Your two values. Pick a pair where the answer is not obvious: two strings with
    different capitalisation, a number and the same number written as text, or zero and
    an empty string.

CHECK IT YOURSELF
    Predict each result before running. Count how many you got right.

DELIVERABLE
    This file, with your comments and your code.
"""

# Your code below

a = "Ada"
b = "ada"

# Comparison operators
equal = a == b
different = a != b
less = a < b
less_equal = a <= b
greater = a > b
greater_equal = a >= b

print("COMPARISON OPERATORS")
print("Operation       | Result")
print("-------------------------")
print("a == b          |", equal)
print("a != b          |", different)
print("a < b           |", less)
print("a <= b          |", less_equal)
print("a > b           |", greater)
print("a >= b          |", greater_equal)

# Logical operators
print()
print("LOGICAL OPERATORS")
print("Operation       | Result")
print("-------------------------")
print("equal and less  |", equal and less)
print("equal or less   |", equal or less)
print("not equal       |", not equal)
print("different and less |", different and less)
print("greater or equal |", greater or equal)



# TEST RESULTS
# The program displays six comparisons and five logical combinations.
# The results are displayed as True or False.
# Uppercase and lowercase letters produce different comparison results.
# My correct predictions: ___ / 11.
