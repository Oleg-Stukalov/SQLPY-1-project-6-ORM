import sqlalchemy as sa
from sqlalchemy.orm import Query, scoped_session, sessionmaker
import datetime

#################### setup some data ######################
pub1 = sa.Publisher(
    name = 'МИФ'
)
sa.session.add(pub1)
sa.session.commit()


book1 = sa.Book(
    title = '45 татуировок менеджера',
    id_publisher = 0
)
sa.session.add(book1)
sa.session.commit()

sh1 = sa.Shop(
    name = 'Буквоед-1'
)
sa.session.add(sh1)
sa.session.commit()

st1 = sa.Stock(
    id_book = 0,
    id_shop = 0,
    count = 100
    )
sa.session.add(st1)
sa.session.commit()

sale1 = sa.Sale(
    price = 570,
    date_sale = datetime.today(),
    id_stock = 0,
    count = 84
    )
sa.session.add(sale1)
sa.session.commit()

