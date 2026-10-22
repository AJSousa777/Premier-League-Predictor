import csv #Python's CSV module - to read CSV files
from pathlib import Path #library

project_root = Path (__file__).resolve().parent.parent
file_path = project_root / "data" / "premier_league_2026_27.csv"

#"open" = opens the file so Python can read it.   "with" = closes the file when finished.
#"r" = read mode.   "newline" = self-explanatory.
with open (file_path, "r", newline="", encoding="utf-8-sig") as csv_file:
    reader = csv.DictReader(csv_file) #reads each row as a dictionary, using column names as keys.
                                      #example: row["HomeTeam"] accesses the home team's name

    rows = list(reader) #loads all rows into a Python list.

print(f"Total matches in file: {len(rows)}") #"len(rows)" = return number of data rows
print(f"Column names: {reader.fieldnames}")  

completed_matches = [] #empty  to store completed matches (matches with valid results)

#FTHG = home team's full-time goals
#FTAG = away team's full-time goals
#FTR = full-time result
for row in rows:
    if row["FTHG"] != "" and row["FTAG"] != "" and row["FTR"] != "":
        completed_matches.append(row)

print(f"completed matches: {len(completed_matches)}")

invalid_results = [] #empty list to store rows with invalid results

for row in rows:
    try: #try the following code, if it fails, go to the "except" block
        home_goals = int(row["FTHG"]) #convert home goals to integer
        away_goals = int(row["FTAG"]) #convert away goals to integer
    except ValueError: #if conversion fails (i.e., the value is not a valid integer)
        invalid_results.append(row) 
        continue

#calculate expected result based on home and away goals
    if home_goals > away_goals:
        expected_result = "H"
    elif home_goals < away_goals:
        expected_result = "A"
    else:
        expected_result = "D"

#check if the actual result matches the calculated result
    if row["FTR"] != expected_result:
        invalid_results.append(row)

print(f"Rows with invalid results: {len(invalid_results)}")

print("\nChecking the raw CSV values:") #print a heading so we can identify this diagnostic output.
for row in rows[:5]:  # Display the first 5 rows for inspection
    print("FTHG:", repr(row["FTHG"])) #show the home team's goals exatcly as Python reads the value
    print("FTAG:", repr(row["FTAG"])) #show the away team's goals exactly as Python reads the value 
    print("FTR:", repr(row["FTR"])) #show the recorded full-time result exactly as Python reads the value

empty_rows = sum(
    1 for row in rows #count this row if any of the required fields are empty
    if row["FTHG"] == "" or row["FTAG"] == "" or row["FTR"] == ""
)

#Display how many rows have missing values in those fields
print("Rows with empty result field:", empty_rows)