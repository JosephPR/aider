from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///baseball_stats.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    team = db.Column(db.String(50))
    position = db.Column(db.String(20))
    batting_average = db.Column(db.Float)
    home_runs = db.Column(db.Integer)
    rbi = db.Column(db.Integer)
    ops = db.Column(db.Float)
    era = db.Column(db.Float)
    wins = db.Column(db.Integer)
    losses = db.Column(db.Integer)
    saves = db.Column(db.Integer)
    strikeouts = db.Column(db.Integer)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)

@app.route('/api/players', methods=['GET'])
def get_players():
    players = Player.query.all()
    return jsonify([{
        'id': player.id,
        'name': player.name,
        'team': player.team,
        'position': player.position,
        'batting_average': player.batting_average,
        'home_runs': player.home_runs,
        'rbi': player.rbi,
        'ops': player.ops,
        'era': player.era,
        'wins': player.wins,
        'losses': player.losses,
        'saves': player.saves,
        'strikeouts': player.strikeouts,
        'updated_at': player.updated_at.isoformat()
    } for player in players])

@app.route('/api/players', methods=['GET', 'POST'])
def get_players():
    if request.method == 'POST':
        data = request.json
        new_player = Player(
            name=data['name'],
            team=data['team'],
            position=data['position'],
            batting_average=data.get('batting_average'),
            home_runs=data.get('home_runs'),
            rbi=data.get('rbi'),
            ops=data.get('ops'),
            era=data.get('era'),
            wins=data.get('wins'),
            losses=data.get('losses'),
            saves=data.get('saves'),
            strikeouts=data.get('strikeouts')
        )
        db.session.add(new_player)
        db.session.commit()
        return jsonify({
            'message': 'Player created successfully',
            'id': new_player.id
        }), 201

    players = Player.query.all()
    return jsonify([{
        'id': player.id,
        'name': player.name,
        'team': player.team,
        'position': player.position,
        'batting_average': player.batting_average,
        'home_runs': player.home_runs,
        'rbi': player.rbi,
        'ops': player.ops,
        'era': player.era,
        'wins': player.wins,
        'losses': player.losses,
        'saves': player.saves,
        'strikeouts': player.strikeouts,
        'updated_at': player.updated_at.isoformat()
    } for player in players])

@app.route('/api/players/<int:player_id>', methods=['GET'])
def get_player(player_id):
    player = Player.query.get_or_404(player_id)
    return jsonify({
        'id': player.id,
        'name': player.name,
        'team': player.team,
        'position': player.position,
        'batting_average': player.batting_average,
        'home_runs': player.home_runs,
        'rbi': player.rbi,
        'ops': player.ops,
        'era': player.era,
        'wins': player.wins,
        'losses': player.losses,
        'saves': player.saves,
        'strikeouts': player.strikeouts,
        'updated_at': player.updated_at.isoformat()
    })

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
