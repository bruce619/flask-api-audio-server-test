from routers import Song, Podcast, Audiobook, db
from marshmallow import fields, ValidationError
from marshmallow_sqlalchemy import ModelSchema
import datetime

# ModelSchema class makes it possible to return JSON from the Python objects from the SQLAlchemy


# custom validation
def string_must_not_be_greater_than_100_characters(data):
    if len(data) > 100:
        raise ValidationError("Character must not be greater than 100")


def number_must_be_positive(data):
    if data < 0:
        raise ValidationError("second must be positive")


def must_not_be_more_than_10_participants(data):
    if len(data) > 10:
        raise ValidationError("participants must not be more than 10")


class SongSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = Song
        sqla_session = db.session

    id = fields.Number(dump_only=True)
    name_of_song = fields.String(required=True, validate=string_must_not_be_greater_than_100_characters)
    duration = fields.Integer(required=True, validate=number_must_be_positive)
    uploaded_time = fields.DateTime(default=datetime.datetime.utcnow)


class PodcastSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = Podcast
        sqla_session = db.session

    id = fields.Number(dump_only=True)
    name_of_the_podcast = fields.String(required=True, validate=string_must_not_be_greater_than_100_characters)
    duration = fields.Number(required=True, validate=number_must_be_positive)
    uploaded_time = fields.DateTime(required=True, default=datetime.datetime.utcnow)
    host = fields.String(required=True, validate=string_must_not_be_greater_than_100_characters)
    participants = fields.List(fields.String(validate=must_not_be_more_than_10_participants), required=False, validate=must_not_be_more_than_10_participants)


class AudiobookSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = Audiobook
        sqla_session = db.session

    id = fields.Number(dump_only=True)
    title_of_the_audiobook = fields.String(required=True, validate=string_must_not_be_greater_than_100_characters)
    author_of_title = fields.String(required=True, validate=must_not_be_more_than_10_participants)
    narrator = fields.String(required=True, validate=string_must_not_be_greater_than_100_characters)
    duration = fields.Integer(required=True, validate=number_must_be_positive)
    uploaded_time = fields.DateTime(required=True, default=datetime.datetime.utcnow)

