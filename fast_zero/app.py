from fastapi import FastAPI, HTTPException, status
from fastapi.responses import HTMLResponse

from fast_zero.schemas import Message, UserDB, UserList, UserPublic, UserSchema

app = FastAPI(
    title='FastAPI do Zero',
    description='Uma API de exemplo criada com FastAPI',
    version='1.0.0',
)

database = []

@app.get('/', status_code=status.HTTP_200_OK, response_model=Message)
def read_root():
    return {
        'message': 'Bem-vindo à API FastAPI do Zero!',
        'docs_url': '/docs',
        'redoc_url': '/redoc',
    }

@app.get(
    '/hello-world',
    response_class=HTMLResponse,
)
def hello_world():
    html_content = """
    <!DOCTYPE html>
    <html>
        <head>
            <title>Hello World</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    margin: 0;
                    background-color: #f0f2f5;
                }
                h1 {
                    color: #1a73e8;
                    text-align: center;
                    padding: 20px;
                    border-radius: 8px;
                    background-color: white;
                    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
                }
            </style>
        </head>
        <body>
            <h1>Hello World!</h1>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content)


@app.post(
    '/users/', status_code=status.HTTP_201_CREATED, response_model=UserPublic
)
def create_user(user: UserSchema):
    user_with_id = UserDB(**user.model_dump(), id=len(database) + 1)
    database.append(user_with_id)
    return user_with_id


@app.get('/users/', response_model=UserList)
def read_user():
    return {'users': database}


@app.get('/users/{user_id}', response_model=UserPublic)
def read_single_user(user_id: int):
    if user_id > len(database) or user_id < 1:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail='User Not Found'
        )

    user_with_id = database[user_id - 1]
    return user_with_id


@app.put('/users/{user_id}', response_model=UserPublic)
def update_user(user_id: int, user: UserSchema):
    if user_id > len(database) or user_id < 1:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail='User Not Found'
        )

    user_with_id = UserDB(**user.model_dump(), id=user_id)
    database[user_id - 1] = user_with_id

    return user_with_id


@app.delete('/users/{user_id}', response_model=Message)
def delete_user(user_id: int):
    if user_id > len(database) or user_id < 1:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail='User Not Found'
        )

    del database[user_id - 1]

    return {
        'message': 'User deleted',
        'docs_url': '/docs',
        'redoc_url': '/redoc',
    }
