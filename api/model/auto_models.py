from sqlalchemy.ext.automap import automap_base
from sqlalchemy import create_engine
from api.config import settings

Base = automap_base()

engine = create_engine(settings.DB_URL)

Base.prepare(engine, reflect=True)

users = Base.classes.users
memos = Base.classes.memos