

from invoke import task

from fanfic.services import config
from fanfic.models import Base


engine = config.build_sqla_engine()


@task
def init_db(ctx):
    """Create database tables.
    """
    Base.metadata.create_all(engine)


@task
def reset_db(ctx):
    """Drop and recreate database tables.
    """
    Base.metadata.drop_all(engine)

    init_db(ctx)
