from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    team = db.Column(db.String(3))
    position = db.Column(db.String(2))
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
    sacrifice_hits = db.Column(db.Integer)
    sacrifice_flies = db.Column(db.Integer)
    hit_by_pitch = db.Column(db.Integer)
    avg = db.Column(db.String(4))
    obp = db.Column(db.String(4))
    slg = db.Column(db.String(4))
    ops = db.Column(db.String(4))

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'team': self.team,
            'position': self.position,
            'age': self.age,
            'games': self.games,
            'at_bats': self.at_bats,
            'runs': self.runs,
            'hits': self.hits,
            'doubles': self.doubles,
            'triples': self.triples,
            'home_runs': self.home_runs,
            'rbi': self.rbi,
            'stolen_bases': self.stolen_bases,
            'caught_stealing': self.caught_stealing,
            'walks': self.walks,
            'strikeouts': self.strikeouts,
            'sacrifice_hits': self.sacrifice_hits,
            'sacrifice_flies': self.sacrifice_flies,
            'hit_by_pitch': self.hit_by_pitch,
            'avg': self.avg,
            'obp': self.obp,
            'slg': self.slg,
            'ops': self.ops
        }
