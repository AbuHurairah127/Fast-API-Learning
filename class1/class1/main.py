# fastapi_neon/main.py

from fastapi import FastAPI
from pydantic import BaseModel

class Todo(BaseModel):
    id:int
    title:str
    desc:str
    is_completed:bool

todos=[Todo(id=1,title="Write Code",desc="Write Code of FastAPIs to develop the todo application.",is_completed=False)]

app = FastAPI(title="Hello World API", 
    version="0.0.1",
    servers=[
        {
            "url": "http://0.0.0.0:8000", # ADD NGROK URL Here Before Creating GPT Action
            "description": "Development Server"
        }
        ])



@app.get("/testing")
def read_root():
    return {"message": "Hello World!"}

@app.get("/get-all-todos")
def get_all_todo():
    return todos

@app.post("/add-todo")
def add_todo(item:Todo):
    todos.append(item)
    return {"message": "Todo Added Successfully!"}

@app.get("/get-todo/{id}")
def get_todo(id:int):
    for dictionary in todos:
        if dictionary.id == id:
            return dictionary
    return None 
# @app.put("/get-todo/{id}")
# def get_todo(id:int):
#     for dictionary in todos:
#         if dictionary.id == id:
#             return dictionary
#     return None 