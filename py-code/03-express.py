import os
from termcolor import colored, cprint

from sqlalchemy import MetaData
from sqlalchemy import create_engine
from sqlalchemy import Table

#Restore the state of metadata.db - prior to run
os.system('git checkout -- express.db')

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
#Extracting the column details of a table loaded from sqlite3 database.
number = 1
code = """
#Bind metadata to the engine
engine = create_engine("sqlite:///express.db")
metadata = MetaData(engine)

#Reflection - Load the user table
user_table = Table('user', metadata, autoload = True, autoload_with = engine)

#Print the column details
print(user_table.c.username.name)
print(user_table.c.username.type)
print(user_table.c.username.nullable)
print(user_table.c.username.primary_key)
print(user_table.c.username.foreign_keys)

"""
heading = "Extracting the column details of a table loaded from sqlite3 \
\ndatabase."
print_output(number,code,heading)

#Bind metadata to the engine
engine = create_engine("sqlite:///express.db")
metadata = MetaData(engine)

#Reflection - Load the user table
user_table = Table('user', metadata, autoload = True, autoload_with = engine)

#Print the column details
print(user_table.c.username.name)
print(user_table.c.username.type)
print(user_table.c.username.nullable)
print(user_table.c.username.primary_key)
print(user_table.c.username.foreign_keys)

input("\nEnter to continue...")

################################################################################

#2
#Comparison operators in SQL Expression do not yeild a True or False.
#It results in an object with the value at the end of == being converted into
#a bound parameter.

number += 1
code = """
print(user_table.c.username == 'ed')
"""
heading = "Comparison operators in SQL Expression do not yeild a True or False."
heading += "\nIt results in an object with the value at the end of == being "
heading += "\nconverted into a bound parameter."
print_output(number,code,heading)

print(user_table.c.username == 'ed')

input("\nEnter to continue...")

################################################################################

os.system('clear')
print("\n"* 5)
cprint("END".rjust(38, " "), 'blue', attrs=['bold'])
heading = "NOTE: RESET YOUR GIT : git checkout -- express.db"
heading = heading.rjust(( len(heading) + ((80 - len(heading)) // 2)), " ")
cprint('{}'.format(heading), 'red', attrs=['blink','bold'])
print("\n"* 5)
