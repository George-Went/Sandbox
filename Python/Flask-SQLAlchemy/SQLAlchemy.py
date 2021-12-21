## This is just sql alchemy examples

# %%
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy import create_engine
# from app.models import *  # Imports sqlalchemy schemas
# from app import db
from sqlalchemy import select
from sqlalchemy import Column, Integer, Text, MetaData, Table
from sqlalchemy import create_engine

engine = create_engine("sqlite:///students.sqlite3")


metadata = MetaData()
messages = Table(
    "messages",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("message", Text),
)

messages.create(bind=engine)

insert_message = messages.insert().values(message="Hello, World!")
engine.execute(insert_message)

stmt = select([messages.c.message])
(message,) = engine.execute(stmt).fetchone()
print(message)

# %%
## Example Database
# %%
from sqlalchemy import create_engine, ForeignKey, Column, Integer, String, select
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///mycollege.db", echo=True)
Base = declarative_base()


def result_dict(r):
    return dict(zip(r.keys(), r))


def result_dicts(rs):
    return list(map(result_dict, rs))


class Department(Base):
    __tablename__ = "department"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    employees = relationship("Employee", secondary="link")


class Employee(Base):
    __tablename__ = "employee"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    departments = relationship(Department, secondary="link")


class Link(Base):
    __tablename__ = "link"
    department_id = Column(Integer, ForeignKey("department.id"), primary_key=True)
    employee_id = Column(Integer, ForeignKey("employee.id"), primary_key=True)


## Tables are created when following statement is run
Base.metadata.create_all(engine)
# %%


## Creating objectcs for both tables
d1 = Department(name="Accounts")
d2 = Department(name="Sales")
d3 = Department(name="Marketing")

e1 = Employee(name="John")
e2 = Employee(name="Tony")
e3 = Employee(name="Graham")

## Appending both tables so that
## "John" Object is in "Accounts"
## and "Accounts" Object is in "Graham"
e1.departments.append(d1)
e2.departments.append(d3)
d1.employees.append(e3)
d2.employees.append(e2)
d3.employees.append(e1)
e3.departments.append(d2)


Session = sessionmaker(bind=engine)
session = Session()
session.add(e1)
session.add(e2)
session.add(d1)
session.add(d2)
session.add(d3)
session.add(e3)
session.commit()
# %%


## Displaying tables in the terminal
## Databases will be shown in []
print(engine.table_names())
statement = select(Department).union_all
print(statement)

# %%
stmt = select("*").select_from(Link)
result = session.execute(stmt).fetchall()
result_dicts(result)

# %%
stmt = select("*").select_from(Department)
result = session.execute(stmt).fetchall()
result_dicts(result)
