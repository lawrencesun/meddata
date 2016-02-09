from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
data = Table('data', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('systolic_pressure', Integer, default=ColumnDefault(0)),
    Column('diastolic_pressure', Integer, default=ColumnDefault(0)),
    Column('cardiac_rate', Integer, default=ColumnDefault(0)),
    Column('timestamp', DateTime),
    Column('user_id', Integer),
    Column('body', String(length=240)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['data'].columns['body'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['data'].columns['body'].drop()
