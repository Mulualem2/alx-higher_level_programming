#!/usr/bin/python3
"""
Adds the State object "Louisiana" to the database hbtn_0e_6_usa.
Usage: ./11-model_state_insert.py <mysql username> /
                                  <mysql password> /
                                  <database name>
"""
if __name__ == '__main__':
    from sys import argv
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    if len(argv) != 4:
        print("error")
    else:
        USER = argv[1]
        PASS = argv[2]
        DB = argv[3]
        engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                               .format(USER, PASS, DB), pool_pre_ping=True)
        Session = sessionmaker(bind=engine)
        session = Session()
        add_state = State(name='Louisiana')
        session.add(add_state)
        session.commit()
        print(add_state.id)
