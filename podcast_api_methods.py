from flask import jsonify, make_response
from app_config.app import db
from api_models.schema import PodcastSchema
from api_models.models import Podcast
import datetime


# =========================================================================================
#           GET DATA
# =========================================================================================

# Get audio file type podcast
def get_podcast_data():
    podcast_data = Podcast.query.all()
    podcast_schema = PodcastSchema(many=True)
    podcasts = podcast_schema.dump(podcast_data)
    return make_response(jsonify({"podcasts": podcasts}), 200)


def get_podcast_data_by_id(audioFileId):
    podcast_id = Podcast.query.get(audioFileId)
    if podcast_id is None:
        return make_response(jsonify({"error": "podcast id does not exist"}), 404)
    podcast_schema = PodcastSchema()
    podcasts = podcast_schema.dump(podcast_id)
    return make_response(jsonify({"podcasts": podcasts}), 200)

# =========================================================================================
#           DELETE DATA
# =========================================================================================


# delete audio file type podcast
def delete_podcast_data_by_id(audioFileId):
    podcast_id = Podcast.query.get(audioFileId)
    if podcast_id is None:
        return make_response(jsonify({"error": "podcast id does not exist"}), 404)
    db.session.delete(podcast_id)
    db.session.commit()
    return make_response(jsonify({"message": "podcast file deleted"}), 200)

# =========================================================================================
#           POST DATA
# =========================================================================================


# post audio file type podcast data
def post_podcast_data(data):
    new_podcast = Podcast(name_of_the_podcast=data['audioFileMetaData']['name_of_the_podcast'],
                          duration=data['audioFileMetaData']['duration'],
                          uploaded_time=datetime.datetime.now(), host=data['audioFileMetaData']['host'],
                          participants=data['audioFileMetaData']['participants'])
    podcast_schema = PodcastSchema()
    db.session.add(new_podcast)
    db.session.commit()
    podcast = podcast_schema.dump(new_podcast)
    return make_response(jsonify({'audioFileMetaData': podcast}), 200)

# =========================================================================================
#           PUT DATA
# =========================================================================================


# update audio file type podcast by id
def put_podcast_data(audioFileId, data):
    get_podcast = Podcast.query.get(audioFileId)
    if get_podcast is None:
        return make_response(jsonify({"error": "podcast id does not exist"}), 404)
    get_podcast.name_of_the_podcast = data['audioFileMetaData']['name_of_the_podcast']
    get_podcast.duration = data['audioFileMetaData']['duration']
    get_podcast.host = data['audioFileMetaData']['host']
    get_podcast.participants = data['audioFileMetaData']['participants']
    get_podcast.uploaded_time = datetime.datetime.now()
    db.session.add(get_podcast)
    db.session.commit()
    podcast_schema = PodcastSchema(only=['id', 'name_of_the_podcast', 'duration', 'host', 'participants'])
    podcast = podcast_schema.dump(get_podcast)
    return make_response(jsonify({"audioFileMetaData": podcast}), 200)