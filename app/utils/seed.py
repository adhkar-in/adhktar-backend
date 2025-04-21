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
            "audio_url": "https://res.cloudinary.com/dbozhll2f/video/upload/v1745242970/matin_1.mp3"
            },
            {
            "title": "Avant de dormir",
            "arabic": "بِاسْمِكَ اللَّهُمَّ أَمُوتُ وَأَحْيَا",
            "phonetic": "Bismika Allahumma amoutu wa ahya ",
            "translation_fr": "C’est en Ton nom, ô Allah, que je meurs et que je vis.",
            "translation_wo": "Ci sa tur laa dee te des, Yàlla.",
            "reference": "Bukhari",
            "benefits": "Met le sommeil sous la protection d’Allah.",
            "category": "Evening",
            "audio_url": "https://res.cloudinary.com/dbozhll2f/video/upload/v1745242970/matin_1.mp3"
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
            "audio_url": "https://res.cloudinary.com/dbozhll2f/video/upload/v1745242970/matin_1.mp3"
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
            "audio_url": "https://res.cloudinary.com/dbozhll2f/video/upload/v1745242970/matin_1.mp3"
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
            "audio_url": "https://res.cloudinary.com/dbozhll2f/video/upload/v1745242970/matin_1.mp3"
            },
            {
            "title": "Avant de manger",
            "arabic": "بِسْمِ اللَّهِ",
            "phonetic": "Bismillah",
            "translation_fr": "Au nom d’Allah.",
            "translation_wo": "Ci turu Yàlla.",
            "reference": "Bukhari",
            "benefits": "Commencer son repas avec le nom d’Allah pour obtenir Sa bénédiction.",
            "category": "Daily",
            "audio_url": "https://res.cloudinary.com/dbozhll2f/video/upload/v1745242970/matin_1.mp3"
            },
            {
            "title": "Après avoir mangé",
            "arabic": "الْـحَمْدُ لِلَّهِ الَّذِي أَطْعَمَنِي هَذَا، وَرَزَقَنِيهِ، مِنْ غَيْرِ حَوْلٍ مِنِّي وَلَا قُوَّةٍ",
            "phonetic": "Alhamdu lillahil-ladhi at’amani hadha wa razaqanihi min ghayri hawlin minni wa la quwwah",
            "translation_fr": "Louange à Allah qui m’a nourri cela et me l’a accordé sans force ni puissance de ma part.",
            "translation_wo": "Yàlla mooy may lekk bii, du manoon ma, moo ko may ci kaw moom.",
            "reference": "Abu Dawud",
            "benefits": "Exprime gratitude et reconnaissance après un repas.",
            "category": "Daily",
            "audio_url": "https://res.cloudinary.com/dbozhll2f/video/upload/v1745242970/matin_1.mp3"
            },
            {
            "title": "Avant d’entrer aux toilettes",
            "arabic": "اللَّهُمَّ إِنِّي أَعُوذُ بِكَ مِنَ الْخُبُثِ وَالْخَبَائِثِ",
            "phonetic": "Allahumma inni a'udhu bika minal-khubthi wal-khaba'ith",
            "translation_fr": "Ô Allah, je cherche protection auprès de Toi contre les démons mâles et femelles.",
            "translation_wo": "Yàlla, maa la nangu fiir ci xel gu bon ak rab yi.",
            "reference": "Bukhari",
            "benefits": "Demande protection contre les impuretés spirituelles.",
            "category": "Daily",
            "audio_url": "https://res.cloudinary.com/dbozhll2f/video/upload/v1745242970/matin_1.mp3"
            },
            {
            "title": "En sortant des toilettes",
            "arabic": "غُفْرَانَكَ",
            "phonetic": "Ghufranak",
            "translation_fr": "Je Te demande pardon.",
            "translation_wo": "Maa la ñaan wér gu yàgg.",
            "reference": "Abu Dawud",
            "benefits": "Exprime humilité et gratitude après avoir accompli un besoin naturel.",
            "category": "Daily",
            "audio_url": "https://res.cloudinary.com/dbozhll2f/video/upload/v1745242970/matin_1.mp3"
            },
            {
            "title": "Quand on entend le tonnerre",
            "arabic": "سُبْحَانَ الَّذِي يُسَبِّحُ الرَّعْدُ بِحَمْدِهِ وَالْمَلَائِكَةُ مِنْ خِيفَتِهِ",
            "phonetic": "Subhana alladhi yusabbihur-ra'du bihamdihi wal-mala’ikatu min khifatih",
            "translation_fr": "Gloire à Celui que le tonnerre loue ainsi que les anges par crainte de Lui.",
            "translation_wo": "Na Yàlla yégluwul boroom kaw ak asamaan yi ci naxari suuf, ak malaika.",
            "reference": "Muwatta Malik",
            "benefits": "Renforce la conscience de la grandeur d’Allah face à la nature.",
            "category": "Daily",
            "audio_url": "https://res.cloudinary.com/dbozhll2f/video/upload/v1745242970/matin_1.mp3"
            },
            {
            "title": "En entrant à la mosquée",
            "arabic": "اللَّهُمَّ افْتَحْ لِي أَبْوَابَ رَحْمَتِكَ",
            "phonetic": "Allahumma iftah li abwaba rahmatik",
            "translation_fr": "Ô Allah, ouvre-moi les portes de Ta miséricorde.",
            "translation_wo": "Yàlla, ubbi ma bunt yërmande ya.",
            "reference": "Muslim",
            "benefits": "Invoque la miséricorde divine à l’entrée dans un lieu sacré.",
            "category": "Home",
            "audio_url": "https://res.cloudinary.com/dbozhll2f/video/upload/v1745242970/matin_1.mp3"
            },
            {
            "title": "En sortant de la mosquée",
            "arabic": "اللَّهُمَّ إِنِّي أَسْأَلُكَ مِنْ فَضْلِكَ",
            "phonetic": "Allahumma inni as’aluka min fadlik",
            "translation_fr": "Ô Allah, je Te demande de Ta grâce.",
            "translation_wo": "Yàlla, maa la ñaan sa niroo.",
            "reference": "Muslim",
            "benefits": "Demande bénédiction après un acte d’adoration.",
            "category": "Home",
            "audio_url": "https://res.cloudinary.com/dbozhll2f/video/upload/v1745242970/matin_1.mp3"
            },
            {
            "title": "Lorsque l’on voit une personne malade",
            "arabic": "لَا بَأْسَ طَهُورٌ إِنْ شَاءَ اللَّهُ",
            "phonetic": "La ba’sa, tahoorun in sha Allah",
            "translation_fr": "Pas de mal, purification si Allah le veut.",
            "translation_wo": "Duñu am lu bon, bu Yàlla ko bëgg baax na.",
            "reference": "Bukhari",
            "benefits": "Remonte le moral du malade tout en se rappelant la sagesse divine.",
            "category": "Daily",
            "audio_url": "https://res.cloudinary.com/dbozhll2f/video/upload/v1745242970/matin_1.mp3"
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
