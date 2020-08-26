import sqlalchemy as sa
from sqlalchemy import create_engine
from sqlalchemy.orm import Query, scoped_session, sessionmaker
from sqlalchemy.orm import relationship
from model import Base
from model import Publisher, Book, Shop, Stock, Sale

#################### setup ORM ######################

#DB_PATH = 'postgresql+psycopg2://dz-2-user:P@ssw0rd@http://127.0.0.1:58313/browser/'
DB_PATH = 'postgresql://dz_6_user:NoPas@127.0.0.1:5432/dz_4+pagila'
engine = create_engine(DB_PATH)
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
Session.configure(bind=engine)