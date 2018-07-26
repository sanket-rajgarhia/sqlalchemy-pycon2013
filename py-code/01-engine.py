import os
from sqlalchemy import create_engine

#Restore the state of engine.db - prior to run
os.system('git checkout -- engine.db')

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
#engine is a factory for database connections.
number = 1
code = """
engine = create_engine("sqlite:///engine.db")
"""
heading = "Initializing the engine."
print_output(number,code,heading)

#Code
engine = create_engine("sqlite:///engine.db")

input("\nEnter to continue...")

################################################################################

#2
#Demonstrating the execute() method to get the result of the query.
#and also using fetchone() on the result.
number += 1
code = """
result = engine.execute("select emp_id, emp_name from employee "
                        "where emp_id=:empid", empid = 3)
row = result.fetchone()
"""
heading = "Accessing 'row'."
print_output(number,code,heading)

#Code
result = engine.execute("select emp_id, emp_name from employee "
                        "where emp_id=:empid", empid = 3)
row = result.fetchone()
result.close()
print("row : {}".format(row))
print("row['emp_name'] : {}".format(row['emp_name']))
print("row.emp_name : {}".format(row.emp_name))
print("row.keys() : {}".format(row.keys()))

input("\nEnter to continue...")

################################################################################

#3
#Demonstrating that result is iterable.
number += 1
code = """
result = engine.execute("select * from employee")
for row in result:
    print(row)
result.close()
"""
heading = "The object 'result' is iterable."
print_output(number, code, heading)

#Code
result = engine.execute("select * from employee")
for row in result:
    print(row)
result.close()

input("\nEnter to continue...")

################################################################################

#4
#Demonstrating fetchall() to fetch a list and result object gets exhausted.
#Calling result.fetchall() returns an empty list.
number += 1
code = """
result = engine.execute("select * from employee")
print(result.fetchall())
print(result.fetchall())
result.close()
"""
heading = "Demonstrating - fetchall() returns a list of rows and exhausts \
result."
print_output(number,code,heading)

result = engine.execute("select * from employee")
print(result.fetchall())
print(result.fetchall())
result.close()

input("\nEnter to continue...")

################################################################################

#5
#The execute() method auto commits for statements like INSERT, UPDATE, DELETE.
number += 1
code = """
result = engine.execute("insert into employee_of_month(emp_name) \
values(:empname)", empname = 'fred')
result = engine.execute("select * from employee_of_month")
print(result.fetchall())
"""
heading = "The execute() method auto commits for statements like INSERT, UPDATE\
 DELETE."
print_output(number,code,heading)

result = engine.execute("insert into employee_of_month(emp_name) \
values(:empname)", empname = 'fred')
result = engine.execute("select * from employee_of_month")
print(result.fetchall())
result.close()

input("\nEnter to continue...")

################################################################################

#6
#Demonstrating using the engine.connect() to control the scope of the
#connection and execute a transaction using begin() method of connect object.
number += 1
code = """
connection = engine.connect()
transaction = connection.begin()
connection.execute("insert into employee (emp_name) values (:emp_name)",\
emp_name = 'wendy' )
connection.execute("update employee_of_month set emp_name = :emp_name", \
emp_name = 'wendy')
transaction.commit()
connection.close()


result = engine.execute("select * from employee")
print(result.fetchall())
result = engine.execute("select * from employee_of_month")
print(result.fetchall())
"""
heading = "Demonstrating using the engine.connect() to control the scope of\n\
the connection and execute a transaction using begin() method of connect\n\
object."
print_output(number,code,heading)

connection = engine.connect()
transaction = connection.begin()
connection.execute("insert into employee (emp_name) values (:emp_name)",\
emp_name = 'wendy' )
connection.execute("update employee_of_month set emp_name = :emp_name", \
emp_name = 'wendy')
transaction.commit()
connection.close()

result = engine.execute("select * from employee")
print(result.fetchall())
result = engine.execute("select * from employee_of_month")
print(result.fetchall())

input("\nEnter to continue...")

################################################################################

print("NOTE: RESET YOUR GIT : git checkout -- engine.db")
