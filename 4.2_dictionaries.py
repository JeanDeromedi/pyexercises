"""Exercise 4.2 — Working with a dictionary

WHAT THE PROGRAM MUST DO
    Describe one real object from your field using a dictionary of at least five fields,
    then read it, change it, remove one field, and display every field with its value.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What object did you describe, which five fields did you choose, and why those?
       A field you would never actually use does not count.

WHAT THE AI CANNOT KNOW
    Your object and your fields. A campaign, a customer, a product, a store, a supplier.
    Choose something you would genuinely have to describe in your job.

CHECK IT YOURSELF
    Ask your program for a field that does not exist. Note what happens in a comment,
    then make it survive that case.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: A dictionary containing information about a client's investment position.
# 2. Process: Read the investment information, update the number of shares, remove an unnecessary field, and check for a missing field.
# 3. Out: Display the updated investment information and a message if a field does not exist.
# 4. My object, my five fields, and why those: The object is a client's investment position. The fields are the client's name, asset name, stock ticker, number of shares, and share price. These help a wealth manager identify and monitor an investment. An additional note field is included for temporary information.


# Your code below
investment = {
    "client": "Jean",
    "asset": "Apple",
    "ticker": "AAPL",
    "shares": 10,
    "price": 190,
    "note": "Review investment"
}

# Read one field
print("Client:", investment["client"])

# Update the number of shares
investment["shares"] = 15

# Remove the note
del investment["note"]

# Display all remaining fields
for key, value in investment.items():
    print(key, ":", value)

# Check for a field that does not exist
print("Sector:", investment.get("sector", "Not available"))

# TEST RESULT
# Accessing a missing field using [] causes a KeyError.
# Using get() prevents the error and displays "Not available".