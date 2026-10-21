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

completed_matches = [] #empty list

#FTHG = home team's full-time goals
#FTAG = away team's full-time goals
#FTR = full-time result
for row in rows:
    if row["FTHG"] != "" and row["FTAG"] != "" and row["FTR"] != "":
        completed_matches.append(row)

print(f"completed matches: {len(completed_matches)}")
print(f"Rows without a complete result: {len(rows) - len(completed_matches)}")