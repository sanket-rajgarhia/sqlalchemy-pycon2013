import os
from termcolor import colored, cprint

from sqlalchemy.ext.declarative import declarative_base

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
#Creating the 'Declarative Base'.
number = 1
code = """
Base = declarative_base()
print(Base.metadata)
"""
heading = "#Creating the 'Declarative Base'."
print_output(number,code,heading)

Base = declarative_base()
print(Base.metadata)

input("\nEnter to continue...")

################################################################################
