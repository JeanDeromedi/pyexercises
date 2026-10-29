"""Exercise 3.0 — Computing with what the user typed

WHAT THE PROGRAM MUST DO
    Ask for two numbers and display the result of the four operations.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What should your program do when the second number is zero? Decide, write your
       decision down, and only then implement it.

WHAT THE AI CANNOT KNOW
    Your answer to question 4. There are at least three defensible ones: refuse the
    value and ask again, display a message instead of a result, or stop the program.
    Pick one and be able to defend it.

CHECK IT YOURSELF
    Compute 7 divided by 2 in your head. Run your program with 7 and 2. If your program
    shows 3, it is not wrong by accident: find out why, and write the reason in a comment.
    Then run it with 0 as the second number.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: Two numbers entered by the user.
# 2. Process: Perform addition, subtraction, multiplication, and division using the two numbers.
# 3. Out: Display the results of the four calculations.
# 4. What happens when the second number is zero, and why: The program displays an error message for division because dividing by zero is impossible. The other three operations still work.


# Your code below
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)

if num2 == 0:
    print("Division: Cannot divide by zero.")
else:
    print("Division:", num1 / num2)


# TEST RESULTS
# 7 / 2 gives 3.5 as expected.
# The / operator performs normal division.
# The // operator would give 3.0 because it uses floor division.
# When the second number is 0, the program displays an error
# message for division while the other operations still work.
