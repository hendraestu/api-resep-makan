import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    HOST = "localhost"
    DATABASE = "makanan"
    USERNAME = "root"
    PASSWORD = "hendra24"
    JWT_SECRET_KEY = str(os.environ.get("JWT_SECRET"))
    #SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://'+USERNAME+':'+PASSWORD+'@'+HOST+'/'+DATABASE
    SQLALCHEMY_DATABASE_URI = 'postgresql://kefkkivcpruiwg:7c7ef0366794411547a8a8a4d074d7141459c864bf90bf61f03ffdcf5ea45396@ec2-3-219-131-161.compute-1.amazonaws.com:5432/dbrp2evucrkcao'

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True