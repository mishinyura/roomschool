from sqlalchemy import inspect
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from app.models.base_model import Base
from app.core.config import settings

engine = create_async_engine(
    url=settings.db.get_url,
    echo=True
)

session_maker = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)


async def get_session() -> AsyncSession:
    async with session_maker() as session:
        yield session


async def create_tables():
    async with engine.begin() as conn:
        inspector = await conn.run_sync(lambda conn: inspect(conn))

        existing_tables = await conn.run_sync(lambda _: inspector.get_table_names())

        # Проверяем нужные таблицы
        needed_tables = Base.metadata.tables.keys()

        tables_to_create = [
            table for table in needed_tables if table not in existing_tables
        ]

        if tables_to_create:
            await conn.run_sync(
                lambda conn: Base.metadata.create_all(
                    conn,
                    tables=[Base.metadata.tables[table] for table in tables_to_create],
                )
            )
            print(f"Created tables: {tables_to_create}")
        else:
            print("All tables already exist")