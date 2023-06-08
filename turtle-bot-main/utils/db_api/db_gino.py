import datetime
import sqlalchemy as sa
from typing import List
from aiogram import Dispatcher
import data.config
from gino import Gino

db = Gino()

class BaseModel(db.Model):
    __abstract__ = True

    def str(self):
        model = self.__class__.__name__
        table: sa.Table = sa.inspect(self.__class__)
        primary_key_columns: List[sa.Column] = table.primary_key.columns
        values = {
            column.name: getattr(self, self._column_name_map[column.name])
            for column in primary_key_columns
        }
        values_str = " ".join(f"{name}={value!r}" for name, value in values.items())
        return f"<{model} {values_str}>"


class TimedBaseModel(BaseModel):
    __abstract__ = True
    presentTime = datetime.datetime.now()
    created_at = db.Column(sa.DateTime(False), server_default=sa.func.now())


async def on_startup(dispatcher: Dispatcher):
    print('установка связи с postgresql')
    await db.set_bind(data.config.POSTGRES_URI)