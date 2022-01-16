# %%
from sqlalchemy import create_engine, ForeignKey, Column, Integer, String, select
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///container.db", echo=True)
Base = declarative_base()

# Set up functions for recording and printing table data
def result_dict(r):
    return dict(zip(r.keys(), r))


def result_dicts(rs):
    return list(map(result_dict, rs))


class Channel(Base):
    __tablename__ = "channel"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    subscriptions = relationship("Group", secondary="link")


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    containers = relationship(Container, secondary="link")


class Subscription(Base):
    __tablename__ = "subscriptions"
    id = Column(Integer, primary_key=True)
    Container_id = Column(Integer, ForeignKey("container.id", primary_key=True))
    group_id = Column(Integer, ForeignKey("group.id"), primary_key=True)


## Tables are created when following statement is run
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
