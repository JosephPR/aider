from app import app, db, Player

def add_sample_players():
    players = [
        {
            "name": "Mike Trout",
            "team": "Los Angeles Angels",
            "position": "CF",
            "batting_average": 0.296,
            "home_runs": 40,
            "rbi": 95,
            "ops": 0.972
        },
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
        }
    ]

    for player_data in players:
        player = Player(**player_data)
        db.session.add(player)
    
    db.session.commit()

if __name__ == '__main__':
    with app.app_context():
        add_sample_players()
