from flask import jsonify, make_response
from app import db
from schema import AudiobookSchema
from models import Audiobook
import datetime

# =========================================================================================
#           GET DATA
# =========================================================================================


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


# post audio file type audiobook
def post_audiobook_data(data):
    new_audiobook = Audiobook(title_of_the_audiobook=data['audioFileMetaData']['title_of_the_audiobook'],
                              author_of_title=data['audioFileMetaData']['author_of_title'],
                              narrator=data['audioFileMetaData']['narrator'], duration=data['audioFileMetaData']['duration'],
                              uploaded_time=datetime.datetime.now())
    audio_schema = AudiobookSchema()
    db.session.add(new_audiobook)
    db.session.commit()
    audiobook = audio_schema.dump(new_audiobook)
    return make_response(jsonify({'audioFileMetaData': audiobook}), 200)

# =========================================================================================
#           PUT DATA
# =========================================================================================


# update audio file type podcast by id
def put_audiobook_data(audioFileId, data):
    get_audiobook = Audiobook.query.get(audioFileId)
    if get_audiobook is None:
        return make_response(jsonify({"error": "audiobook id does not exist"}), 404)
    get_audiobook.title_of_the_audiobook = data['audioFileMetaData']['title_of_the_audiobook']
    get_audiobook.author_of_title = data['audioFileMetaData']['author_of_title']
    get_audiobook.narrator = data['audioFileMetaData']["narrator"]
    get_audiobook.duration = data['audioFileMetaData']['duration']
    get_audiobook.uploaded_time = datetime.datetime.now()
    db.session.add(get_audiobook)
    db.session.commit()
    audio_book_schema = AudiobookSchema(only=['id', 'title_of_the_audiobook', 'author_of_title', 'narrator', 'duration'])
    audio_book = audio_book_schema.dump(get_audiobook)
    return make_response(jsonify({"audioFileMetaData": audio_book}), 200)
