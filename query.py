import sqlalchemy as sa
from sqlalchemy import create_engine
from sqlalchemy.orm import Query, scoped_session, sessionmaker
from sqlalchemy.orm import relationship
from model import Base
from model import Publisher, Book, Shop, Stock, Sale

#################### setup ORM ######################

#DB_PATH = 'postgresql+psycopg2://dz-2-user:P@ssw0rd@http://127.0.0.1:58313/browser/'
DB_PATH = 'postgresql+psycopg2://dz-2-user:P@ssw0rd@127.0.0.1:5432/dz_4+pagila'
engine = create_engine(DB_PATH)
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
Session.configure(bind=engine)


if __name__ == '__main__':
    session = Session()

    #запросы
    pub_input = input('Пожалуйста, введите имя издателя для поиска в БД')
    q = session.query(Publisher).filter(Publisher.name == pub_input)
    print('q.all:', q.all())

