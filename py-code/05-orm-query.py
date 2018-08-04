import os
from termcolor import colored, cprint

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column, ForeignKey
from sqlalchemy import Integer, String
from sqlalchemy import select, or_
from sqlalchemy.orm import Session, relationship

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

#2
#Using the Domain Model object oriented classes.
number = 1
code = """
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
print("-" * 80)
print("Unpacking tuples returned from sesson.query() method.")
for name, fullname in session.query(User.name, User.fullname):
    print(name, fullname)
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
print("-" * 80)
print("Unpacking tuples returned from sesson.query() method.")
for name, fullname in session.query(User.name, User.fullname):
    print(name, fullname)

input("\nEnter to continue...")

################################################################################

#3
#ORM and session.query() method.
number += 1
code = """
"""
heading = "ORM and session.query() method."
print_output(number,code,heading)

print("Mix entities and columns in the session.query() method.")
print("-" * 80)
result = session.query(User, User.name).all()
print(result)
print("-" * 80)

print("Indexing - Always remeber to use order_by().")
print("-" * 80)
result = session.query(User).order_by(User.id)[2]
print(result)
print("-" * 80)

print("Slicing - Always remember to use order_by().")
print("-" * 80)
result = session.query(User).order_by(User.id.desc())[1:3]
print(result)
print("-" * 80)

print("filter_by(attribute = 'value') for WHERE clause")
print("-" * 80)
result = session.query(User).filter_by(name = 'ed').first()
print(result)
print("-" * 80)

print("filter(DomainModel.attribute == 'value') for WHERE clause - can use SQL \
Expression.")
print("-" * 80)
result = session.query(User).filter(User.name == 'ed').first()
print(result)
print("-" * 80)

print("OR Conjunction")
print("-" * 80)
result = session.query(User).filter(or_(User.name == 'ed', User.id > 3)).all()
print(result)
for user in result:
    print(user.id, user.name, user.fullname)
print("-" * 80)

print("Using filter() in sequence automatically uses the AND conjunction.")
print("-" * 80)
query = session.query(User).filter(
                            User.name == 'ed').filter(User.id == 1)
print(query)
result = query.all()
for user in result:
    print(user.id, user.name, user.fullname)
print("-" * 80)

print("Formation of query doesn't execute the query.")
print("-" * 80)
query = session.query(User).filter(User.name.in_(["ed","wendy","mary"]))
print(query)
print("-" * 80)

print("Execution of a query to fetch - first(), all() or one()")
print("-" * 80)
result_first = query.first()
print("first() : {}".format(result_first))
result_all = query.all()
print(result_all)
print("-" * 80)
print("Execution of a query to fetch one() must yield only 1 row")
print("-" * 80)
query = session.query(User).filter(User.name == 'ed')
print(query)
result_one = query.one()
print("One row : {} {} {}".format(result_one.id,
                                  result_one.name, result_one.fullname))
input("\nEnter to continue...")

################################################################################

#4
#Exercies - 1

number += 1
coded = """
"""
heading = "Exercise - 1"
print_output(number,code,heading)

print("Getting fullname from User for all users - in alphabetical order.")
print("-" * 80)
query1 = session.query(User.fullname).order_by(User.fullname)
print(query1)
result1 = query1.all()
for full_name in result1:
    print(full_name[0])
print("-" * 80)

print("Modifying query1 to get only records for 'mary' and 'ed' and displaying")
print("the second record only.")
print("-" * 80)
query2 = query1.filter(or_(User.name == "mary",User.name == "ed"))
print(query2)
result2 = query2[1]
print(result2)

input("\nEnter to continue...")

################################################################################

#5
#Establishing relationship between Domain Models.
number += 1
code = """
class Address(Base):
    __tablename__ = 'address'

    id = Column(Integer, primary_key = True)
    email_address = Column(String(100), nullable = False)
    user_id = Column(Integer, ForeignKey(User.id))

    user = relationship("User", backref="addresses")

    def __repr__(self):
        return "<Address (%r) >" % self.email_address

Base.metadata.create_all(engine)
"""
heading = "Establishing relationship between Domain Models."
print_output(number,code,heading)

class Address(Base):
    __tablename__ = 'address'

    id = Column(Integer, primary_key = True)
    email_address = Column(String(100), nullable = False)
    user_id = Column(Integer, ForeignKey(User.id))

    user = relationship("User", backref="addresses")

    def __repr__(self):
        return "<Address (%r) >" % self.email_address

Base.metadata.create_all(engine)

input("\nEnter to continue...")

################################################################################

#6
#Add data and accessing data from the Domain Model using relationship.
number += 1
code = """
"""
heading="Add data and accessing data from the Domain Model using relationship."
print_output(number,code,heading)

print("Creating a new user - now also adds an 'addresses' attribute to it.")
print("-" * 80)
usr_jack = User(name = "jack", fullname = "Jack Bean")
print("id : {} \nname : {} \nfullname : {} \naddresses : {}".format(usr_jack.id,
usr_jack.name, usr_jack.fullname, usr_jack.addresses))
print("-" * 80)

print("Adding Address objects to 'addresses' collection of usr_jack object")
print("-" * 80)
usr_jack.addresses = [Address(email_address = 'jack@gmail.com'),
                       Address(email_address = 'j25@yahoo.com'),
                       Address(email_address= 'jack@hotmail.com')]

print("Accessing the user attribute of the Address object - yeilds User - jack")
print("-" * 80)
print(usr_jack.addresses[0].user)
print("-" * 80)

print("Cascading : Adding usr_jack object to a session automatically")
print("adds the Address objects created, to the session")
print("and can be verified using session.new.")
print("-" * 80)
session.add(usr_jack)
print(session.new)
print("-" * 80)

print("Unit of Work determines automatically the correct order in which the")
print("objects will be inserted.")
print("Committing the session - expires the objects.")
print("-" * 80)
print(usr_jack.__dict__)
session.commit()
print(usr_jack.__dict__)
print("-" * 80)

print("Accessing usr_jack.addresses will now perform a 'Lazy Load'.")
print("Retrieves id for usr_jack : {}".format(usr_jack.id))
print(usr_jack.__dict__)
print("-" * 80)
print("Lazy Loading addresses collection for usr_jack")
print(usr_jack.addresses)
print(usr_jack.__dict__)
print("-" * 80)

print("Changing the email_address of one user to belong to another user.")
print("-" * 80)
usr_fred = session.query(User).filter_by(name = "fred").one()
usr_jack.addresses[1].user = usr_fred
print("Email addresses for jack : {} ".format(usr_jack.addresses))
print("Email addresses for fred : {} ".format(usr_fred.addresses))
print(session.new)
print(session.dirty)
session.commit()

input("\nEnter to continue...")

################################################################################

os.system('clear')
print("\n"* 5)
cprint("END".rjust(38, " "), 'blue', attrs=['bold'])
heading = "NOTE: RESET YOUR GIT : git checkout -- orm-query.db"
heading = heading.rjust(( len(heading) + ((80 - len(heading)) // 2)), " ")
cprint('{}'.format(heading), 'red', attrs=['blink','bold'])
print("\n"* 5)
