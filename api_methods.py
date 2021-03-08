from flask import jsonify, make_response
from schema import SongSchema, PodcastSchema, AudiobookSchema
from routers import Song, Podcast, Audiobook, db
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

# Get audio file type audiobook
def get_audiobook_data():
    audiobook_data = Audiobook.query.all()
    audio_schema = AudiobookSchema(many=True)
    audiobooks = audio_schema.dump(audiobook_data)
    return make_response(jsonify({"audiobooks": audiobooks}), 200)


# Get audio file type audiobook by id
def get_audiobook_data_by_id(audioFileId):
    audiobook_id = Audiobook.query.get(audioFileId)
    if audiobook_id is None:
        return make_response(jsonify({"error": "audiobook id does not exist"}), 404)
    audiobook_schema = AudiobookSchema()
    audiobooks = audiobook_schema.dump(audiobook_id)
    return make_response(jsonify({"audiobooks": audiobooks}), 200)


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


# delete audio file type podcast
def delete_podcast_data_by_id(audioFileId):
    podcast_id = Podcast.query.get(audioFileId)
    if podcast_id is None:
        return make_response(jsonify({"error": "podcast id does not exist"}), 404)
    db.session.delete(podcast_id)
    db.session.commit()
    return make_response(jsonify({"message": "song file deleted"}), 200)


# delete audio file type audiobook
def delete_audiobook_data_by_id(audioFileId):
    audiobook_id = Audiobook.query.get(audioFileId)
    if audiobook_id is None:
        return make_response(jsonify({"error": "audiobook id does not exist"}), 404)
    db.session.delete(audioFileId)
    db.session.commit()
    return make_response(jsonify({"message": "audiobook file deleted"}), 200)

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


# post audio file type podcast data
def post_podcast_data(data):
    new_podcast = Podcast(name_of_the_podcast=data['audioFileMetaData']['name_of_the_podcast'], duration=data['audioFileMetaData']['duration'],
                          uploaded_time=datetime.datetime.now(), host=data["host"], participants=data['participants'])
    podcast_schema = PodcastSchema()
    db.session.add(new_podcast)
    db.session.commit()
    podcast = podcast_schema.dump(new_podcast)
    return make_response(jsonify({'audioFileMetaData': podcast}), 200)


# post audio file type audiobook
def post_audiobook_data(data):
    new_audiobook = Audiobook(title_of_the_audiobook=data['audioFileMetaData']['title_of_the_audiobook'],
                              author_of_title=data['audioFileMetaData']['author_of_title'],
                              narrator=data['audioFileMetaData']['narrator'], duration=data['audioFileMetaData']['duration'],
                              uploaded_time=datetime.datetime.now())
    podcast_schema = PodcastSchema()
    db.session.add(new_audiobook)
    db.session.commit()
    audiobook = podcast_schema.dump(new_audiobook)
    return make_response(jsonify({'audioFileMetaData': audiobook}), 200)

# =========================================================================================
#           PUT DATA
# =========================================================================================


# update audio file type song by id
def put_song_data(audioFileId, data):
    get_song = Song.query.get(audioFileId)
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
    return make_response(jsonify({"audioFileMetaData": song}), 200)


# update audio file type podcast by id
def put_podcast_data(audioFileId, data):
    get_podcast = Podcast.query.get(audioFileId)
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
    return make_response(jsonify({"audioFileMetaData": podcast}), 200)


# update audio file type podcast by id
def put_audiobook_data(audioFileId, data):
    get_audiobook = Audiobook.query.get(audioFileId)
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
    return make_response(jsonify({"audioFileMetaData": audio_book}), 200)


