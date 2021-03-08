from flask import jsonify, make_response
from app_config.app import db
from api_models.schema import SongSchema
from api_models.models import Song
import datetime


# =========================================================================================
#           GET DATA
# =========================================================================================


# Get audio file type song
def get_song_data():
    song_data = Song.query.all()
    song_schema = SongSchema(many=True)
    songs = song_schema.dump(song_data)
    return make_response(jsonify({"songs": songs}), 200)


# get audio file type song by id
def get_song_data_by_id(audioFileId):
    song_id = Song.query.get(audioFileId)
    if song_id is None:
        return make_response(jsonify({"error": "song id does not exist"}), 404)
    song_schema = SongSchema()
    songs = song_schema.dump(song_id)
    return make_response(jsonify({"songs": songs}), 200)

# =========================================================================================
#           DELETE DATA
# =========================================================================================


# delete audio file type song
def delete_song_data_by_id(audioFileId):
    song_id = Song.query.get(audioFileId)
    if song_id is None:
        return make_response(jsonify({"error": "song id does not exist"}), 404)
    db.session.delete(song_id)
    db.session.commit()
    return make_response(jsonify({"message": "song file deleted"}), 200)


# =========================================================================================
#           POST DATA
# =========================================================================================


# # post audio file type song data
def post_song_data(data):
    new_song = Song(name_of_song=data['audioFileMetaData']['name_of_song'], duration=data['audioFileMetaData']['duration'], uploaded_time=datetime.datetime.now())
    song_schema = SongSchema()
    db.session.add(new_song)
    db.session.commit()
    song = song_schema.dump(new_song)
    return make_response(jsonify({'audioFileMetaData': song}), 200)


# =========================================================================================
#           PUT DATA
# =========================================================================================


# update audio file type song by id
def put_song_data(audioFileId, data):
    get_song = Song.query.get(audioFileId)
    if get_song is None:
        return make_response(jsonify({"error": "song id does not exist"}), 404)
    get_song.name_of_song = data['audioFileMetaData']['name_of_song']
    get_song.duration = data['audioFileMetaData']['duration']
    get_song.uploaded_time = datetime.datetime.now()
    db.session.add(get_song)
    db.session.commit()
    song_schema = SongSchema(only=['id', 'name_of_song', 'duration'])
    song = song_schema.dump(get_song)
    return make_response(jsonify({"audioFileMetaData": song}), 200)


