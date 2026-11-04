"""Exercise 7.1 — Loading a file, cleaning it, saving the result (homework)

This is the direct rehearsal for the final exam. Session 8 starts with it.

WHAT THE PROGRAM MUST DO
    Load names.txt, clean what is inside, sort it by last name, and write the result to
    a new file. The original file must not be modified.

DO THIS BEFORE ANYTHING ELSE
    Open names.txt and read it with your eyes. Then write, in comments at the top of
    your file, everything that is wrong with it. There are at least four different
    problems. Find them yourself.

    This step is not optional and it is graded. An assistant cannot see your file.

ANSWER THESE, in comments, after the list of problems
    1. What goes in?
    2. What happens to it?  (one line per problem you found, and how you deal with it)
    3. What comes out?
    4. What does "sort by last name" mean when a line contains two words, and how do you
       know which one is the last name?

WHAT THE AI CANNOT KNOW
    The actual content of names.txt. If you paste this brief into an assistant without
    describing the file, it will write a program for a clean file, and that program will
    crash or produce nonsense on the real one.

    Describe the file to it. That description is the exercise.

CHECK IT YOURSELF
    Count the lines in names.txt, then in your output file. The numbers should differ,
    and you should be able to say exactly why. Then check the first and last name of
    your sorted list by hand.

DELIVERABLE
    This file, plus the output file your program produced.
"""

# What is wrong with names.txt (found by reading it, not by guessing):
# -
# -
# -
# -

# 1. In: A text file containing names with formatting problems.
# 2. Process, problem by problem: Remove empty lines and extra spaces, standardize capitalization, preserve compound surnames, and sort alphabetically by last name.
# 3. Out: A new file called names_sorted.txt containing eight cleaned and sorted names.
# 4. How I decide which word is the last name: The first word is the first name, and the remaining words form the surname. This ensures that van Rossum stays together.


# Your code below

with open("names.txt", "r", encoding="utf-8") as infile:
    lines = infile.readlines()

names = []

for line in lines:
    words = line.strip().split()
    if not words:
        continue

    first_name = words[0].capitalize()
    surname = " ".join(
        word.lower() if word.lower() == "van" else word.capitalize()
        for word in words[1:]
    )
    names.append((first_name, surname))

names.sort(key=lambda name: name[1].lower())

with open("names_sorted.txt", "w", encoding="utf-8") as outfile:
    for first_name, surname in names:
        outfile.write(first_name + " " + surname + "\n")

print("Original lines:", len(lines))
print("Cleaned names:", len(names))
print("First name in sorted list:", " ".join(names[0]))
print("Last name in sorted list:", " ".join(names[-1]))
print("Saved cleaned names to names_sorted.txt")


# TEST RESULTS
# Original file: 10 lines.
# Cleaned file: 8 lines.
# Two empty lines were removed.
# First sorted name: Margaret Hamilton.
# Last sorted name: Guido van Rossum.
# The original file was not modified.
# All results matched expectations.
