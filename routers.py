from flask import Flask
from api_methods import *
from flask_sqlalchemy import SQLAlchemy
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:copycat@localhost:5432/test_db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Song(db.Model):
    __tablename__ = 'songs'  # table name will default to name of the model

    # create db columns table
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name_of_song = db.Column(db.String(100), nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    uploaded_time = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)

    # define what each instance or row in the DB will have (id is taken care of)
    def __init__(self, name_of_song, duration, uploaded_time):
        self.name_of_song = name_of_song
        self.duration = duration
        self.uploaded_time = uploaded_time

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
        return self

    def __repr__(self):
        return f'{self.name_of_song} ({self.duration}) uploaded at {self.uploaded_time}'


class Podcast(db.Model):
    __tablename__ = 'podcasts'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name_of_the_podcast = db.Column(db.String(100), nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    uploaded_time = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)
    host = db.Column(db.String(100), nullable=False)
    participants = db.Column(db.ARRAY(db.String(100)), nullable=True)

    def __init__(self, name_of_the_podcast, duration, uploaded_time, host, participants):
        self.name_of_the_podcast = name_of_the_podcast
        self.duration = duration
        self.uploaded_time = uploaded_time
        self.host = host
        self.participants = participants

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
        return self

    def __repr__(self):
        return f'{self.name_of_the_podcast} ({self.duration}) uploaded at {self.uploaded_time}'


class Audiobook(db.Model):
    __tablename__ = 'audiobooks'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title_of_the_audiobook = db.Column(db.String(100), nullable=False)
    author_of_title = db.Column(db.String(100), nullable=False)
    narrator = db.Column(db.String(100), nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    uploaded_time = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)

    def __init__(self, title_of_the_audiobook, author_of_title, narrator, duration, uploaded_time):
        self.title_of_the_audiobook = title_of_the_audiobook
        self.author_of_title = author_of_title
        self.narrator = narrator
        self.duration = duration
        self.uploaded_time = uploaded_time

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
        return self

    def __repr__(self):
        return f'{self.title_of_the_audiobook} ({self.duration}) by {self.author_of_title} uploaded at {self.uploaded_time}'


@app.route('/<audiofiletype>/', methods=['GET'])
def get_all_data(audiofiletype):
    if audiofiletype.lower() == AudioType.SONG.value:
        return song_model_data()
    elif audiofiletype.lower() == AudioType.PODCAST.value:
        return podcast_model_data()
    elif audiofiletype.lower() == AudioType.AUDIOBOOK.value:
        return audiobook_model_data()
    else:
        return make_response(jsonify({"error": "audio file type invalid"}), 500)


@app.route('/<audiofiletype>/<audiofileid>/', methods=['GET'])
def get_audio_data(audiofiletype, audiofileid):
    if audiofiletype.lower() == AudioType.SONG.value:
        return song_model_data_by_id(audiofileid)
    elif audiofiletype.lower() == AudioType.PODCAST.value:
        return podcast_model_data_by_id(audiofileid)
    elif audiofiletype.lower() == AudioType.AUDIOBOOK.value:
        return audiobook_model_data_by_id(audiofileid)
    else:
        # raise TypeError("invalid Type " + str(audiofiletype) + " must be of AudioType: song, podcast, or audiobook")
        return make_response(jsonify({"error": "audio file type invalid"}), 500)


if __name__ == '__main__':
    app.run(debug=True)

