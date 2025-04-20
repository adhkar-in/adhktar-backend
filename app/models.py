from app import db

class Invocation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    arabic = db.Column(db.Text, nullable=False)
    phonetic = db.Column(db.Text)
    reference = db.Column(db.String(255))
    benefits = db.Column(db.Text)
    category = db.Column(db.String(100))
    audio_url = db.Column(db.String(255))
    translations = db.relationship('Translation', backref='invocation', lazy=True)

class Translation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    invocation_id = db.Column(db.Integer, db.ForeignKey('invocation.id'), nullable=False)
    language_code = db.Column(db.String(10), nullable=False)  # ex: 'fr', 'wo'
    text = db.Column(db.Text, nullable=False)
