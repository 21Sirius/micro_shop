
from fastapi import FastAPI
import uvicorn
from pydantic import EmailStr, BaseModel

from items_views import router as items_router


app = FastAPI()
app.include_router(items_router)


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




if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)
