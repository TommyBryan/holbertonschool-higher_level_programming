#!/usr/bin/python3
"""
Prints the State id with the name passed as argument from the database hbtn_0e_6_usa
Usage: ./10-model_state_my_get.py <mysql username> <mysql password> <database name> <state name>
If not found, prints "Not found"
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    username, password, db_name, state_name = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]

    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}',
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the State with the exact name
    state = session.query(State).filter(State.name == state_name).first()

    if state:
        print(state.id)
    else:
        print("Not found")

    session.close()
