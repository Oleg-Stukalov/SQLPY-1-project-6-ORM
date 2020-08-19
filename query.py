import sqlalchemy as sa
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Query, scoped_session, sessionmaker

#################### setup ORM ######################
Base = declarative_base()

engine = create_engine('postgresql+psycopg2://dz-2-user:P@ssw0rd@http://127.0.0.1:58313/browser/')
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)


#запросы
pub_input = input('Пожалуйста, введите имя издателя для поиска в БД')
q = sa.session.query(publisher).filter(publisher.name == pub_input)
