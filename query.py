from model import Base
from model import Publisher, Book, Shop, Stock, Sale
from engine_session import engine, Session



#starter
if __name__ == '__main__':
    session = Session()

    #запросы
    pub_input = input('Пожалуйста, введите имя издателя для поиска в БД: ')
    q = session.query(Publisher).filter(Publisher.name == pub_input)
    print('q.all:', q.all())

