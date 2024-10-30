from flask import Flask, jsonify, request, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__, 
    template_folder='baseball_stats/templates',
    static_folder='baseball_stats/static')
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///baseball_stats.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    team = db.Column(db.String(50))
    position = db.Column(db.String(20))
    age = db.Column(db.Integer)
    games = db.Column(db.Integer)
    at_bats = db.Column(db.Integer)
    runs = db.Column(db.Integer)
    hits = db.Column(db.Integer)
    doubles = db.Column(db.Integer)
    triples = db.Column(db.Integer)
    home_runs = db.Column(db.Integer)
    rbi = db.Column(db.Integer)
    stolen_bases = db.Column(db.Integer)
    caught_stealing = db.Column(db.Integer)
    walks = db.Column(db.Integer)
    strikeouts = db.Column(db.Integer)
    batting_average = db.Column(db.Float)
    on_base_pct = db.Column(db.Float)
    slugging_pct = db.Column(db.Float)
    ops = db.Column(db.Float)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)


@app.route('/api/players', methods=['GET', 'POST'])
def get_players():
    if request.method == 'POST':
        data = request.json
        new_player = Player(
            name=data['name'],
            team=data['team'],
            position=data['position'],
            age=data.get('age'),
            games=data.get('games'),
            at_bats=data.get('at_bats'),
            runs=data.get('runs'), 
            hits=data.get('hits'),
            doubles=data.get('doubles'),
            triples=data.get('triples'),
            home_runs=data.get('home_runs'),
            rbi=data.get('rbi'),
            stolen_bases=data.get('stolen_bases'),
            caught_stealing=data.get('caught_stealing'),
            walks=data.get('walks'),
            strikeouts=data.get('strikeouts'),
            batting_average=data.get('batting_average'),
            on_base_pct=data.get('on_base_pct'),
            slugging_pct=data.get('slugging_pct'),
            ops=data.get('ops')
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

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from models import db, Player
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///baseball.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route('/api/players', methods=['GET'])
def get_players():
    players = Player.query.all()
    return jsonify([player.to_dict() for player in players])

@app.route('/api/players/<int:id>', methods=['GET'])
def get_player(id):
    player = Player.query.get_or_404(id)
    return jsonify(player.to_dict())

@app.route('/api/players/team/<team>', methods=['GET'])
def get_players_by_team(team):
    players = Player.query.filter_by(team=team.upper()).all()
    return jsonify([player.to_dict() for player in players])

@app.route('/api/players/position/<position>', methods=['GET'])
def get_players_by_position(position):
    players = Player.query.filter_by(position=position.upper()).all()
    return jsonify([player.to_dict() for player in players])

def init_db():
    with app.app_context():
        db.create_all()
        
        # Only load data if the database is empty
        if Player.query.first() is None:
            with open('mlb.json') as f:
                players_data = json.load(f)
                
            for data in players_data:
                player = Player(
                    name=data['Player'],
                    team=data['Team'],
                    position=data['Pos'],
                    age=data['Age'],
                    games=data['G'],
                    at_bats=data['AB'],
                    runs=data['R'],
                    hits=data['H'],
                    doubles=data['2B'],
                    triples=data['3B'],
                    home_runs=data['HR'],
                    rbi=data['RBI'],
                    stolen_bases=data['SB'],
                    caught_stealing=data['CS'],
                    walks=data['BB'],
                    strikeouts=data['SO'],
                    sacrifice_hits=data['SH'],
                    sacrifice_flies=data['SF'],
                    hit_by_pitch=data['HBP'],
                    avg=data['AVG'],
                    obp=data['OBP'],
                    slg=data['SLG'],
                    ops=data['OPS']
                )
                db.session.add(player)
            
            db.session.commit()

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
