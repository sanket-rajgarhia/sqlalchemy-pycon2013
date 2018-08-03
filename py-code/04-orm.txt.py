import os
from termcolor import colored, cprint

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column
from sqlalchemy import Integer, String
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

#Restore the state of metadata.db - prior to run
os.system('git checkout -- orm.db')

#Function to print heading and code
def print_output(number,code,heading):
    os.system('clear')
    number_print = "\nNo {}.".format(number)
    print(number_print)
    print("_"*len(number_print))
    print("{}".format(code).rstrip('\n'))
    print("\n{}".format(heading))
    print("-"*len(heading.split('\n')[0]))
    return

################################################################################

#1
#Creating the 'Declarative Base'.
number = 1
code = """
Base = declarative_base()
print(Base.metadata)
"""
heading = "#Creating the 'Declarative Base'."
print_output(number,code,heading)

Base = declarative_base()
print(Base.metadata)

input("\nEnter to continue...")

################################################################################

#2
#Creating the 'User' domain model using the Base class.
number += 1
code = """
class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key = True)
    name = Column(String)
    fullname = Column(String)

    #Overloading the inheretid function
    def __repr__(self):
        return "<User (%r %r)>" % (self.name, self.fullname)

print(User.__tablename__)
print(User.__mapper__)
"""
heading = "Creating the 'User' domain model using the Base class."
print_output(number,code,heading)

class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key = True)
    name = Column(String)
    fullname = Column(String)

    #Overloading the inheretid function
    def __repr__(self):
        return "<User (%r %r)>" % (self.name, self.fullname)

print(User.__tablename__)
print(User.__mapper__)

input("\nEnter to continue...")

################################################################################

#3
#Creating the engine and creating all tables in Base.metadata.
#Persisting the data in the data object.
number += 1
code = """
#Creating all tables in Base.metadata
engine = create_engine("sqlite:///orm.db")
Base.metadata.create_all(engine)

print("Persisting the data in the data object.")
print("-" * 80)
ed_user = User(name = 'ed', fullname = 'Edward Jones')
print(ed_user)
print("-" * 80)
session = Session(engine)
session.add(ed_user)
result = session.query(User).filter_by(name = 'ed').first()
print(result.id, result.name, result.fullname)
session.commit()
"""
heading = "Creating the engine and creating all tables in Base.metadata"
heading += "\nPersisting the data in the data object."
print_output(number,code,heading)

#Creating all tables in Base.metadata
engine = create_engine("sqlite:///orm.db")
Base.metadata.create_all(engine)

print("Persisting the data in the data object.")
print("-" * 80)
ed_user = User(name = 'ed', fullname = 'Edward Jones')
print(ed_user)
print("-" * 80)
session = Session(engine)
session.add(ed_user)
result = session.query(User).filter_by(name = 'ed').first()
print(result.id, result.name, result.fullname)
session.commit()

input("\nEnter to continue...")

################################################################################

os.system('clear')
print("\n"* 5)
cprint("END".rjust(38, " "), 'blue', attrs=['bold'])
heading = "NOTE: RESET YOUR GIT : git checkout -- orm.db"
heading = heading.rjust(( len(heading) + ((80 - len(heading)) // 2)), " ")
cprint('{}'.format(heading), 'red', attrs=['blink','bold'])
print("\n"* 5)
