from sqlalchemy import Column, BigInteger, String, sql, ForeignKey
from utils.db_api.db_gino import TimedBaseModel

class Turtle(TimedBaseModel):
    __tablename__ = 'turtles'
    turtle_id = Column((BigInteger),primary_key =True)
    weight = Column(String(120)) # Column(BigInteger) # критичность проёба
    user_id = Column(BigInteger) # Кому дали черепаху
    issuer_id = Column(BigInteger, ForeignKey('users.user_id')) # Кто дал черепаху
    admin_id = Column(BigInteger, ForeignKey('users.user_id')) # Кто одобрил/отклонил черепаху
    status = Column(String(12)) # WAIT, REJECTED, ACTIVE
    comm = Column(String(255)) # За что дали черепаху
    protest = Column(String(255)) # Комментарий для протеста черепахи

    query: sql.select

    def return_turtle_id(self):
         return self.turtle_id