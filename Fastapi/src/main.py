from fastapi import FastAPI , Body, Depends
from pydantic import BaseModel, validator

from utils.functions import calculate
from utils import schemas
from utils import models

from database import Base, engine, SessionLocal
from sqlalchemy.orm import Session 


Base.metadata.create_all(engine)

def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()


class CalParam(BaseModel):
    cal_type: str
    a: int
    b: int

    @validator('cal_type')
    def check_calculate_type(cls, v):
        if v not in ['addition', 'subtraction', 'multiplication', 'division']:
            raise ValueError('cal_type must be one of "addition", "subtraction", "multiplication, or "division".')
        return v

    @validator('b')
    def check_zero_division(cls, v, values):
        if values.get('cal_type') == 'division' and v == 0:
            raise ValueError('b must not be zero.')
        return v
    
    # a가 0이고 b가 10이면 안되는 함수를 만들어보자 
    @validator('a')
    def check_zero_addition(cls, v):
        if  v == 10:
            raise ValueError('a must not be zero.')
        return v

app = FastAPI()


fakeDatabase = {
    1: {'task': 'Clean car'},
    2: {'task': 'Clean my room'},
    3: {'task': 'Clean my computer'},
}


# app은 server application 
# @ 뒤에 app.get 과 url 경로를 입력한 후 함수를 만들면 바로 구현이 가능하다.
@app.get('/')
def read_root():
    return {
        'result': '설유환의 첫번째 Fast API 작품입니다.',
    }

# 질의하는 함수 READ
def getItems(session: Session = Depends(get_session)):
    items = session.query(models.Item).all()
    return items


# ADD Data Create
@app.get("/{id}")
def getItem(id:int, session: Session = Depends(get_session)):
    item = session.query(models.Item).get(id)
    return item

# @app.get('/getitem/')
# def getItems():
#     return ['Item 1', 'Item 2', 'Item 3']


# ADD Data
#Option #2
@app.post("/")
def addItem(item:schemas.Item, session: Session = Depends(get_session)):
    item = models.Item(task = item.task)
    session.add(item)
    session.commit()
    session.refresh(item)

    return item


# Update Data
@app.put("/{id}")
def updateItem(id:int, item:schemas.Item, session: Session = Depends(get_session)):
    itemObject = session.query(models.Item).get(id)
    itemObject.task = item.task
    session.commit()
    return itemObject

# Deleting Data
@app.delete("/{id}")
def deleteItem(id:int, session: Session = Depends(get_session)):
    itemObject = session.query(models.Item).get(id)
    session.delete(itemObject)
    session.commit()
    session.close()
    return 'Item was deleted...'




@app.post('/calculator/')
def calculator(param: CalParam):
    return {
        'result': calculate(param.a, param.b, param.cal_type)
    }



# uvicorn main:app --reload 명령어로 실행함 
# reload 옵션은 코드를 수정할 때마다 바로바로 서버에 반영되는 옵션
