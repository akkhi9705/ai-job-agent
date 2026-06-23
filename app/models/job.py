from sqlalchemy import (
    MetaData,
    Table,
    Column,
    Integer,
    String,
    Text
)

metadata = MetaData()

jobs = Table(
    "jobs",
    metadata,

    Column("id", Integer, primary_key=True),

    Column("company", String),

    Column("title", String),

    Column("location", String),

    Column("jd", Text),

    Column("apply_link", String),

    Column("source", String)
)