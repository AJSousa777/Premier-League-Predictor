import csv
from pathlib import Path #library

project_root = Path (__file__).resolve().parent.parent #Find the project root folder by moving up from this script's location.
input_file = project_root / "data" / "prepared_matches.csv" #Build the path to the original Premier League CSV file.
output_file = project_root / "data" / "prepared_matches.csv" #Build the path to the output CSV file.

matches = [] #empty list to store the matches we want to keep.

with open(input_file, "r", newline="", encoding="utf-8-sig") as csv_file: #open OG CSV file in read mode
    reader = csv.DictReader(csv_file) #read each CSV row as a dictionary, using column names as keys.

    for row in reader: #process every match row in the original CSV file
        matches.append(row) #Store the current match row

print(f"Rows loaded: {len(matches)}") #print how many matches were loaded from the original dataset

if matches: print(f"Columns: {list(matches[0].keys())}") #print the column names in the original dataset

print("\nFirst five prepared matches:") #print the first five matches for inspection

for match in matches[:5]:
    print(match["Date"], match["HomeTeam"], match["AwayTeam"], match["HomeGoals"], match["AwayGoals"], match["Result"]) #print the first five matches in a readable format 