from sqlalchemy import create_engine

#engine is a factory for database connections.
engine = create_engine("sqlite:///engine.db")
