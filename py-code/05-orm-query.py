import os
from termcolor import colored, cprint

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column
from sqlalchemy import Integer, String
from sqlalchemy import select
from sqlalchemy.orm import Session

#Restore the state of orm-query.db - prior to run
os.system('git checkout -- orm-query.db')

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
#Initialization.
Base = declarative_base()

class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key = True)
    name = Column(String)
    fullname = Column(String)

    #Overloading the inheretid function
    def __repr__(self):
        return "<User (%r %r)>" % (self.name, self.fullname)

engine = create_engine("sqlite:///orm-query.db")
Base.metadata.create_all(engine)

session = Session(engine)
session.add_all([
                  User(name = 'ed', fullname = 'Edward Jones'),
                  User(name = 'wendy', fullname = 'Wendy Weathersmith'),
                  User(name = 'mary', fullname = 'Mary Contrary'),
                  User(name = 'fred', fullname = 'Fred Flintstone')
                ])
session.commit()

################################################################################

#1
#Using the Domain Model object oriented classes.
number = 1
code = """
print("Attributes of Domain Model classes act as Column() objects.")
print(User.name == 'ed')
"""
heading = "Using the Domain Model object oriented classes."
print_output(number,code,heading)

print("Attributes of Domain Model classes act just as Column() objects.")
print(User.name == 'ed')
print("-" * 80)
print("To get the Column() object - use property.columns")
print("User.name.property.columns[0]: {}".format(User.name.property.columns[0]))
print("-" * 80)
print("Using the Domain Model object instead of table and column objects in \
SQL Expression.")
select_stmt = select([User.id.label("ID"), User.name, User.fullname]).where(
                      User.name.in_(['ed','wendy'])).order_by(User.name.desc())
print(select_stmt)
print("-" * 80)
print("Use session.connection().execute(query) to execute a query on a \
database that the engine is connected to.")
result = session.connection().execute(select_stmt).fetchall()
print(result)
print("-" * 80)
print("Using ORM session.query() with Domain Model OO class.")
query = session.query(User.id.label("ID"), User.name, User.fullname).filter(
                       User.name.in_(['ed','wendy'])).order_by(User.name.desc())
result = query.all()
print(result)
input("\nEnter to continue...")

################################################################################

os.system('clear')
print("\n"* 5)
cprint("END".rjust(38, " "), 'blue', attrs=['bold'])
heading = "NOTE: RESET YOUR GIT : git checkout -- orm-query.db"
heading = heading.rjust(( len(heading) + ((80 - len(heading)) // 2)), " ")
cprint('{}'.format(heading), 'red', attrs=['blink','bold'])
print("\n"* 5)
