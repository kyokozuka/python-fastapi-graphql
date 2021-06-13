from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session


SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:root@mysql:3306/sample_db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

session = scoped_session(
    sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=engine
    )
)

Base = declarative_base()

Base.query = session.query_property()
