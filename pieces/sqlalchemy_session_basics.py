from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# sqlite3/mysql/postgres engine
engine = create_engine('mysql://root@localhost/test_tmp', echo=False)

Base = declarative_base()

Session = sessionmaker(bind=engine)

# 创建 session 时，还没有建立连接，不同的 session 对应的不同的连接
# 通过 `show processlist` 命令可以看到
session1 = Session()
session2 = Session()

SessionNoAutoflush = sessionmaker(bind=engine, autoflush=False)
session3 = SessionNoAutoflush()


class User(Base):
    __tablename__  = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(64))


def create_tables():
    Base.metadata.create_all(engine)


def test_autoflush():
    """
    ``理解 autoflush``: 开启了 autoflush 的 session，它 add 一个对象时，
    session 会自动将 sql 语句发送给 MySQL，这时，之后使用这个 session 进行
    查询时，这个对象是可以被查到。

    而没有开启 autoflush 的 session 则不会立即执行对应的 sql 语句，
    需要用户手动 flush。
    """
    session1.add(User(name='wen'))
    session3.add(User(name='wen'))

    assert session1.query(User).filter_by(name='wen').first() is not None
    assert session3.query(User).filter_by(name='wen').first() is None

    session3.flush()
    assert session3.query(User).filter_by(name='wen').first() is not None
