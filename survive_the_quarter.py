# First name: Jean
# Last name: Arnaud-Deromedi
# Group: A 
#
# 1. What goes in?
#    scenarios_A.csv uses commas and has 14 columns: ID, Scenario, three
#    option texts, three budget changes, three reputation changes and three
#    feedback messages. The changes are signed whole numbers (like -800, 15).
#    The player also enters a name and a choice of A, B or C each day.
#
# 2. What happens?
#    Load and check the scenarios from my group's CSV file.
#    Shuffle the scenarios and select ten for the game.
#    Show the day, both gauges, the situation and all three options.
#    Ask again for a choice until A, B or C is entered.
#    Apply the chosen changes and limit reputation to a maximum of 100.
#    Record the move and stop immediately if either gauge reaches zero.
#    Show the result and the best and worst reputation moves.
#    Compare the budget with earlier games and append the result to a CSV.
#
# 3. What comes out?
#    The player sees each day's choices, consequences, gauges, and final
#    result (fired or a title), with the best and worst moves.
#    results.csv has one row per game: name,budget,reputation,title,date.
#
# 4. What could go wrong?
#    An invalid choice: keep asking until the player enters A, B or C.
#    Budget or reputation reaches 0 or less: fire the player immediately.
#    Reputation goes above 100: cap it at 100.
#    Missing or invalid scenario file: show an explanation and exit safely.
#    Empty player name: ask again before starting the game.
#
# Chosen feature: C - High score.
# I chose it to compare each player's remaining budget against past games,
# without changing the starting conditions of 10,000 EUR and 50 reputation.

import csv
import random
from datetime import date
from pathlib import Path

# Keep game files beside this Python script so Codespaces can find them.
FOLDER = Path(__file__).resolve().parent
SCENARIO_FILE = FOLDER / "scenarios_A.csv"
RESULTS_FILE = FOLDER / "results.csv"
EXPECTED_COLUMNS = [
    "ID", "Scenario", "OptionA", "OptionB", "OptionC",
    "BudgetA", "BudgetB", "BudgetC",
    "ReputationA", "ReputationB", "ReputationC",
    "FeedbackA", "FeedbackB", "FeedbackC",
]


# Read the real Group A columns and convert changes into numbers.
def load_scenarios(filename):
    scenarios = []
    with open(filename, "r", newline="", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file, delimiter=",")
        if reader.fieldnames != EXPECTED_COLUMNS:
            raise ValueError("The scenario file has unexpected columns.")
        for row in reader:
            if not row["Scenario"]:
                raise ValueError("A scenario has no situation text.")
            options = {}
            for letter in "ABC":
                options[letter] = (
                    row["Option" + letter],
                    int(row["Budget" + letter]),
                    int(row["Reputation" + letter]),
                    row["Feedback" + letter],
                )
            scenarios.append({"id": int(row["ID"]), "story": row["Scenario"], "options": options})
    if len(scenarios) < 10:
        raise ValueError("At least ten scenarios are required.")
    return scenarios


# Ask until a real name is entered; do not accept an empty name.
def get_player_name():
    while True:
        name = input("Player name: ").strip()
        if name:
            return name
        print("Please enter a name.")


# Ask for one of the three allowed answers, including lowercase choices.
def get_valid_choice():
    while True:
        choice = input("Your choice (A, B or C): ").strip().upper()
        if choice in ("A", "B", "C"):
            return choice
        print("Please type A, B or C.")


# Return the two new gauges as a tuple, keeping reputation at 100 or less.
def apply_choice(budget, reputation, option):
    text, budget_change, reputation_change, feedback = option
    return budget + budget_change, min(100, reputation + reputation_change)


# Translate the final surviving score into one of the four titles.
def get_title(budget, reputation):
    score = reputation + budget // 200
    if score < 95:
        return "Eternal Intern", score
    if score < 120:
        return "Growth Hacker", score
    if score < 140:
        return "CMO Material", score
    return "Viral Legend", score


# Compare this game's remaining budget to earlier saved games (feature C).
def show_high_score(budget):
    previous_budgets = []
    if RESULTS_FILE.exists():
        with open(RESULTS_FILE, "r", newline="", encoding="utf-8") as file:
            for row in csv.DictReader(file):
                try:
                    previous_budgets.append(int(row["budget"]))
                except (ValueError, TypeError, KeyError):
                    continue
    if not previous_budgets:
        print("High score: this is the first recorded budget!")
    elif budget > max(previous_budgets):
        print("NEW HIGH SCORE! Previous best budget:", max(previous_budgets), "EUR")
    else:
        print("High score to beat:", max(previous_budgets), "EUR")
        print("Your budget:", budget, "EUR - record not beaten.")


# Append one completed game to results.csv; write the header only once.
def save_result(name, budget, reputation, title):
    needs_header = not RESULTS_FILE.exists() or RESULTS_FILE.stat().st_size == 0
    with open(RESULTS_FILE, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        if needs_header:
            writer.writerow(["name", "budget", "reputation", "title", "date"])
        writer.writerow([name, budget, reputation, title, date.today().isoformat()])
    print("Saved in results.csv")


# Play ten randomly ordered scenarios, or stop as soon as a gauge is empty.
def play_game():
    try:
        scenarios = load_scenarios(SCENARIO_FILE)
    except (OSError, ValueError, csv.Error) as error:
        print("Cannot start: problem reading scenarios_A.csv:", error)
        return

    print("=== CROISSANT ROCKET: SURVIVE THE QUARTER ===")
    try:
        name = get_player_name()
        budget = 10000
        reputation = 50
        history = []  # One tuple per played day: (day, choice text, actual reputation change)
        random.shuffle(scenarios)

        for day, scenario in enumerate(scenarios[:10], start=1):
            print("\n--- Day", day, "---")
            print("[Budget:", budget, "EUR | Reputation:", str(reputation) + "/100]")
            print(scenario["story"])
            for letter in "ABC":
                print("  " + letter + ": " + scenario["options"][letter][0])

            choice = get_valid_choice()
            option = scenario["options"][choice]
            choice_text, change_budget, change_rep, feedback = option
            previous_reputation = reputation
            budget, reputation = apply_choice(budget, reputation, option)
            history.append((day, choice_text, reputation - previous_reputation))
            print(feedback)
            print("Budget change:", f"{change_budget:+d}", "EUR | Reputation change:", f"{change_rep:+d}")
            print("Now: Budget", budget, "EUR | Reputation", reputation, "/100")

            if budget <= 0 or reputation <= 0:
                break
    except (EOFError, KeyboardInterrupt):
        print("\nGame interrupted. No result saved.")
        return

    # Show a firing reason or calculate the score only for surviving players.
    print("\n==============================")
    if budget <= 0 or reputation <= 0:
        title = "Fired"
        reasons = []
        if budget <= 0:
            reasons.append("budget reached zero")
        if reputation <= 0:
            reasons.append("reputation reached zero")
        print(name + ", you're fired: " + " and ".join(reasons) + ".")
    else:
        title, score = get_title(budget, reputation)
        print("Quarter survived!")
        print("Final score:", score)
        print(name + ", your title:", title)
    print("Budget left:", budget, "EUR | Reputation:", str(reputation) + "/100")

    # Tuple history lets us compare reputation changes and name the move.
    if history:
        best = max(history, key=lambda move: move[2])
        worst = min(history, key=lambda move: move[2])
        print("Best move: day", best[0], "-", best[1], f"({best[2]:+d} reputation)")
        print("Worst move: day", worst[0], "-", worst[1], f"({worst[2]:+d} reputation)")

    # The optional feature reads previous budgets before saving the new one.
    try:
        show_high_score(budget)
        save_result(name, budget, reputation, title)
    except (OSError, csv.Error) as error:
        print("Could not save or read results.csv:", error)


# Start the game only when this file is run directly.
if __name__ == "__main__":
    play_game()
