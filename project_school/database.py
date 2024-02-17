from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import engine_from_config
from os import getenv
from dotenv import load_dotenv

load_dotenv(dotenv_path=r'C:\Users\Nurdaulet.DESKTOP-KDILCUN\PycharmProjects\sql\.env')

USERNAME = getenv('USER')
PASSWORD = getenv('PASSWORD')
HOST = getenv('HOST')
PORT = getenv('PORT')
DB_NAME = 'project_school'

db_config = {
    'sqlalchemy.url': f'postgresql+psycopg2://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}'
}

engine = engine_from_config(db_config,
                            # echo=True,
                            client_encoding='utf8')

Session = sessionmaker(bind=engine)

Base = declarative_base()


def get_session():
    session = Session()
    return session
