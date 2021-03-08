from app_config.app import app
from song_api_methods import get_song_data, get_song_data_by_id, delete_song_data_by_id, post_song_data, put_song_data
from podcast_api_methods import get_podcast_data, get_podcast_data_by_id, delete_podcast_data_by_id, post_podcast_data, put_podcast_data
from audiobook_api_methods import get_audiobook_data, get_audiobook_data_by_id, delete_audiobook_data_by_id, post_audiobook_data, put_audiobook_data
from enum_class import AudioType
from flask import request
from flask import jsonify, make_response


# ===============================================================================
#               API ROUTES
# ===============================================================================
@app.route('/<audioFileType>', methods=['GET'])
def get_all_audio_data(audioFileType):
    if audioFileType.lower() == AudioType.SONG.value:
        return get_song_data()
    elif audioFileType.lower() == AudioType.PODCAST.value:
        return get_podcast_data()
    elif audioFileType.lower() == AudioType.AUDIOBOOK.value:
        return get_audiobook_data()
    else:
        return make_response(jsonify({"error": "audio file type invalid"}), 500)


@app.route('/<audioFileType>/<audioFileId>', methods=['GET'])
def get_audio_data_by_id(audioFileType, audioFileId):
    if audioFileType.lower() == AudioType.SONG.value:
        return get_song_data_by_id(audioFileId)
    elif audioFileType.lower() == AudioType.PODCAST.value:
        return get_podcast_data_by_id(audioFileId)
    elif audioFileType.lower() == AudioType.AUDIOBOOK.value:
        return get_audiobook_data_by_id(audioFileId)
    else:
        return make_response(jsonify({"error": "audio file type invalid"}), 500)


@app.route('/<audioFileType>/<audioFileId>', methods=['DELETE'])
def delete_audio_data(audioFileType, audioFileId):
    if audioFileType.lower() == AudioType.SONG.value:
        return delete_song_data_by_id(audioFileId)
    elif audioFileType.lower() == AudioType.PODCAST.value:
        return delete_podcast_data_by_id(audioFileId)
    elif audioFileType.lower() == AudioType.AUDIOBOOK.value:
        return delete_audiobook_data_by_id(audioFileId)
    else:
        return make_response(jsonify({"error": "audio file type invalid"}), 500)


@app.route('/', methods=['POST'])
def post_audio_data():
    data = request.get_json()
    if not data:
        return make_response(jsonify({"message": "No input data provided"}), 400)
    if data['audioFileType'] == AudioType.SONG.value:
        return post_song_data(data)
    elif data['audioFileType'] == AudioType.PODCAST.value:
        return post_podcast_data(data)
    elif data['audioFileType'] == AudioType.AUDIOBOOK.value:
        return post_audiobook_data(data)
    return make_response(jsonify({"error": "audio file type invalid"}), 500)


@app.route('/<audioFileType>/<audioFileId>', methods=['PUT'])
def update_audio_data(audioFileType, audioFileId):
    data = request.get_json()
    if audioFileType.lower() == AudioType.SONG.value:
        return put_song_data(audioFileId, data)
    elif audioFileType.lower() == AudioType.PODCAST.value:
        return put_podcast_data(audioFileId, data)
    elif audioFileType.lower() == AudioType.AUDIOBOOK.value:
        return put_audiobook_data(audioFileId, data)
    else:
        return make_response(jsonify({"error": "audio file type invalid"}), 500)


if __name__ == '__main__':
    app.run(debug=True)

# in the project directory, run python api.py in terminal/cmd




