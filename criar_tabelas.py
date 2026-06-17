from sqlalchemy import inspect
from banco import engine

insp = inspect(engine)

print(insp.get_table_names())
