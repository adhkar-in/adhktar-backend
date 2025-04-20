from app import db
from app.models import Invocation, Translation

def seed_data():
    if Invocation.query.count() == 0:
        invocations_data = [
            {
                "title": "Après le réveil",
                "arabic": "الحَمْدُ للهِ الَّذِي أَحْيَانَا بَعْدَ مَا أَمَاتَنَا، وَإِلَيْهِ النُّشُورُ",
                "phonetic": "Alhamdu lillahil-ladhi ahyana ba'da ma amatana wa ilayhin-nushoor",
                "translation_fr": "Louange à Allah qui nous a redonné la vie après nous avoir fait mourir, et c’est vers Lui que se fera la résurrection.",
                "translation_wo": "Sama Yàlla mooy fi yégle nanu ba mu ko defa dee, te moom la nuy dellu.",
                "reference": "Bukhari",
                "benefits": "Exprime la gratitude envers Allah pour une nouvelle journée.",
                "category": "Morning",
                "audio_url": "http://localhost:5000/static/audio/morning_1.mp3"
            },
            {
                "title": "Avant de dormir",
                "arabic": "بِاسْمِكَ اللَّهُمَّ أَمُوتُ وَأَحْيَا",
                "phonetic": "Bismika Allahumma amoutu wa ahya",
                "translation_fr": "C’est en Ton nom, ô Allah, que je meurs et que je vis.",
                "translation_wo": "Ci sa tur laa dee te des, Yàlla.",
                "reference": "Bukhari",
                "benefits": "Met le sommeil sous la protection d’Allah.",
                "category": "Evening",
                "audio_url": "http://localhost:5000/static/audio/evening_1.mp3"
            },
            {
                "title": "En entrant dans la maison",
                "arabic": "اللَّهُمَّ إِنِّي أَسْأَلُكَ خَيْرَ الْمَوْلَجِ وَخَيْرَ الْمَخْرَجِ",
                "phonetic": "Allahumma inni as’aluka khayral-mawlaji wa khayral-makhraji",
                "translation_fr": "Ô Allah, je Te demande le meilleur de l’entrée et le meilleur de la sortie.",
                "translation_wo": "Yàlla, maa la ñaan bu baax ci dugg ak ci génn.",
                "reference": "Abu Dawud",
                "benefits": "Demande bénédiction et sécurité au foyer.",
                "category": "Home",
                "audio_url": "http://localhost:5000/static/audio/home_1.mp3"
            },
            {
                "title": "Sortie de la maison",
                "arabic": "بِسْمِ اللَّهِ، تَوَكَّلْتُ عَلَى اللَّهِ، وَلَا حَوْلَ وَلَا قُوَّةَ إِلَّا بِاللَّهِ",
                "phonetic": "Bismillah, tawakkaltu ‘ala Allah, wa la hawla wa la quwwata illa billah",
                "translation_fr": "Au nom d’Allah, je place ma confiance en Allah, et il n’y a de force et de puissance qu’en Allah.",
                "translation_wo": "Ci turu Yàlla, maa koy jéem, duñu am dërëm ndax moom rekk la fi am.",
                "reference": "Tirmidhi",
                "benefits": "Assure la protection divine à l’extérieur.",
                "category": "Daily",
                "audio_url": "http://localhost:5000/static/audio/daily_1.mp3"
            },
            {
                "title": "Dou'a du voyage",
                "arabic": "سُبْحَانَ الَّذِي سَخَّرَ لَنَا هَذَا وَمَا كُنَّا لَهُ مُقْرِنِينَ",
                "phonetic": "Subhana alladhi sakhkhara lana hadha wa ma kunna lahu muqrinin",
                "translation_fr": "Gloire à Celui qui nous a soumis ceci alors que nous n’étions pas capables par nous-mêmes.",
                "translation_wo": "Yàlla moo nu jox lii, du ñu ko manoon.",
                "reference": "Muslim",
                "benefits": "Protection et rappel de la dépendance envers Allah pendant le voyage.",
                "category": "Travel",
                "audio_url": "http://localhost:5000/static/audio/travel_1.mp3"
            }
        ]

        for data in invocations_data:
            inv = Invocation(
                title=data["title"],
                arabic=data["arabic"],
                phonetic=data["phonetic"],
                reference=data["reference"],
                benefits=data["benefits"],
                category=data["category"],
                audio_url=data["audio_url"]
            )
            db.session.add(inv)
            db.session.commit()

            translations = [
                Translation(invocation_id=inv.id, language_code="fr", text=data["translation_fr"]),
                Translation(invocation_id=inv.id, language_code="wo", text=data["translation_wo"])
            ]
            db.session.bulk_save_objects(translations)
            db.session.commit()
