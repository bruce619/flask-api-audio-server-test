from flask import request, jsonify, make_response
from schema import SongSchema, PodcastSchema, AudiobookSchema
from routers import Song, Podcast, Audiobook, db
from enum import Enum


# enum class that maps to model/db class
class AudioType(Enum):
    SONG = 'song'
    PODCAST = 'podcast'
    AUDIOBOOK = 'audiobook'

# =========================================================================================
#           GET DATA
# =========================================================================================


# Get audio file type song
def get_song_data():
    song_data = Song.query.all()
    song_schema = SongSchema(many=True)
    songs = song_schema.dump(song_data)
    return make_response(jsonify({"songs": songs}), 200)


def get_song_data_by_id(audiofileid):
    song_id = Song.query.get(audiofileid)
    if song_id is None:
        return make_response(jsonify({"error": "song id does not exist"}), 404)
    song_schema = SongSchema()
    songs = song_schema.dump(song_id)
    return make_response(jsonify({"songs": songs}), 200)


# Get audio file type podcast

def get_podcast_data():
    podcast_data = Podcast.query.all()
    podcast_schema = PodcastSchema(many=True)
    podcasts = podcast_schema.dump(podcast_data)
    return make_response(jsonify({"podcasts": podcasts}), 200)


def get_podcast_data_by_id(audiofileid):
    podcast_id = Podcast.query.get(audiofileid)
    if podcast_id is None:
        return make_response(jsonify({"error": "podcast id does not exist"}), 404)
    podcast_schema = PodcastSchema()
    podcasts = podcast_schema.dump(podcast_id)
    return make_response(jsonify({"podcasts": podcasts}), 200)


# Get audio file type audiobook

def get_audiobook_data():
    audiobook_data = Audiobook.query.all()
    audio_schema = AudiobookSchema(many=True)
    audiobooks = audio_schema.dump(audiobook_data)
    return make_response(jsonify({"audiobooks": audiobooks}), 200)


def get_audiobook_data_by_id(audiofileid):
    audiobook_id = Audiobook.query.get(audiofileid)
    if audiobook_id is None:
        return make_response(jsonify({"error": "audiobook id does not exist"}), 404)
    podcast_schema = PodcastSchema()
    audiobooks = podcast_schema.dump(audiobook_id)
    return make_response(jsonify({"audiobooks": audiobooks}), 200)

# =========================================================================================
#           DELETE DATA
# =========================================================================================


# delete audio file type song
def delete_song_data_by_id(audiofileid):
    song_id = Song.query.get(audiofileid)
    if song_id is None:
        return make_response(jsonify({"error": "song id does not exist"}), 404)
    db.session.delete(song_id)
    db.session.commit()
    return make_response(jsonify({"message": "song file deleted"}), 200)


# delete audio file type podcast
def delete_podcast_data_by_id(audiofileid):
    podcast_id = Podcast.query.get(audiofileid)
    if podcast_id is None:
        return make_response(jsonify({"error": "podcast id does not exist"}), 404)
    db.session.delete(podcast_id)
    db.session.commit()
    return make_response(jsonify({"message": "song file deleted"}), 200)


# delete audio file type audiobook
def delete_audiobook_data_by_id(audiofileid):
    audiobook_id = Audiobook.query.get(audiofileid)
    if audiobook_id is None:
        return make_response(jsonify({"error": "audiobook id does not exist"}), 404)
    db.session.delete(audiofileid)
    db.session.commit()
    return make_response(jsonify({"message": "audiobook file deleted"}), 200)


# =========================================================================================
#           POST DATA
# =========================================================================================

# post audio file type song data
def post_song_data():
    data = request.get_json()
    song_schema = SongSchema()
    song = song_schema.load(data)
    result = song_schema.dump(song.create())
    return make_response(jsonify({"song": result}), 200)


# post audio file type podcast data
def post_podcast_data():
    data = request.get_json()
    podcast_schema = PodcastSchema()
    podcast = podcast_schema.load(data)
    result = podcast_schema.dump(podcast.create())
    return make_response(jsonify({"podcast": result}), 200)


# post audio file type audiobook
def post_audiobook_data():
    data = request.get_json()
    audiobook_schema = AudiobookSchema()
    audiobook = audiobook_schema.load(data)
    result = audiobook_schema.dump(audiobook.create())
    return make_response(jsonify({"audiobook": result}), 200)


# =========================================================================================
#           PUT DATA
# =========================================================================================

# update audio file type song by id
def put_song_data(audiofileid):
    data = request.get_json()
    get_song = Song.query.get(audiofileid)
    if get_song is None:
        return make_response(jsonify({"error": "song id does not exist"}), 404)
    if data.get('name_of_song'):
        get_song.name_of_song = data['name_of_song']
    if data.get('duration'):
        get_song.duration = data['duration']
    db.session.add(get_song)
    db.session.commit()
    song_schema = SongSchema(only=['id', 'name_of_song', 'duration'])
    song = song_schema.dump(get_song)
    return make_response(jsonify({"song": song}), 200)


# update audio file type podcast by id
def put_podcast_data(audiofileid):
    data = request.get_json()
    get_podcast = Podcast.query.get(audiofileid)
    if get_podcast is None:
        return make_response(jsonify({"error": "podcast id does not exist"}), 404)
    if data.get('name_of_the_podcast'):
        get_podcast.name_of_the_podcast = data['name_of_the_podcast']
    if data.get('duration'):
        get_podcast.duration = data['duration']
    if data.get('host'):
        get_podcast.host = data['host']
    if data.get('participants'):
        get_podcast.participants = data['participants']
    db.session.add(get_podcast)
    db.session.commit()
    podcast_schema = PodcastSchema(only=['id', 'name_of_the_podcast', 'duration', 'host', 'participants'])
    podcast = podcast_schema.dump(get_podcast)
    return make_response(jsonify({"podcast": podcast}), 200)


# update audio file type podcast by id
def put_audiobook_data(audiofileid):
    data = request.get_json()
    get_audiobook = Audiobook.query.get(audiofileid)
    if get_audiobook is None:
        return make_response(jsonify({"error": "audiobook id does not exist"}), 404)
    if data.get('title_of_the_audiobook'):
        get_audiobook.title_of_the_audiobook = data['title_of_the_audiobook']
    if data.get('author_of_title'):
        get_audiobook.author_of_title = data['author_of_title']
    if data.get('narrator'):
        get_audiobook.narrator = data["narrator"]
    if data.get('duration'):
        get_audiobook.duration = data['duration']
    db.session.add(get_audiobook)
    db.session.commit()
    audio_book_schema = AudiobookSchema(only=['id', 'title_of_the_audiobook', 'author_of_title', 'narrator', 'duration'])
    audio_book = audio_book_schema.dump(get_audiobook)
    return make_response(jsonify({"audiobook": audio_book}), 200)


