import csv
import shutil
import pandas as pd
from tempfile import NamedTemporaryFile

############## Leaderboard (CSV) ################


class Results:
    def __init__(self):
        self.col = ['Name', 'Wins', 'Losses']

    # Adding up new scores with previous scores using temp file
    def update_total(self, username, wins, losses):
        tempfile = NamedTemporaryFile(mode='w', delete=False)
        with open('leaderboard_total.csv', 'r') as csvfile, tempfile:
            reader = csv.DictReader(csvfile, fieldnames=self.col)
            writer = csv.DictWriter(tempfile, fieldnames=self.col)
            for row in reader:
                if row['Name'] == username:
                    print(f"Updating results for {row['Name']}...")
                    row['Wins'], row['Losses'] = int(
                        row['Wins']) + int(wins), int(row['Losses']) + int(losses)
                row = {'Name': row['Name'], 'Wins': row['Wins'],
                       'Losses': row['Losses']}
                writer.writerow(row)

        shutil.move(tempfile.name, 'leaderboard_total.csv')
        self.sort_leaderboard()

    # Sorting and reading the leaderboard results to player
    def sort_leaderboard(self):
        dataFrame = pd.read_csv("leaderboard_total.csv")
        dataFrame.sort_values(by='Wins', ascending=False,
                              inplace=True, na_position='first')

        print("\nSorted by wins:\n", dataFrame)


results = Results()
