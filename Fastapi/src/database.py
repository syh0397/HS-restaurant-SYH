from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#Creates database engine  pool 관리
engine = create_engine('sqlite:///todo.db')

#ORM에서는 처음에 데이터베이스 테이블을 써먹을 수 있게 설정한 다음 직접 정의한 클래스에 맵핑을 해야한다. 
# qlalchemy에서는 두가지가 동시에 이뤄지는데 Declarative 란걸 이용해 클래스를 생성하고 실제 디비 테이블에 연결을 한다.
Base = declarative_base()

# sessionmaker는 sqlalchemy에서 제공하는 class로 
# session을 만들어 주는 factory라고 생각하면 될 것 같다. 
# 일반적으로 sessionmaker를 db 엔진과 연결한 후 session을 생성한다.
SessionLocal = sessionmaker(bind=engine, expire_on_commit=False)