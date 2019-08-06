import os

class Config:
    """Main configurations class"""


    # SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://njoroge:njoro1234@localhost/njoroge'
    # DATABASE_URL = 'mysql+mysqldb://njoroge:1234@localhost/njoroge.mysql'
    SECRET_KEY = os.environ.get("SECRET_KEY")
    UPLOADED_PHOTOS_DEST = 'app/static/photos'
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")   



# PGUSER=njoroge PGPASSWORD=njoro1234 heroku pg:push pitches HEROKU_POSTGRESQL_YELLOW -minutespitch

class ProdConfig(Config): 
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")


class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://njoroge:njoro1234@localhost/njoroge'
    DEBUG = True


config_options = {
    'development': DevConfig,
    'production': ProdConfig
}
