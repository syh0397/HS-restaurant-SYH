from fastapi import FastAPI
from pydantic import BaseModel, validator

from utils.functions import calculate

class CalParam(BaseModel):
    cal_type: str
    a: int
    b: int

    @validator('cal_type')
    def check_calculate_type(cls, v):
        if v not in ['더하기', '빼기', '곱하기', '나누기']:
            raise ValueError('cal_type must be one of "addition", "subtraction", "multiplication, or "division".')
        return v

    @validator('b')
    def check_zero_division(cls, v, values):
        if values.get('cal_type') == '나누기' and v == 0:
            raise ValueError('b must not be zero.')
        return v

app = FastAPI()

# app은 server application 
# @ 뒤에 app.get 과 url 경로를 입력한 후 함수를 만들면 바로 구현이 가능하다.
@app.get('/')
def read_root():
    return {
        'result': '설유환의 첫번째 Fast API 작품입니다.',
    }


@app.post('/calculator/')
def calculator(param: CalParam):
    return {
        'result': calculate(param.a, param.b, param.cal_type)
    }



# uvicorn main:app --reload 명령어로 실행함 
# reload 옵션은 코드를 수정할 때마다 바로바로 서버에 반영되는 옵션
