from flask import url_for
from app import db
from app.models import Invocation, Translation

def seed_data():
    if Invocation.query.count() == 0:
        inv = Invocation(
            title="Après le réveil",
            arabic="الحَمْدُ للهِ الَّذِي أَحْيَانَا...",
            phonetic="Alhamdu lillahilladhi ahyana ba'dama amatana...",
            reference="Bukhari",
            benefits="Exprimer la gratitude...",
            category="Morning",
            audio_url= "http://localhost:5000/static/audio/matin_1.mp3"
        )
        db.session.add(inv)
        db.session.commit()

        translations = [
            Translation(invocation_id=inv.id, language_code="fr", text="Louange à Allah qui nous a redonné la vie..."),
            Translation(invocation_id=inv.id, language_code="wo", text="Sama Yàlla mooy fi yégleu...")  # exemple wolof
        ]
        db.session.bulk_save_objects(translations)
        db.session.commit()
