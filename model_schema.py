from models import Song, Podcast, Audiobook, db
from marshmallow import fields, validate
from marshmallow_sqlalchemy import ModelSchema
import datetime

# ModelSchema class makes it possible to return JSON from the Python objects from the SQLAlchemy


class SongSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = Song
        sqla_session = db.session

    id = fields.Number(dump_only=True)
    name_of_song = fields.String(required=True, validate=[validate.Length(max=100)])
    duration = fields.Integer(required=True, validate=[validate.Range(min=0)])
    uploaded_time = fields.DateTime(default=datetime.datetime.utcnow)


class PodcastSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = Podcast
        sqla_session = db.session

    id = fields.Number(dump_only=True)
    name_of_the_podcast = fields.String(required=True,validate=[validate.Length(max=100)])
    duration = fields.Number(required=True, validate=[validate.Range(min=0)])
    uploaded_time = fields.DateTime(required=True, default=datetime.datetime.utcnow)
    host = fields.String(required=True)
    participants = fields.List(fields.String(), required=False, validate=[validate.Length(equal=10)])


class AudiobookSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = Audiobook
        sqla_session = db.session

    id = fields.Number(dump_only=True)
    title_of_the_audiobook = fields.String(required=True, validate=[validate.Length(max=100)])
    author_of_title = fields.String(required=True, validate=[validate.Length(max=100)])
    narrator = fields.String(required=True, validate=[validate.Length(max=100)])
    duration = fields.Integer(required=True, validate=[validate.Range(min=0)])
    uploaded_time = fields.DateTime(required=True, default=datetime.datetime.utcnow)

