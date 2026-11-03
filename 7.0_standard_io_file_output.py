"""Exercise 7.0 — Collecting data and saving it

WHAT THE PROGRAM MUST DO
    Ask the user for the information needed to record one entry, then save it to a CSV
    file. Running the program twice must produce two entries, not overwrite the first.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?  (name your file, and list your columns)
    4. Which columns did you choose, and what would you actually do with this file once
       it has two hundred rows in it?

WHAT THE AI CANNOT KNOW
    Your columns. They must be the ones you would really need to collect for a purpose
    you can state. See 7.0_student_data.csv for the shape of a header line, not for
    the columns to use.

    Two behaviours are yours to decide, and an assistant will guess them wrong:
    what happens the very first time, when the file does not exist yet and needs its
    header line, and what happens when a value the user typed is not acceptable.

CHECK IT YOURSELF
    Run your program three times with different values. Then open the file and count
    the lines. You should have three entries and exactly one header line. If you have
    three header lines, or one entry, your program is wrong.

DELIVERABLE
    This file, plus the CSV your program produced.
"""

# 1. In: The client's name, asset name, number of shares, and price per share.
# 2. Process: Collect the information, check that the values are valid, and save the data to a CSV file. If the file already exists, add a new entry without deleting previous records.
# 3. Out, file name and columns: A CSV file named investment_records.csv containing four columns: client_name, asset_name, shares, and price_eur.
# 4. Why these columns, and what this file is for: These columns allow a wealth manager to identify clients, track their investments, and monitor their holdings. With 200 records, the file could be used to analyse investment positions and calculate portfolio values.


# Your code below

import csv
import os

file_name = "investment_records.csv"

client_name = input("Enter client name: ").strip()
asset_name = input("Enter asset name: ").strip()
shares_text = input("Enter number of shares: ")
price_text = input("Enter price per share in EUR: ")

try:
    shares = int(shares_text)
    price = float(price_text)
except ValueError:
    print("Invalid input: shares must be a whole number and price must be numeric.")
else:
    if not client_name or not asset_name or shares <= 0 or price <= 0:
        print("Invalid input: complete all fields and use positive numbers.")
    else:
        new_file = not os.path.exists(file_name) or os.path.getsize(file_name) == 0

        with open(file_name, "a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file, delimiter=";")

            if new_file:
                writer.writerow(["client_name", "asset_name", "shares", "price_eur"])

            writer.writerow([client_name, asset_name, shares, price])

        print("Investment entry saved to", file_name)

# TEST RESULTS
# The program successfully created the CSV file.
# Running the program three times produced three entries.
# The CSV contains exactly one header line.
# Previous entries were preserved without being overwritten.
# Invalid numerical inputs are rejected without saving an entry.
# Everything worked as expected.