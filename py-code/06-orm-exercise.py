import os
from termcolor import colored, cprint

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import Column, ForeignKey
from sqlalchemy import String, Integer, Float
from sqlalchemy.orm import Session, relationship
from sqlalchemy import func

#Restore the state of orm-exercise.db - prior to run
os.system('git checkout -- orm-exercise.db')

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

#1 ORM Exercise.
number = 1
code = """
"""
heading = "ORM Exercise."
print_output(number,code,heading)

print("Setting up the engine")
engine = create_engine("sqlite:///orm-exercise.db")

print("Setting up the Base class")
Base = declarative_base()

print("Defining the Account Table")
class Account(Base):
    __tablename__ = 'account'

    id = Column(Integer, primary_key = True)
    owner = Column(String(50), nullable = False)
    balance = Column(Float, default = 0)

    def __repr__(self):
        return "(<Account %r %r >)" % (self.owner, self.balance)

print("Defining the Transaction Table")
class Transaction(Base):
    __tablename__ = 'transaction'

    id = Column(Integer, primary_key = True)
    amount = Column(Float, default = 0)
    account_id = Column(Integer, ForeignKey(Account.id))

    account = relationship("Account", backref="transactions")

    def __repr__(self):
        return "<Transaction %r %r" % (self.amount, self.account_id)

print("Creating the Tables in the Database.")
Base.metadata.create_all(engine)

print("Creating a session.")
session = Session(engine)

print("Inserting rows in 'accounts'")
session.add_all([
                    Account(owner = 'Jack Jones', balance = 5000),
                    Account(owner = 'Ed Rendell', balance = 10000)
                ])
session.commit()

print("Updating Accounts with transactions")
owner_jack = session.query(Account).filter_by(owner = 'Jack Jones').one()
owner_jack.transactions = [
                            Transaction(amount = 500),
                            Transaction(amount = 4500)
                          ]

owner_ed = session.query(Account).filter_by(owner = 'Ed Rendell').one()
owner_ed.transactions = [
                            Transaction(amount = 6000),
                            Transaction(amount = 4000)
                        ]
session.commit()

print("Report")
accounts = session.query(Account).all()
totals = session.query(Transaction.account_id,func.sum(Transaction.amount).\
                      label("total")).\
                      group_by(Transaction.account_id)
for account in accounts:
    print("Owner : {} ({})".format(account.owner, account.id))
    print("Balance : {}".format(account.balance))
    print("-" * 80)
    for transaction in account.transactions:
        print(transaction.amount)
    for total in totals:
        if total.account_id == account.id:
            print("********************")
            print("Total : {}".format(total.total))
            break
    print("-" * 80)
input("\nEnter to continue...")

################################################################################

os.system('clear')
print("\n"* 5)
cprint("END".rjust(38, " "), 'blue', attrs=['bold'])
heading = "NOTE: RESET YOUR GIT : git checkout -- orm-exercise.db"
heading = heading.rjust(( len(heading) + ((80 - len(heading)) // 2)), " ")
cprint('{}'.format(heading), 'red', attrs=['blink','bold'])
print("\n"* 5)
