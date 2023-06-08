from sqlalchemy import Column, BigInteger, String, sql, ForeignKey
from utils.db_api.db_gino import TimedBaseModel

class like(TimedBaseModel):
    __tablename__ = 'like'
    like_id = Column((BigInteger),primary_key =True)
    user_id = Column(BigInteger) # Кому дали черепаху
    issuer_id = Column(BigInteger, ForeignKey('users.user_id')) # Кто дал лайк
    admin_id = Column(BigInteger, ForeignKey('users.user_id')) # Кто одобрил/отклонил лайк
    status = Column(String(12)) # WAIT, REJECTED, ACTIVE
    comm = Column(String(255)) # За что дали лайк

    query: sql.select

    def return_like_id(self):
         return self.like_id