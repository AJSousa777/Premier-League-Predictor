#libraries
from pathlib import Path
from urllib.request import urlretrieve

Data_URL = "https://football-data.co.uk/mmz4281/2627/E0.csv"    #Website adress stored in a variable

project_root = Path(__file__).resolve().parent.parent   #parents = source_folder & premier-league-predictor_folder (project_root)
data_folder = project_root / "data" #path to data folder
data_folder.mkdir(exist_ok=True) #make sure folder exists.

file_path = data_folder / "premier_league_2026_27.csv" # path to the file where the downloaded data will be saved

urlretrieve(Data_URL, file_path) #download the data

print(f"Data saved to: {file_path}") #confirmation

