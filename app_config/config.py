
class Config(object):
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:copycat@localhost:5432/test_db"   # replace with yours
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = '\xf0?a\x9a\\\xff\xd4;\x0c\xcbHi'
    CSRF_ENABLED = True


