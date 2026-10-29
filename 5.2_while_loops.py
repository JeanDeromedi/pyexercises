"""Exercise 5.2 — Repeating until something changes

WHAT THE PROGRAM MUST DO
    Keep asking the user something until a condition you define is met, then display a
    summary of what happened during the loop.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What is your stop condition, what is your maximum number of attempts, and what
       does your summary contain?

WHAT THE AI CANNOT KNOW
    Your stop condition and your safety limit. An assistant asked for a while loop will
    write one that can run for ever if the user never gives the expected answer. Decide
    how many attempts you allow, and what your program does when that limit is reached.

    Accepting "Yes", "yes" and " yes " as the same answer is your decision too. Make it
    and write it down.

CHECK IT YOURSELF
    Run it and never give the expected answer. If your program is still running after
    your stated maximum, it is wrong. Then run it and answer with capitals and extra
    spaces.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: The user's answer to a question asking them to confirm an investment review.
# 2. Process: Use a while loop to repeat the question until the user answers yes or reaches the maximum number of attempts.
# 3. Out: Display the number of attempts and whether the investment review was confirmed.
# 4. My stop condition, my attempt limit, my summary: The program stops when the user answers yes or after five attempts. It accepts uppercase letters and extra spaces. The summary displays the number of attempts and whether confirmation was successful.


# Your code below

attempts = 0
max_attempts = 5
confirmed = False

while attempts < max_attempts and not confirmed:
    answer = input("Confirm investment review (yes/no): ")
    answer = answer.strip().lower()
    attempts += 1

    if answer == "yes":
        confirmed = True

print("Total attempts:", attempts)

if confirmed:
    print("Investment review confirmed.")
else:
    print("Maximum attempts reached. Review not confirmed.")

# TEST RESULTS
# Five incorrect answers: The program stops after 5 attempts.
# Uppercase YES: The program accepts the answer.
# Extra spaces around yes: The program accepts the answer.
# The program displays the attempts and confirmation status.
