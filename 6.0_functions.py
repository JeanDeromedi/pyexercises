"""Exercise 6.0 — Naming a piece of work

WHAT THE PROGRAM MUST DO
    Write a function that computes something useful about the list you built in exercise
    4.0, then call it three times with different inputs and display the three results.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?  (what your function receives)
    2. What happens to it?
    3. What comes out?  (what your function returns)
    4. What is your function called, and does its name say what it does without reading
       the code?

WHAT THE AI CANNOT KNOW
    What is worth computing about your data, and what to call it. A function named
    "process" or "do_stuff" fails this exercise even if it works.

    Your function must RETURN its result, not print it. Find out why that difference
    matters and write the reason in a comment. It is the whole point of the exercise.

CHECK IT YOURSELF
    Call your function with an empty list. Note what happens. Then decide whether that
    behaviour is acceptable, and say so in a comment.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In:A list of monthly investment amounts in euros.
# 2. Process: A function calculates the total amount invested by adding all values in the list.
# 3. Out: The function returns the total investment amount.
# 4. My function name, and why return rather than print: The function is called calculate_total_invested, which clearly describes its purpose. Using return allows the result to be reused in other calculations, while print() only displays it.


# Your code below

investments = [500, 650, 400, 750, 600, 900, 550, 800]

def calculate_total_invested(amounts):
    return sum(amounts)

print("Total investment:", calculate_total_invested(investments))

print("First three months:", calculate_total_invested(investments[:3]))

print("Empty list:", calculate_total_invested([]))


# TEST RESULTS
# The complete list returns 5150, as expected.
# The first three months return 1550, as expected.
# An empty list returns 0.
# This is acceptable because an empty list means no investments.
