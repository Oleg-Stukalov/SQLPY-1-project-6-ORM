
import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

#################### setup ######################
Base = declarative_base()

class Publisher(Base):
    __tablename__ = 'publisher'

    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(50), nullable=False)
    children = relationship('Book', backref='publisher')


class Book(Base):
    __tablename__ = 'book'

    id = sa.Column(sa.Integer, primary_key=True)
    title = sa.Column(sa.String(30), nullable=False)
    id_publisher = sa.Column(sa.Integer, sa.ForeignKey('publisher.id'))
    children = relationship('Stock', backref='book')

class Shop(Base):
    __tablename__ = 'shop'

    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(30), nullable=False)
    children = relationship('Stock', backref='shop')

class Stock(Base):
    __tablename__ = 'stock'

    id = sa.Column(sa.Integer, primary_key=True)
    id_book = sa.Column(sa.Integer, sa.ForeignKey('book.id'))
    id_shop = sa.Column(sa.Integer, sa.ForeignKey('shop.id'))
    count = sa.Column(sa.Integer)
    children = relationship('Sale', backref='stock')


class Sale(Base):
    __tablename__ = 'sale'

    id = sa.Column(sa.Integer, primary_key=True)
    price = sa.Column(sa.Integer, nullable=False)
    date_sale = sa.Column(sa.Date, nullable=False)
    id_stock = sa.Column(sa.Integer, sa.ForeignKey('stock.id'))
    count = sa.Column(sa.Integer)








# if __name__ == '__main__':
#     print('PyCharm')


