from typing import Annotated

from fastapi import FastAPI, Path
import uvicorn
from pydantic import EmailStr, BaseModel

app = FastAPI()


class CreateUser(BaseModel):
    email: EmailStr


@app.get('/')
def hello_index():
    return {
        'message': 'Hello Index',
    }


@app.get('/hello/')
def hello(name: str = 'World'):
    name = name.strip().title()
    return {'message': f'Hello {name}'}


@app.post('/users/')
def create_user(user: CreateUser):
    return {
        "message": 'succsess',
        "email": user.email
    }


@app.post('/calc/add/')
def add(a: int, b: int):
    return {
        'a': a,
        'b': b,
        'result': a + b,
    }


@app.get('/items/')
def list_items():
    return [
        'Item1',
        'Item2',
        'Item3',
    ]


@app.get('/items/latest/')
def get_latest_items():
    return {'item': {"id": 0, 'name': 'latest'}}


@app.get('/items/{item_id}/')
def get_item_by_id(item_id: Annotated[int, Path(ge=1)]):
    return {
        'item': {
            'id': item_id,
        },
    }


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)
