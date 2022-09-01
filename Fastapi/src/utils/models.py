from sqlalchemy import Column, Integer, String
from database import Base 

# sqlite나 postgresql은 테이블을 생성할 때 varchar 컬럼을 길이를 설정하지 않아도 별 문제 없이 데이터타입으로 쓸 수 있지만 그 외 데이터베이스에서는 허용되지 않는다. 
# 그러므로 컬럼 길이가 필요한 데이터베이스의 경우 length가 필요하다.
class Item(Base):
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True)
    task = Column(String(256))

# Integer, Numeric 같은 경우에도 위와 동일하게 쓸 수 있다.

# 덧붙여 Firebird나 오라클에서는 PK를 생성할 때 sequence가 필요한데 Sequence 생성자를 써야 한다.