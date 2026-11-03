"""Exercise 6.1 — Small functions working together

WHAT THE PROGRAM MUST DO
    Write three small functions, each doing one thing, and a fourth that uses the other
    three to answer one question about your data.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?  (say which function does what, in order)
    3. What comes out?
    4. What question does your fourth function answer, and why does splitting it into
       three make it easier to check?

WHAT THE AI CANNOT KNOW
    Your question and your split. Ask an assistant for "three functions" and it will
    invent three; they will not be the three your question needs. Decide the split first,
    on paper, then ask.

    One function, one job. If you cannot describe what one of yours does in a single
    sentence without using the word "and", it is doing two things.

CHECK IT YOURSELF
    Test each of the three small functions on its own before combining them. Write in a
    comment the input and expected output you used for each. That is three test cases,
    and they are part of the deliverable.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: A list of eight monthly investment amounts in euros.
# 2. Process, function by function: The first function calculates the total invested. The second counts the investments. The third finds the largest investment. The fourth uses these three results to calculate how much the largest investment exceeds the average.
# 3. Out: The results of the three individual functions and the difference between the largest investment and the average.
# 4. The question my fourth function answers: How much higher is the largest monthly investment than the average? Splitting the calculation into three functions makes it easier to test each calculation separately and identify errors.


# Your code below

investments = [500, 650, 400, 750, 600, 900, 550, 800]

def calculate_total(amounts):
    return sum(amounts)

def count_investments(amounts):
    return len(amounts)

def find_largest(amounts):
    return max(amounts)

def compare_to_average(amounts):
    total = calculate_total(amounts)
    count = count_investments(amounts)
    largest = find_largest(amounts)
    return largest - (total / count)

# Test the three functions separately
print("Total test:", calculate_total(investments[:3]))
print("Count test:", count_investments(investments[:3]))
print("Largest test:", find_largest(investments[:3]))

# Final result
print("Difference from average:", compare_to_average(investments))


# TEST RESULTS
# calculate_total([500, 650, 400]): Expected 1550, correct.
# count_investments([500, 650, 400]): Expected 3, correct.
# find_largest([500, 650, 400]): Expected 650, correct.
