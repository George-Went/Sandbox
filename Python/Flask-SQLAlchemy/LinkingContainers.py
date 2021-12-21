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


class Container(Base):
    __tablename__ = "container"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    groups = relationship("Group", secondary="link")


class Group(Base):
    __tablename__ = "group"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    containers = relationship(Container, secondary="link")


class Link(Base):
    __tablename__ = "link"
    id = Column(Integer, primary_key=True)
    Container_id = Column(Integer, ForeignKey("container.id", primary_key=True))
    group_id = Column(Integer, ForeignKey("group.id"), primary_key=True)


## Tables are created when following statement is run
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# %%


## Creating objectcs for both tables
c1 = Container(name="Flask")
c2 = Container(name="Database")
c3 = Container(name="Vue")

g1 = Group(name="FullStack")
g2 = Group(name="Database")

## Add Group 1 Containers

g1.containers.append(c1)
g1.containers.append(c2)
g1.containers.append(c3)

## Add group 2 container
g2.containers.append(c2)

## Add Container 1 groups
c1.groups.append(g1)

## Add Container 2 groups
c2.groups.append(g1)
c2.groups.append(g2)

## Add Container 3 groups
c3.groups.append(g1)


# added containers to the engine 'session'
session.add(c1)
session.add(c2)
session.add(c3)
# added groups to the engine 'session'
session.add(g1)
session.add(g2)

# Commit the session to the database
# Will exeute the above statements
session.commit()


# %%
stmt = select("*").select_from(Link)
result = session.execute(stmt).fetchall()
result_dicts(result)

# %%
stmt = select("*").select_from(Container)
result = session.execute(stmt).fetchall()
result_dicts(result)

# %%
print(engine.table_names())

# %%
