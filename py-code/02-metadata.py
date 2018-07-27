import os
from termcolor import colored, cprint

from sqlalchemy import MetaData
from sqlalchemy import Table, Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer, String, DateTime, Numeric, Enum
from sqlalchemy import create_engine

#Restore the state of metadata.db - prior to run
os.system('git checkout -- metadata.db')

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
#Using the MetaData() object to containg the structure of the schema.
#Create the 'user' table.
number = 1
code = """
metadata = MetaData()
user_table = Table('user', metadata,
    Column('id', Integer, primary_key = True),
    Column('name', String),
    Column('fullname', String))
"""
heading = "Listing the attributes of user_table."
print_output(number,code,heading)

metadata = MetaData()
user_table = Table('user', metadata,
    Column('id', Integer, primary_key = True),
    Column('name', String),
    Column('fullname', String))

#List attributes of user_table
print("user_table.name : {}". format(user_table.name))
print("user_table.columns : {}".format(user_table.columns))
print("user_table.columns.id : {}".format(user_table.columns.id))
print("user_table.columns.id.type : {}".format(user_table.columns.id.type))
print("user_table.columns.name.name : {}".format(user_table.columns.name.name))
print("user_table.columns.keys() : {}".format(user_table.columns.keys()))
name_column = user_table.columns.name
print("name_column : {}".format(name_column))
print("name_column.table : {}".format(name_column.table))
print("user_table.primary_key : {}".format(user_table.primary_key))
print("user_table.select() : {}".format(user_table.select()))

input("\nEnter to continue...")

################################################################################

#2
#Using the metadata.create_all(engine) method to create all tables in a schema.
#If a table exists then it will not be created again.
#Add the 'user' table to the schema.
number += 1
code = """
engine = create_engine("sqlite:///metadata.db")
metadata.create_all(engine)
"""
heading = "Using the metadata.create_all(engine) method to create all tables\n\
in a schema.\nIf a table exists then it will not be created again.\n\
Add the 'user' table to the schema."
print_output(number,code,heading)

engine = create_engine("sqlite:///metadata.db")
metadata.create_all(engine)

input("\nEnter to continue...")

################################################################################

#3
#Creating a table with different data types.
#Using the table object's create(engine) method to create the table
#in the database.
number += 1
code = """
table_fancy = Table('fancy',metadata,
                     Column(key, String(50), primary_key = True),
                     Column(timestamp, DateTime),
                     Column(amount, Integer(10,2)),
                     Column(type, Enum('a', 'b', 'c'))
                    )
table_fancy.create(engine)
"""
heading = "Creating a table with different data types and using the table \n\
object's create(engine) method to create the table\n\
in the database."
print_output(number,code,heading)

table_fancy = Table('fancy',metadata,
                     Column('key', String(50), primary_key = True),
                     Column('timestamp', DateTime),
                     Column('amount', Numeric(10,2)),
                     Column('type', Enum('a', 'b', 'c'))
                    )
table_fancy.create(engine)

input("\nEnter to continue...")

################################################################################

#4
#Creating a table with Foreign Key.
#Using the table object's create(engine) method to
number += 1
code = """
address_table = Table('address',metadata,
                      Column('id', Integer, primary_key = True),
                      Column('email_address',String(100), nullable = False)
                      Column('user_id', Integer, ForeignKey('user.id'))
                      )
address_table.create(engine)
"""
heading = "Creating a table with Foreign Key constraint.\n\
Using the table object's create(engine) method to \n\
create the table in the database."
print_output(number,code,heading)

address_table = Table('address',metadata,
                      Column('id', Integer, primary_key = True),
                      Column('email_address',String(100), nullable = False),
                      Column('user_id', Integer, ForeignKey('user.id'))
                      )
address_table.create(engine)

input("\nEnter to continue...")

################################################################################
os.system('clear')
print("\n"* 5)
cprint("END".rjust(38, " "), 'blue', attrs=['bold'])
heading = "NOTE: RESET YOUR GIT : git checkout -- metadata.db"
heading = heading.rjust(( len(heading) + ((80 - len(heading)) // 2)), " ")
cprint('{}'.format(heading), 'red', attrs=['blink','bold'])
print("\n"* 5)
