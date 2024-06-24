#!/usr/bin/python3
from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, CHAR
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Person(Base):
    __tablename__ = "people"

    ssn = Column("ssn", Integer, primary_key=True)
    first_name = Column("firstname", String(200))
    last_name = Column("lastname", String(200))
    gender = Column("gender", CHAR)
    age = Column("age", Integer)

    def __init__(self, ssn, first, last, gender, age):
        self.ssn = ssn
        self.first_name = first
        self.last_name = last
        self.gender = gender
        self.age = age

    def __repr__(self):
        return f"{self.ssn} {self.first_name} {self.last_name} {self.gender}, {self.age}"

class Thing(Base):
    __tablename__ = "things"

    tid = Column("tid", Integer, primary_key=True)
    description = Column("description", String(200))
    owner = Column(Integer, ForeignKey("people.ssn"))

    def __init__(self, tid, description, owner):
        self.tid = tid
        self.description = description
        self.owner = owner

    def __repr__(self):
        return f"({self.tid} {self.description} {self.owner})"

engine = create_engine('mysql+mysqldb://gmb:#Kamusinde2016@localhost/mydb')

Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

person = Person(12312, "Mike", "Smith", "M", 35)
session.add(person)
session.commit()

p1 = Person(56454, "Anna", "Blue", "F", 40)
p2 = Person(16171, "Bob", "Blue", "M", 35)
p3 = Person(44848, "Angela", "Cold", "F", 22)

session.add(p1)
session.add(p2)
session.add(p3)
session.commit()

results = session.query(Person).filter(Person.first_name.in_(['Anna', 'Mike']))
for person in results:
    print(person)

t1 = Thing(1, "Car", p1.ssn)
t2 = Thing(2, "Laptop", p2.ssn)
t3 = Thing(3, "PS5", p3.ssn)
t4 = Thing(4, "Tool", p3.ssn)
t5 = Thing(5, "Book", p3.ssn)

session.add(t1)
session.add(t2)
session.add(t3)
session.add(t4)
session.add(t5)
session.commit()

results = session.query(Thing, Person).filter(Thing.owner == Person.ssn).filter(Person.first_name == 'Anna').all()
for r in results:
    print(r)
