from app import db
import datetime


# ===============================================================================
#               Models
# ===============================================================================
class Song(db.Model):
    __tablename__ = 'songs'  # table name will default to name of the model

    # create db columns table
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name_of_song = db.Column(db.String(100), nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    uploaded_time = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow,  onupdate=datetime.datetime.utcnow)

    # define what each instance or row in the DB will have (id is taken care of)
    def __init__(self, name_of_song, duration, uploaded_time):
        self.name_of_song = name_of_song
        self.duration = duration
        self.uploaded_time = datetime.datetime.now()

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
    uploaded_time = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)
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
    uploaded_time = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)

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


# run script once to create db tables
# db.create_all()
