from sqlalchemy import Column, BigInteger, String, sql, Integer

from utils.db_api.db_gino import TimedBaseModel


class User(TimedBaseModel):
    __tablename__ = 'users'
    user_id = Column(BigInteger, primary_key=True)
    username = Column(String(50)) # никнейм
    status = Column(String(50)) # WAIT, ACTIVE
    role = Column(String(10)) # admin, user
    name = Column(String(30)) #  Имя
    surname = Column(String(30)) # Фамилия

    query: sql.select

    def return_user_id(self):
         return self.name, self.surname, self.user_id

    def return_user_role(self):
        return self.role

    def return_user_status(self):
        return self.status
