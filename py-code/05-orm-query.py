import os
from termcolor import colored, cprint

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column
from sqlalchemy import Integer, String
from sqlalchemy import select
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

os.system('clear')
print("\n"* 5)
cprint("END".rjust(38, " "), 'blue', attrs=['bold'])
heading = "NOTE: RESET YOUR GIT : git checkout -- orm.db"
heading = heading.rjust(( len(heading) + ((80 - len(heading)) // 2)), " ")
cprint('{}'.format(heading), 'red', attrs=['blink','bold'])
print("\n"* 5)
