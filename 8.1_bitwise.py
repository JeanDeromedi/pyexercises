"""Exercise 8.1 — Bitwise operators (bonus, not graded)

WHAT THE PROGRAM MUST DO
    Represent a set of permissions as bits, combine two of them, test whether a third is
    present, then add it and remove one.

ANSWER THESE FIRST, in comments
    1. What goes in? Three marketing permissions represented by binary values.
    2. What happens to it? Combine, check, add and remove permissions using bitwise operators.
    3. What comes out? The updated permissions displayed in binary.
    4. What are your permissions about? Not files: invent a set from your own field, View, edit and publish a marketing campaign.
       such as who may view, edit and publish a campaign.

WHAT THE AI CANNOT KNOW
    Your permission set and what each one means in your context.

CHECK IT YOURSELF
    Display the value in binary at each step and read the bits yourself.

DELIVERABLE
    This file, with your comments and your code.
"""

# Your code below

# Marketing campaign permissions
VIEW = 1
EDIT = 2
PUBLISH = 4

# Combine two permissions
permissions = VIEW | EDIT
print("Initial permissions:", bin(permissions))

# Check if publishing is allowed
has_publish = (permissions & PUBLISH) != 0
print("Can publish:", has_publish)

# Add publishing permission
permissions = permissions | PUBLISH
print("After adding publish:", bin(permissions))

# Remove editing permission
permissions = permissions & ~EDIT
print("After removing edit:", bin(permissions))

# Check the final permissions
print("Can view:", (permissions & VIEW) != 0)
print("Can edit:", (permissions & EDIT) != 0)
print("Can publish:", (permissions & PUBLISH) != 0)

# TEST RESULTS
# Combining VIEW and EDIT gives 0b11.
# Adding PUBLISH gives 0b111.
# Removing EDIT gives 0b101.
# Final permissions allow viewing and publishing, but not editing.