from sqlalchemy import create_engine

#engine is a factory for database connections.
engine = create_engine("sqlite:///engine.db")

################################################################################

#Demonstrating the execute() method to get the result of the query.
#and also using fetchone() on the result.
result = engine.execute("select emp_id, emp_name from employee "
                        "where emp_id=:empid", empid = 3)
row = result.fetchone()
result.close()

################################################################################

code = """
result = engine.execute("select emp_id, emp_name from employee "
                        "where emp_id=:empid", empid = 3)
row = result.fetchone()
"""
heading = "Accessing 'row'"
print("\n" + code )
print("\n" + heading)
print("-"*len(heading))
print("row : {}".format(row))
print("row['emp_name'] : {}".format(row['emp_name']))
print("row.emp_name : {}".format(row.emp_name))

input("\nEnter to continue...")

################################################################################
