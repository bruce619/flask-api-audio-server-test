from enum import Enum


# enum class that maps to model/db class
class AudioType(Enum):
    SONG = 'song'
    PODCAST = 'podcast'
    AUDIOBOOK = 'audiobook'
