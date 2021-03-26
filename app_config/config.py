class Config(object):
    SQLALCHEMY_DATABASE_URI = "postgresql://username:password@localhost:5432/test_db"   # replace with yours
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = ''  # replace with secret key
    CSRF_ENABLED = True


