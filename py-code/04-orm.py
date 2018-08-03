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

################################################################################

#4
#Inserting multiple rows into the table.
number += 1
code = """
session = Session(engine)
wendy_user = User(name = 'wendy', fullname = 'Wendy Weathersmith')
session.add(wendy_user)

session.add_all([
    User(name = 'mary', fullname = 'Mary Contrary'),
    User(name = 'fred', fullname = 'Fred Flintstone')
])

print("Pending user list not yet flushed : {}".format(session.new))

our_user = session.query(User).filter_by(name = 'wendy').first()
print(our_user.id, our_user.name, our_user.fullname)

print("Pending user list after fetching using a query : {}".format(session.new))
print("wendy_user = our_user : {}".format(wendy_user == our_user))
print("id(wendy_user) id(our_user): {} {}".format(id(wendy_user), id(our_user)))

session.commit()

print("After session.commit() - transaction endsand all variables are expired.")
print("Accessing domain objects after expiration results in lazy loading.")
print(wendy_user.fullname)
print(wendy_user.__dict__)
"""
heading = "Inserting multiple rows into the table. "
print_output(number,code,heading)

print("Creating a session using - session = Session(engine)")
session = Session(engine)

print("Adding User objects to the session - using session.add_all([ U1, U2])")
wendy_user = User(name = 'wendy', fullname = 'Wendy Weathersmith')
session.add(wendy_user)

session.add_all([
    User(name = 'mary', fullname = 'Mary Contrary'),
    User(name = 'fred', fullname = 'Fred Flintstone')
])

print("Pending user list not yet flushed : {}".format(session.new))

print("A query to the table flushes the pending entries to the database")
print("before fetching new data.")
our_user = session.query(User).filter_by(name = 'wendy').first()

print("Data Fetched for User whose name = 'wendy'")
print(our_user.id, our_user.name, our_user.fullname)

print("Pending user list after fetching using a query : {}".format(session.new))
print("-" * 80)

print("Comparing wendy_user and our_user for Identity Mapping within a Unit of \
Work")
print("wendy_user = our_user : {}".format(wendy_user == our_user))
print("id(wendy_user) id(our_user): {} {}".format(id(wendy_user), id(our_user)))

session.commit()

print("After session.commit() - transaction endsand all variables are expired.")
print("Accessing domain objects after expiration results in lazy loading.")
print(wendy_user.fullname)
print(wendy_user.__dict__)

input("\nEnter to continue...")

################################################################################

os.system('clear')
print("\n"* 5)
cprint("END".rjust(38, " "), 'blue', attrs=['bold'])
heading = "NOTE: RESET YOUR GIT : git checkout -- orm.db"
heading = heading.rjust(( len(heading) + ((80 - len(heading)) // 2)), " ")
cprint('{}'.format(heading), 'red', attrs=['blink','bold'])
print("\n"* 5)
