import os
import databases
import orm
# this is in here because we'll import this file at the very start
from dotenv import load_dotenv
load_dotenv()

database = databases.Database('sqlite:///' + os.environ.get('DATABASE_PATH'))
models = orm.ModelRegistry(database)
