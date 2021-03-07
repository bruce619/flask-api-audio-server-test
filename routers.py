from flask import Flask, request, jsonify, make_response
from model_schema import SongSchema, PodcastSchema, AudiobookSchema
from enum import Enum


app = Flask(__name__)

class AudioType(Enum):
    SONG = 'song'
    PODCAST = 'podcast'
    AUDIOBOOK = 'audiobook'

class Audio:
    def __init__(self, audiotype: AudioType):
        self.audiotype =  audiotype

    # validate the audiotype in the AudioType Enum using getters and setters

    # get audiotype
    @property
    def audiotype(self):
        return self._audiotype

    # set audio type
    @audiotype.setter
    def audiotype(self, audiotype: AudioType):
        # raise an exception if the audiotype passed in is not in AudioType Enum
        if audiotype not in AudioType:
            raise ValueError("Audio type invalid " + str(audiotype) + " Audio file type must be: song, podcast, or audiobook")
        self._audiotype = audiotype

    def __repr__(self):
        return f'Audio Type: {self.audiotype}'



if __name__ == '__main__':
    app.run(debug=True)

