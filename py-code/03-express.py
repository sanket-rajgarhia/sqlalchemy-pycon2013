import os
from termcolor import colored, cprint

from sqlalchemy import MetaData
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy import Integer, String
from sqlalchemy import and_, or_
from sqlalchemy.dialects import mysql, postgresql, sqlite
from sqlalchemy import select, func

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

#5
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

#6
#Exercise
number += 1
code = """
print("Expression for : user.fullname = 'ed'")
expression1 = user_table.c.fullname == 'ed'
print(expression1)
print("Expression for : user.fullname = 'ed' AND user.id > 5  ")
expression2 = and_(user_table.c.fullname == 'ed', user_table.c.id > 5)
print(expression2)
print("Expression for : user.username = 'edward' OR \
(user.fullname = 'ed' AND user.id > 5) ")
expression3 = or_(user_table.c.username == 'edward',
              and_(user_table.c.fullname == 'ed', user_table.c.id > 5))
print(expression3)
note="NOTE: NO brackets surrounding the AND clause is required since it has \
\nhigher precedence than OR and executes first in the above listed query."
cprint(note, 'red', attrs=['bold'])
print("Expression for : user.username = 'edward' AND \
(user.fullname = 'ed' OR user.id > 5) ")
expression4 = and_(user_table.c.username == 'edward',
              or_(user_table.c.fullname == 'ed', user_table.c.id > 5))
print(expression4)
"""
heading = "Exercise."
print_output(number,code,heading)

print("Expression for : user.fullname = 'ed'")
expression1 = user_table.c.fullname == 'ed'
print(expression1)
print("Expression for : user.fullname = 'ed' AND user.id > 5  ")
expression2 = and_(user_table.c.fullname == 'ed', user_table.c.id > 5)
print(expression2)
print("Expression for : user.username = 'edward' OR \
(user.fullname = 'ed' AND user.id > 5) ")
expression3 = or_(user_table.c.username == 'edward',
              and_(user_table.c.fullname == 'ed', user_table.c.id > 5))
print(expression3)
note="NOTE: NO brackets surrounding the AND clause is required since it has \
\nhigher precedence than OR and executes first in the above listed query."
cprint(note, 'red', attrs=['bold'])
print("Expression for : user.username = 'edward' AND \
(user.fullname = 'ed' OR user.id > 5) ")
expression4 = and_(user_table.c.username == 'edward',
              or_(user_table.c.fullname == 'ed', user_table.c.id > 5))
print(expression4)

input("\nEnter to continue...")

################################################################################

#7
#Insert SQL statement.
number += 1
code = """
print("insert into user (username,fullname) values ('ed', 'Ed Jones')")
print('-' * 80)
insert_stmt = user_table.insert().values(username='ed', fullname='Ed Jones')
print(insert_stmt)
connection = engine.connect()
result = connection.execute(insert_stmt)

print("result.inserted_primary_key : {}".format(result.inserted_primary_key))
print('-' * 80)
print("Multiple Insert")
print('-' * 80)
insert_stm = user_table.insert()
print(insert_stm)
result = connection.execute(insert_stm, [
             {'username' : 'jack', 'fullname' : 'Jack Burger'},
             {'username' : 'wendy', 'fullname' : 'Wendy Weathersmith'}])
connection.close()
"""
heading = "Insert SQL statement."
print_output(number,code,heading)

print("insert into user (username,fullname) values ('ed', 'Ed Jones')")
print('-' * 80)
insert_stmt = user_table.insert().values(username='ed', fullname='Ed Jones')
print(insert_stmt)
connection = engine.connect()
result = connection.execute(insert_stmt)

print("result.inserted_primary_key : {}".format(result.inserted_primary_key))
print('-' * 80)
print("Multiple Insert")
print('-' * 80)
insert_stm = user_table.insert()
print(insert_stm)
result = connection.execute(insert_stm, [
             {'username' : 'jack', 'fullname' : 'Jack Burger'},
             {'username' : 'wendy', 'fullname' : 'Wendy Weathersmith'}])
connection.close()

input("\nEnter to continue...")

################################################################################

#8
#SELECT statement.
number += 1
code = """
cprint("Fetching selected columns and filtered by a where clause.", 'red' )
print('-' * 80)
statement = select([user_table.c.username, user_table.c.fullname])\
.where(user_table.c.username == 'ed')
print(statement)
connection = engine.connect()
result = connection.execute(statement)
print('-' * 80)
print(result.fetchall())
print('-' * 80)

cprint("Fetching the full table.", 'red')
print('-' * 80)
statement = select([user_table])
print(statement)
result = connection.execute(statement)
print('-' * 80)
print(result.fetchall())
print('-' * 80)

cprint("Two where() clauses are joined by an AND.", 'red')
print('-' * 80)
statement = select([user_table]).where(user_table.c.username == 'ed')\
.where(user_table.c.fullname == 'Ed Jones')
print(statement)
result = connection.execute(statement)
print('-' * 80)
print(result.fetchall())
print('-' * 80)

cprint('Using order_by()', 'red')
print("-" * 80)
statement = select([user_table]).order_by(user_table.c.fullname)
print(statement)
result = connection.execute(statement)
print('-' * 80)
print(result.fetchall())
print('-' * 80)

connection.close()
"""
heading = "SELECT statement."
print_output(number,code,heading)

cprint("Fetching selected columns and filtered by a where clause.", 'red' )
print('-' * 80)
statement = select([user_table.c.username, user_table.c.fullname])\
.where(user_table.c.username == 'ed')
print(statement)
connection = engine.connect()
result = connection.execute(statement)
print('-' * 80)
print(result.fetchall())
print('-' * 80)

cprint("Fetching the full table.", 'red')
print('-' * 80)
statement = select([user_table])
print(statement)
result = connection.execute(statement)
print('-' * 80)
print(result.fetchall())
print('-' * 80)

cprint("Two where() clauses are joined by an AND.", 'red')
print('-' * 80)
statement = select([user_table]).where(user_table.c.username == 'ed')\
.where(user_table.c.fullname == 'Ed Jones')
print(statement)
result = connection.execute(statement)
print('-' * 80)
print(result.fetchall())
print('-' * 80)

cprint('Using order_by()', 'red')
print("-" * 80)
statement = select([user_table]).order_by(user_table.c.fullname)
print(statement)
result = connection.execute(statement)
print('-' * 80)
print(result.fetchall())
print('-' * 80)

connection.close()

input("\nEnter to continue...")

################################################################################

#9
#Exercise - 2.
number += 1
code = """
"""
heading = "Exercise - 2."
print_output(number,code,heading)

cprint("Insert Dilbert Jones into user table and fetch id.", 'red')
print("-" * 80)
statement = user_table.insert().values(username = 'dilbert',
                                       fullname = 'Dilbert Jones')
print(statement)
connection = engine.connect()
result = connection.execute(statement)
print(result.inserted_primary_key)
print("-" * 80)
cprint("select from user table where username is 'wendy' OR 'dilbert'", 'red')
print("-" * 80)
statement = select([user_table]).where(
            or_(user_table.c.username == 'wendy',
                user_table.c.username == 'dilbert'))
print(statement)
result = connection.execute(statement)
print(result.fetchall())

connection.close()

input("\nEnter to continue...")

################################################################################

#10
#Creation of Address table and insertion of values.
number += 1
code = """
address_table = Table('address', metadata,
            Column('id', Integer, primary_key = True),
            Column('user_id', Integer, ForeignKey('user.id'), nullable = False),
            Column('email_address', String(100),nullable = False))
address_table.create(engine)

result = engine.execute(address_table.insert(),[
        {"user_id": 1, "email_address": "ed@ed.com"},
        {"user_id": 1, "email_address": "ed@gmail.com"},
        {"user_id": 2, "email_address": "jack@yahoo.com"},
        {"user_id": 3, "email_address": "wendy@gmail.com"}])

result = engine.execute(select([address_table]))
print(result.fetchall())
"""
heading = "Creation of Address table and insertion of values."
print_output(number,code,heading)

address_table = Table('address', metadata,
            Column('id', Integer, primary_key = True),
            Column('user_id', Integer, ForeignKey('user.id'), nullable = False),
            Column('email_address', String(100),nullable = False))
address_table.create(engine)

result = engine.execute(address_table.insert(),[
        {"user_id": 1, "email_address": "ed@ed.com"},
        {"user_id": 1, "email_address": "ed@gmail.com"},
        {"user_id": 2, "email_address": "jack@yahoo.com"},
        {"user_id": 3, "email_address": "wendy@gmail.com"}])

result = engine.execute(select([address_table]))
print(result.fetchall())

input("\nEnter to continue...")

################################################################################

#11
#Demonstrating joins.
number += 1
code = """
print("table1.join(table2,on clause)")
print("-" * 80)
join_clause1 = user_table.join(address_table,
                              user_table.c.id == address_table.c.user_id)
print(join_clause1)
print("-" * 80)
print("table1.join(table2) - ON clause automatically figured out")
print("due to Foreign Key relationship between table2 and table1")
print("-" * 80)
join_clause2 = user_table.join(address_table)
print(join_clause2)
print("-" * 80)

print("Using select_from() to connect the join clause to a select statement.")
print("-" * 80)
select_stmt = select([user_table, address_table]).select_from(join_clause2)
print(select_stmt)
result = engine.execute(select_stmt)
print(result.fetchall())
"""
heading = "Demonstrating joins."
print_output(number,code,heading)

print("table1.join(table2,on clause)")
print("-" * 80)
join_clause1 = user_table.join(address_table,
                              user_table.c.id == address_table.c.user_id)
print(join_clause1)
print("-" * 80)
print("table1.join(table2) - ON clause automatically figured out")
print("due to Foreign Key relationship between table2 and table1")
print("-" * 80)
join_clause2 = user_table.join(address_table)
print(join_clause2)
print("-" * 80)

print("Using select_from() to connect the join clause to a select statement.")
print("-" * 80)
select_stmt = select([user_table, address_table]).select_from(join_clause2)
print(select_stmt)
result = engine.execute(select_stmt)
print(result.fetchall())

input("\nEnter to continue...")

################################################################################

#12
#The select() returns a selectable. It is like a temporary table.
number += 1
code = """
sel_stmt = select([user_table])
filtered_stmt = select([sel_stmt.c.id, sel_stmt.c.username]).where(
                sel_stmt.c.id > 2)
print(filtered_stmt)
result = engine.execute(filtered_stmt)
print(result.fetchall())
"""
heading = "The select() returns a selectable. It is like a temporary table."
print_output(number,code,heading)

sel_stmt = select([user_table])
filtered_stmt = select([sel_stmt.c.id, sel_stmt.c.username]).where(
                sel_stmt.c.id > 2)
print(filtered_stmt)
result = engine.execute(filtered_stmt)
print(result.fetchall())

input("\nEnter to continue...")

################################################################################

#13
#A subquery is same as an alias of select().
number += 1
code = """
select_stmt = select([user_table]).where(
                                   user_table.c.username.in_(['ed','jack']))
print(select_stmt)
print("-" * 80)
select_alias = select_stmt.alias()
print(select_alias)
print("-" * 80)
select_from_alias = select([select_alias.c.id, select_alias.c.fullname]).where(
                    select_alias.c.username == "ed")
print(select_from_alias)
print("-" * 80)
result = engine.execute(select_from_alias)
print(result.fetchall())
"""
heading = "A subquery is same as an alias of select()."
print_output(number,code,heading)

select_stmt = select([user_table]).where(
                                   user_table.c.username.in_(['ed','jack']))
print(select_stmt)
print("-" * 80)
select_alias = select_stmt.alias()
print(select_alias)
print("-" * 80)
select_from_alias = select([select_alias.c.id, select_alias.c.fullname]).where(
                    select_alias.c.username == "ed")
print(select_from_alias)
print("-" * 80)
result = engine.execute(select_from_alias)
print(result.fetchall())

input("\nEnter to continue...")

################################################################################

#14
#Scalar select and group_by().
number += 1
code = """
"""
heading = "Scalar select and group_by()."
print_output(number,code,heading)

select_stmt = select([address_table.c.user_id,
                      func.count(address_table.c.id).label('count')]).group_by(
                      address_table.c.user_id)
print(select_stmt)
print("-" * 80)
result = engine.execute(select_stmt)
print(result.fetchall())
print("-" * 80)
select_alias = select_stmt.alias()
address_select = select([select_alias.c.count]).where(
                 select_alias.c.user_id == 1)
print(address_select)
print("-" * 80)
result = engine.execute(address_select)
print(result.fetchall())

input("\nEnter to continue...")

################################################################################

#15
#Scalar select as a column in a select.Use of as_scalar().
number += 1
code = """
subq_address = select([address_table.c.user_id,
                      func.count(address_table.c.id).label('count')]).group_by(
                      address_table.c.user_id).alias()
select_stmt = select([user_table.c.fullname,
                      subq_address.c.count]).select_from(
                      user_table.join(subq_address))
print(select_stmt)
result = engine.execute(select_stmt)
print(result.fetchall())
print("-" * 80)
subq_address = select([func.count(address_table.c.id)]).where(
                      user_table.c.id == address_table.c.user_id)
print(subq_address)
result = engine.execute(subq_address)
print(result.fetchall())
print("-" * 80)
scalar_sel = select([user_table.c.fullname, subq_address.as_scalar()])
print(scalar_sel)
result = engine.execute(scalar_sel)
print(result.fetchall())
"""
heading = "Scalar select as a column in a select.Use of as_scalar()."
print_output(number,code,heading)

subq_address = select([address_table.c.user_id,
                      func.count(address_table.c.id).label('count')]).group_by(
                      address_table.c.user_id).alias()
select_stmt = select([user_table.c.fullname,
                      subq_address.c.count]).select_from(
                      user_table.join(subq_address))
print(select_stmt)
result = engine.execute(select_stmt)
print(result.fetchall())
print("-" * 80)
subq_address = select([func.count(address_table.c.id)]).where(
                      user_table.c.id == address_table.c.user_id)
print(subq_address)
result = engine.execute(subq_address)
print(result.fetchall())
print("-" * 80)
scalar_sel = select([user_table.c.fullname, subq_address.as_scalar()])
print(scalar_sel)
result = engine.execute(scalar_sel)
print(result.fetchall())

input("\nEnter to continue...")

################################################################################

#16
#Exercise - 3.
number += 1
code = """
select_stmt = select([user_table.c.fullname,
                      address_table.c.email_address]).select_from(
                      user_table.join(address_table)).where(
                      user_table.c.username == 'ed').order_by(
                      address_table.c.email_address)
print(select_stmt)
print("-" * 80)
result = engine.execute(select_stmt)
print(result.fetchall())
"""
heading = "Exercise - 3."
print_output(number,code,heading)

select_stmt = select([user_table.c.fullname,
                      address_table.c.email_address]).select_from(
                      user_table.join(address_table)).where(
                      user_table.c.username == 'ed').order_by(
                      address_table.c.email_address)
print(select_stmt)
print("-" * 80)
result = engine.execute(select_stmt)
print(result.fetchall())

input("\nEnter to continue...")

################################################################################

#N
#Section heading.
number += 1
code = """
"""
heading = ""
print_output(number,code,heading)

input("\nEnter to continue...")

################################################################################
os.system('clear')
print("\n"* 5)
cprint("END".rjust(38, " "), 'blue', attrs=['bold'])
heading = "NOTE: RESET YOUR GIT : git checkout -- express.db"
heading = heading.rjust(( len(heading) + ((80 - len(heading)) // 2)), " ")
cprint('{}'.format(heading), 'red', attrs=['blink','bold'])
print("\n"* 5)
