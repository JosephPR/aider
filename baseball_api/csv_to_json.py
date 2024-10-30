import csv
import json

def convert_csv_to_json():
    players = []
    
    with open('baseball_api/mlb-player-stats-Batters.csv', 'r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Convert numeric strings to appropriate types
            player = {
                'name': row['Player'],
                'team': row['Team'],
                'position': row['Pos'],
                'age': int(row['Age']),
                'games': int(row['G']),
                'at_bats': int(row['AB']),
                'runs': int(row['R']),
                'hits': int(row['H']),
                'doubles': int(row['2B']),
                'triples': int(row['3B']),
                'home_runs': int(row['HR']),
                'rbi': int(row['RBI']),
                'stolen_bases': int(row['SB']),
                'caught_stealing': int(row['CS']),
                'walks': int(row['BB']),
                'strikeouts': int(row['SO']),
                'batting_average': float(row['AVG']),
                'on_base_pct': float(row['OBP']),
                'slugging_pct': float(row['SLG']),
                'ops': float(row['OPS'])
            }
            players.append(player)
    
    with open('baseball_api/players.json', 'w') as f:
        json.dump(players, f, indent=2)

if __name__ == '__main__':
    convert_csv_to_json()
