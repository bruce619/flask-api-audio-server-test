from flask import request, jsonify, make_response
from schema import SongSchema, PodcastSchema, AudiobookSchema
from routers import Song, Podcast, Audiobook
from enum import Enum


class AudioType(Enum):
    SONG = 'song'
    PODCAST = 'podcast'
    AUDIOBOOK = 'audiobook'


def song_model_data():
    song_data = Song.query.all()
    song_schema = SongSchema(many=True)
    songs = song_schema.dump(song_data)
    return make_response(jsonify({"songs": songs}), 200)


def song_model_data_by_id(audiofileid):
    song_id = Song.query.get(audiofileid)
    if song_id is None:
        return make_response(jsonify({"error": "song id does not exist"}), 404)
    song_schema = SongSchema()
    songs = song_schema.dump(song_id)
    return make_response(jsonify({"songs": songs}), 200)

# =======================================================================================


def podcast_model_data():
    podcast_data = Podcast.query.all()
    podcast_schema = PodcastSchema(many=True)
    podcasts = podcast_schema.dump(podcast_data)
    return make_response(jsonify({"podcasts": podcasts}), 200)


def podcast_model_data_by_id(audiofileid):
    podcast_id = Podcast.query.get(audiofileid)
    if podcast_id is None:
        return make_response(jsonify({"error": "podcast id does not exist"}), 404)
    podcast_schema = PodcastSchema()
    podcasts = podcast_schema.dump(podcast_id)
    return make_response(jsonify({"podcasts": podcasts}), 200)

# =======================================================================================


def audiobook_model_data():
    audiobook_data = Audiobook.query.all()
    audio_schema = AudiobookSchema(many=True)
    audiobooks = audio_schema.dump(audiobook_data)
    return make_response(jsonify({"audiobooks": audiobooks}), 200)


def audiobook_model_data_by_id(audiofileid):
    audiobook_id = Audiobook.query.get(audiofileid)
    if audiobook_id is None:
        return make_response(jsonify({"error": "audiobook id does not exist"}), 404)
    podcast_schema = PodcastSchema()
    audiobooks = podcast_schema.dump(audiobook_id)
    return make_response(jsonify({"audiobooks": audiobooks}), 200)