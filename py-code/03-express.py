import os
from termcolor import colored, cprint

from sqlalchemy import MetaData
from sqlalchemy import create_engine
from sqlalchemy import Table
from sqlalchemy import and_, or_
from sqlalchemy.dialects import mysql, postgresql, sqlite

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
print(type(user_table.c.username == 'ed').__mro__)
input("\nEnter to continue...")

################################################################################

#3
#Building expressions using SQL Expression - 1.
number += 1
code = """
#Conjunctions
print((user_table.c.username == 'ed') | (user_table.c.username == 'jack'))
#Import and_ and or_ and build conjuctions
print(and_(user_table.c.fullname == 'ed jones',
       or_(user_table.c.username == 'ed', user_table.c.username == 'jack')
          )
     )
#Comparison operator
print(user_table.c.id > 5)
#NULL and IS NOT NULL - Import is_
print(user_table.c.username == None)
print(user_table.c.username != None)
print(user_table.c.username.is_(None))
#Addition and string concatenation
print(user_table.c.id + 5)
print(user_table.c.fullname + "Family name")
#IN
print(user_table.c.username.in_(["wendy", "mary", "ed"]))
"""
heading = "Building expressions using SQL Expression."
print_output(number,code,heading)

#Conjunctions
print((user_table.c.username == 'ed') | (user_table.c.username == 'jack'))
#Import and_ and or_ and build conjuctions
print(and_(user_table.c.fullname == 'ed jones',
       or_(user_table.c.username == 'ed', user_table.c.username == 'jack')
          )
     )
#Comparison operator
print(user_table.c.id > 5)
#NULL and IS NOT NULL - Import is_
print(user_table.c.username == None)
print(user_table.c.username != None)
print(user_table.c.username.is_(None))
#Addition and string concatenation
print(user_table.c.id + 5)
print(user_table.c.fullname + "Family name")
#IN
print(user_table.c.username.in_(["wendy", "mary", "ed"]))

input("\nEnter to continue...")

################################################################################

#4
#Building expressions using SQL Expression - 2.
number += 1
code = """
#Dialect differences
print("Dialect Differences.")
print("-" * 80)
expression = user_table.c.username == 'ed'
print(expression.compile(dialect=mysql.dialect()))
print(expression.compile(dialect=postgresql.dialect()))
print(expression.compile(dialect=sqlite.dialect()))
print("-" * 80)
#Expressions as an object - BinaryExpression object.
print("Expression as an object - BinaryExpression object.")
print("-" * 80)
print("expression : {}".format(expression))
print("type(expression) : {}".format(type(expression)))
print("expression.left : {}".format(expression.left))
print("expression.right : {}".format(expression.right))
print("expression.operator : {}".format(expression.operator))
print("-" * 80)
#Compiling expressions
print("Parameters of expressions")
print("-" * 80)
expression2 = user_table.c.username.in_(["wendy", "mary", "ed"])
compiled=expression2.compile()
print("expression2 : {}".format(expression2))
print("xpression2.compile().params : {}".format(compiled.params))
print("-" * 80)
"""
heading = "Building expressions using SQL Expression."
print_output(number,code,heading)

#Dialect differences
print("Dialect Differences.")
print("-" * 80)
expression = user_table.c.username == 'ed'
print(expression.compile(dialect=mysql.dialect()))
print(expression.compile(dialect=postgresql.dialect()))
print(expression.compile(dialect=sqlite.dialect()))
print("-" * 80)
#Expressions as an object - BinaryExpression object.
print("Expression as an object - BinaryExpression object.")
print("-" * 80)
print("expression : {}".format(expression))
print("type(expression) : {}".format(type(expression)))
print("expression.left : {}".format(expression.left))
print("expression.right : {}".format(expression.right))
print("expression.operator : {}".format(expression.operator))
print("-" * 80)
#Compiling expressions
print("Parameters of expressions")
print("-" * 80)
expression2 = user_table.c.username.in_(["wendy", "mary", "ed"])
compiled=expression2.compile()
print("expression2 : {}".format(expression2))
print("xpression2.compile().params : {}".format(compiled.params))
print("-" * 80)

input("\nEnter to continue...")

################################################################################

#4
#Using expressions in select statement.
number += 1
code = """
statement = user_table.select().where(user_table.c.username == 'ed')
print(statement)
result = engine.execute(statement)
print(result.fetchall())
"""
heading = "Using expressions in select statement."
print_output(number,code,heading)

statement = user_table.select().where(user_table.c.username == 'ed')
print(statement)
result = engine.execute(statement)
print(result.fetchall())

input("\nEnter to continue...")

################################################################################

os.system('clear')
print("\n"* 5)
cprint("END".rjust(38, " "), 'blue', attrs=['bold'])
heading = "NOTE: RESET YOUR GIT : git checkout -- express.db"
heading = heading.rjust(( len(heading) + ((80 - len(heading)) // 2)), " ")
cprint('{}'.format(heading), 'red', attrs=['blink','bold'])
print("\n"* 5)
