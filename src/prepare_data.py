import csv #Import Python's built-in CSV tools for reading and writing CSV files.
from pathlib import Path #Import Path to build file and folder paths safely.


project_root = Path(__file__).resolve().parent.parent #Find the project root folder by moving up from this script's location.
input_file = project_root / "data" / "premier_league_2026_27.csv" #Build the path to the original Premier League CSV file.
output_file = project_root / "data" / "prepared_matches.csv" #Build the path to the output CSV file.

prepared_matches = [] #empty list to store the matches we want to keep.

#open OG CSV file in read mode
with open(input_file, "r", newline="", encoding="utf-8-sig") as csv_file: 
    reader = csv.DictReader(csv_file) #read each CSV row as a dictionary, using column names as keys.

    #process every match row in the original CSV file
    for row in reader:
        if row["FTHG"] == "" and row["FTAG"] == "" and row["FTR"] == "": #Skip the row if any required result field is empty.
            continue

        #Create a smaller dictionary containing only the columns we need.
        match = {
            "Date": row["Date"], #keep the riginal match date
            "HomeTeam": row["HomeTeam"], #keep the original home team name
            "AwayTeam": row["AwayTeam"], #keep the original away team name
            "HomeGoals": row["FTHG"], #convert the home team's  goal amount from string 
            "AwayGoals": row["FTAG"], #convert the away team's goal amount from string
            "Result": row["FTR"] #keep the original full-time result (H, A, or D)
        }
        
        prepared_matches.append(match) #Add this prepared match dictionary to our list.

fieldnames = ["Date", "HomeTeam", "AwayTeam", "HomeGoals", "AwayGoals", "Result"] #Define the column names and their order in the output CSV.

with open(output_file, "w", newline="", encoding="utf-8-sig") as csv_file: #Open the output file in write mode, creating it or replacing its contents.
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames) #create a CSV writer that will write dictionaries to the file, using the specified column names.
    
    writer.writeheader() #write the column-name header as the first row of the CSV file.
    writer.writerows(prepared_matches) #write all the prepared match dictionaries to the CSV file, one row per dictionary.

print(f"Prepared matches: {len(prepared_matches)}") #print how many matches were written to the prepared dataset
print(f"saved to {output_file}") #print the path to the output file so we can find it easily.