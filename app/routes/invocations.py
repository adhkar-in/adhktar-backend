from flask import Blueprint, jsonify, request
from app.models import Invocation
from app import db
from flasgger.utils import swag_from

invocations_bp = Blueprint("invocations", __name__)

@invocations_bp.route("/", methods=["GET"])
@swag_from({
    'responses': {
        200: {
            'description': 'List of invocations',
            'examples': {
                'application/json': [{"id": 1, "title": "Wake Up", "arabic": "..."}]
            }
        }
    }
})
def get_invocations():
    category = request.args.get("category")
    query = request.args.get("query")
    lang = request.args.get("lang", "fr")

    invocations_query = Invocation.query

    if category:
        invocations_query = invocations_query.filter_by(category=category)
    if query:
        invocations_query = invocations_query.filter(Invocation.title.contains(query))

    invocations = invocations_query.all()
    return jsonify([{
        "id": i.id,
        "title": i.title,
        "arabic": i.arabic,
        "phonetic": i.phonetic,
        "translation": next((t.text for t in i.translations if t.language_code == lang), None),
        "reference": i.reference,
        "benefits": i.benefits,
        "category": i.category,
        "audio_url": i.audio_url
    } for i in invocations])

@invocations_bp.route("/<int:invocation_id>", methods=["GET"])
def get_invocation(invocation_id):
    lang = request.args.get("lang", "fr")
    invocation = Invocation.query.get_or_404(invocation_id)
    translation = next((t.text for t in invocation.translations if t.language_code == lang), None)
    
    return jsonify({
        "id": invocation.id,
        "title": invocation.title,
        "arabic": invocation.arabic,
        "phonetic": invocation.phonetic,
        "translation": translation,
        "reference": invocation.reference,
        "benefits": invocation.benefits,
        "category": invocation.category,
        "audio_url": invocation.audio_url
    })