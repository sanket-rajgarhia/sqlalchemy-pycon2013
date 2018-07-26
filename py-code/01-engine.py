import os
from sqlalchemy import create_engine

#Function to print heading and code
def print_output(number,code,heading):
    os.system('clear')
    number_print = "\nNo {}.".format(number)
    print(number_print)
    print("_"*len(number_print))
    print("{}".format(code).rstrip('\n'))
    print("\n{}".format(heading))
    print("-"*len(heading))
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

input("\nEnter to continue...")

################################################################################

#3
#Demonstrating that result is iterable.
number += 1
code = """
result = engine.execute("select * from employee")
for row in result:
    print(row)
"""
heading = "The object 'result' is iterable."
print_output(number, code, heading)

#Code
result = engine.execute("select * from employee")
for row in result:
    print(row)

input("\nEnter to continue...")

################################################################################

#4
#Demonstrating fetchall() to fetch a list
number += 1
code = """
result = engine.execute("select * from employee")
print(result.fetchall())
"""
heading = "Demonstrating - fetchall() returns a list of rows"
print_output(number,code,heading)

result = engine.execute("select * from employee")
print(result.fetchall())

input("\nEnter to continue...")

################################################################################
