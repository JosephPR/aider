import csv
from app import app, db, Player

def add_sample_players():
    # Clear existing players
    db.session.query(Player).delete()
    
    # Read CSV and add players
    with open('mlb-player-stats-Batters.csv', 'r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        for row in reader:
            player = Player(
                name=row['Player'],
                team=row['Team'],
                position=row['Pos'],
                age=int(row['Age']),
                games=int(row['G']),
                at_bats=int(row['AB']),
                runs=int(row['R']),
                hits=int(row['H']),
                doubles=int(row['2B']),
                triples=int(row['3B']),
                home_runs=int(row['HR']),
                rbi=int(row['RBI']),
                stolen_bases=int(row['SB']),
                caught_stealing=int(row['CS']),
                walks=int(row['BB']),
                strikeouts=int(row['SO']),
                batting_average=float(row['AVG']),
                on_base_pct=float(row['OBP']),
                slugging_pct=float(row['SLG']),
                ops=float(row['OPS'])
            )
            db.session.add(player)
        {
            "name": "Shohei Ohtani",
            "team": "Los Angeles Dodgers",
            "position": "DH/SP",
            "batting_average": 0.304,
            "home_runs": 44,
            "rbi": 95,
            "ops": 1.066,
            "era": 3.14,
            "wins": 10,
            "losses": 5,
            "strikeouts": 167
        },
        {
            "name": "Aaron Judge",
            "team": "New York Yankees",
            "position": "RF",
            "batting_average": 0.267,
            "home_runs": 37,
            "rbi": 75,
            "ops": 0.988
        },
        {
            "name": "Mookie Betts",
            "team": "Los Angeles Dodgers",
            "position": "RF",
            "batting_average": 0.307,
            "home_runs": 39,
            "rbi": 107,
            "ops": 0.987
        },
        {
            "name": "Ronald Acuña Jr.",
            "team": "Atlanta Braves",
            "position": "RF",
            "batting_average": 0.337,
            "home_runs": 41,
            "rbi": 106,
            "ops": 1.012
        },
        {
            "name": "Juan Soto",
            "team": "San Diego Padres",
            "position": "RF",
            "batting_average": 0.275,
            "home_runs": 35,
            "rbi": 109,
            "ops": 0.928
        },
        {
            "name": "Freddie Freeman",
            "team": "Los Angeles Dodgers",
            "position": "1B",
            "batting_average": 0.331,
            "home_runs": 29,
            "rbi": 102,
            "ops": 0.976
        },
        {
            "name": "Gerrit Cole",
            "team": "New York Yankees",
            "position": "SP",
            "era": 2.63,
            "wins": 15,
            "losses": 4,
            "strikeouts": 222
        },
        {
            "name": "Spencer Strider",
            "team": "Atlanta Braves",
            "position": "SP",
            "era": 3.86,
            "wins": 20,
            "losses": 5,
            "strikeouts": 281
        },
        {
            "name": "Corbin Burnes",
            "team": "Milwaukee Brewers",
            "position": "SP",
            "era": 3.39,
            "wins": 10,
            "losses": 8,
            "strikeouts": 200
        },
        {
            "name": "Matt Olson",
            "team": "Atlanta Braves",
            "position": "1B",
            "batting_average": 0.283,
            "home_runs": 54,
            "rbi": 139,
            "ops": 0.993
        },
        {
            "name": "Pete Alonso",
            "team": "New York Mets",
            "position": "1B",
            "batting_average": 0.217,
            "home_runs": 46,
            "rbi": 118,
            "ops": 0.827
        },
        {
            "name": "Julio Rodríguez",
            "team": "Seattle Mariners",
            "position": "CF",
            "batting_average": 0.275,
            "home_runs": 32,
            "rbi": 103,
            "ops": 0.818
        },
        {
            "name": "Francisco Lindor",
            "team": "New York Mets",
            "position": "SS",
            "batting_average": 0.254,
            "home_runs": 31,
            "rbi": 98,
            "ops": 0.810
        },
        {
            "name": "Trea Turner",
            "team": "Philadelphia Phillies",
            "position": "SS",
            "batting_average": 0.266,
            "home_runs": 26,
            "rbi": 76,
            "ops": 0.778
        },
        {
            "name": "Justin Verlander",
            "team": "Houston Astros",
            "position": "SP",
            "era": 3.22,
            "wins": 13,
            "losses": 8,
            "strikeouts": 144
        },
        {
            "name": "Max Scherzer",
            "team": "Texas Rangers",
            "position": "SP",
            "era": 3.77,
            "wins": 13,
            "losses": 6,
            "strikeouts": 174
        },
        {
            "name": "Bobby Witt Jr.",
            "team": "Kansas City Royals",
            "position": "SS",
            "batting_average": 0.276,
            "home_runs": 30,
            "rbi": 96,
            "ops": 0.813
        },
        {
            "name": "Adley Rutschman",
            "team": "Baltimore Orioles",
            "position": "C",
            "batting_average": 0.277,
            "home_runs": 20,
            "rbi": 80,
            "ops": 0.809
        },
        {
            "name": "Gunnar Henderson",
            "team": "Baltimore Orioles",
            "position": "3B",
            "batting_average": 0.255,
            "home_runs": 28,
            "rbi": 82,
            "ops": 0.814
        },
        {
            "name": "Zac Gallen",
            "team": "Arizona Diamondbacks",
            "position": "SP",
            "era": 3.47,
            "wins": 17,
            "losses": 9,
            "strikeouts": 220
        },
        {
            "name": "Blake Snell",
            "team": "San Diego Padres",
            "position": "SP",
            "era": 2.25,
            "wins": 14,
            "losses": 9,
            "strikeouts": 234
        },
        {
            "name": "Marcus Semien",
            "team": "Texas Rangers",
            "position": "2B",
            "batting_average": 0.276,
            "home_runs": 29,
            "rbi": 100,
            "ops": 0.826
        },
        {
            "name": "Corey Seager",
            "team": "Texas Rangers",
            "position": "SS",
            "batting_average": 0.327,
            "home_runs": 33,
            "rbi": 96,
            "ops": 1.013
        },
        {
            "name": "Josh Jung",
            "team": "Texas Rangers",
            "position": "3B",
            "batting_average": 0.266,
            "home_runs": 23,
            "rbi": 70,
            "ops": 0.785
        },
        {
            "name": "Yordan Alvarez",
            "team": "Houston Astros",
            "position": "DH",
            "batting_average": 0.293,
            "home_runs": 31,
            "rbi": 97,
            "ops": 1.019
        },
        {
            "name": "Kyle Tucker",
            "team": "Houston Astros",
            "position": "RF",
            "batting_average": 0.284,
            "home_runs": 29,
            "rbi": 112,
            "ops": 0.834
        },
        {
            "name": "Jose Altuve",
            "team": "Houston Astros",
            "position": "2B",
            "batting_average": 0.311,
            "home_runs": 17,
            "rbi": 51,
            "ops": 0.887
        },
        {
            "name": "Paul Goldschmidt",
            "team": "St. Louis Cardinals",
            "position": "1B",
            "batting_average": 0.268,
            "home_runs": 25,
            "rbi": 80,
            "ops": 0.810
        },
        {
            "name": "Nolan Arenado",
            "team": "St. Louis Cardinals",
            "position": "3B",
            "batting_average": 0.266,
            "home_runs": 26,
            "rbi": 93,
            "ops": 0.774
        },
        {
            "name": "Randy Arozarena",
            "team": "Tampa Bay Rays",
            "position": "LF",
            "batting_average": 0.254,
            "home_runs": 23,
            "rbi": 83,
            "ops": 0.772
        },
        {
            "name": "Wander Franco",
            "team": "Tampa Bay Rays",
            "position": "SS",
            "batting_average": 0.281,
            "home_runs": 17,
            "rbi": 58,
            "ops": 0.819
        },
        {
            "name": "Bo Bichette",
            "team": "Toronto Blue Jays",
            "position": "SS",
            "batting_average": 0.306,
            "home_runs": 20,
            "rbi": 73,
            "ops": 0.814
        },
        {
            "name": "Vladimir Guerrero Jr.",
            "team": "Toronto Blue Jays",
            "position": "1B",
            "batting_average": 0.264,
            "home_runs": 26,
            "rbi": 94,
            "ops": 0.788
        },
        {
            "name": "George Springer",
            "team": "Toronto Blue Jays",
            "position": "CF",
            "batting_average": 0.258,
            "home_runs": 21,
            "rbi": 72,
            "ops": 0.736
        },
        {
            "name": "Luis Robert Jr.",
            "team": "Chicago White Sox",
            "position": "CF",
            "batting_average": 0.264,
            "home_runs": 38,
            "rbi": 80,
            "ops": 0.857
        },
        {
            "name": "Elly De La Cruz",
            "team": "Cincinnati Reds",
            "position": "SS",
            "batting_average": 0.235,
            "home_runs": 13,
            "rbi": 44,
            "ops": 0.710
        },
        {
            "name": "Corbin Carroll",
            "team": "Arizona Diamondbacks",
            "position": "CF",
            "batting_average": 0.285,
            "home_runs": 25,
            "rbi": 76,
            "ops": 0.868
        },
        {
            "name": "Christian Yelich",
            "team": "Milwaukee Brewers",
            "position": "LF",
            "batting_average": 0.278,
            "home_runs": 19,
            "rbi": 76,
            "ops": 0.818
        },
        {
            "name": "Jazz Chisholm Jr.",
            "team": "Miami Marlins",
            "position": "CF",
            "batting_average": 0.250,
            "home_runs": 19,
            "rbi": 51,
            "ops": 0.764
        },
        {
            "name": "Sandy Alcántara",
            "team": "Miami Marlins",
            "position": "SP",
            "era": 4.14,
            "wins": 7,
            "losses": 12,
            "strikeouts": 151
        },
        {
            "name": "Justin Steele",
            "team": "Chicago Cubs",
            "position": "SP",
            "era": 3.06,
            "wins": 16,
            "losses": 5,
            "strikeouts": 176
        },
        {
            "name": "Dansby Swanson",
            "team": "Chicago Cubs",
            "position": "SS",
            "batting_average": 0.244,
            "home_runs": 22,
            "rbi": 80,
            "ops": 0.736
        },
        {
            "name": "Cody Bellinger",
            "team": "Chicago Cubs",
            "position": "CF",
            "batting_average": 0.307,
            "home_runs": 26,
            "rbi": 97,
            "ops": 0.881
        },
        {
            "name": "Bryce Harper",
            "team": "Philadelphia Phillies",
            "position": "DH",
            "batting_average": 0.293,
            "home_runs": 21,
            "rbi": 72,
            "ops": 0.900
        },
        {
            "name": "J.T. Realmuto",
            "team": "Philadelphia Phillies",
            "position": "C",
            "batting_average": 0.252,
            "home_runs": 20,
            "rbi": 63,
            "ops": 0.762
        },
        {
            "name": "Kyle Schwarber",
            "team": "Philadelphia Phillies",
            "position": "DH",
            "batting_average": 0.197,
            "home_runs": 47,
            "rbi": 104,
            "ops": 0.813
        },
        {
            "name": "Zack Wheeler",
            "team": "Philadelphia Phillies",
            "position": "SP",
            "era": 3.61,
            "wins": 13,
            "losses": 6,
            "strikeouts": 212
        },
        {
            "name": "Aaron Nola",
            "team": "Philadelphia Phillies",
            "position": "SP",
            "era": 4.46,
            "wins": 12,
            "losses": 9,
            "strikeouts": 202
        },
        {
            "name": "Francisco Álvarez",
            "team": "New York Mets",
            "position": "C",
            "batting_average": 0.209,
            "home_runs": 25,
            "rbi": 63,
            "ops": 0.721
        },
        {
            "name": "Kodai Senga",
            "team": "New York Mets",
            "position": "SP",
            "era": 2.98,
            "wins": 12,
            "losses": 7,
            "strikeouts": 202
        },
        {
            "name": "Brandon Woodruff",
            "team": "Milwaukee Brewers",
            "position": "SP",
            "era": 2.28,
            "wins": 5,
            "losses": 1,
            "strikeouts": 74
        },
        {
            "name": "Devin Williams",
            "team": "Milwaukee Brewers",
            "position": "RP",
            "era": 1.53,
            "wins": 8,
            "losses": 3,
            "saves": 36,
            "strikeouts": 87
        },
        {
            "name": "Josh Hader",
            "team": "San Diego Padres",
            "position": "RP",
            "era": 1.28,
            "wins": 2,
            "losses": 3,
            "saves": 33,
            "strikeouts": 85
        }
    ]

    for player_data in players:
        player = Player(**player_data)
        db.session.add(player)
    
    db.session.commit()

if __name__ == '__main__':
    with app.app_context():
        add_sample_players()
