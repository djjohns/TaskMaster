from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from database import (
    fetch_one_task,
    fetch_all_tasks,
    create_task,
    update_task,
    remove_task,
)
from model import Task, UpdateTask



app = FastAPI()

origins = ['http://localhost:5173']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {
        "root": "I am groot!"
    }

@app.get("/api/task")
async def get_task():
    response = await fetch_all_tasks()
    return response

@app.get("/api/task/{task_id}", response_model=Task)
async def get_task_by_id(task_id):
    response = await fetch_one_task(task_id)
    if response:
        return response
    raise HTTPException(404, f"Can not get {task_id}. There is no TODO item with this {task_id}")

@app.post("/api/task", response_model=Task)
async def post_task(task:Task):
    response = await create_task(task.model_dump())
    if response:
        return response
    raise HTTPException(400, f"Something went wrong/Bad request.")

@app.put("/api/task/{task_id}", response_model=UpdateTask)
async def put_task(task_id:str, complete:bool):
    print("Received request for task_id:", task_id)
    print("Complete:", complete)
    response = await update_task(task_id, complete)
    if response:
        return response
    raise HTTPException(404, f"Can not update {task_id}. There is no TODO item with this {task_id}")

@app.delete("/api/task/{task_id}")
async def delete_task(task_id:str):
    response = await remove_task(task_id)
    if response:
        return "Successfully deleted item."
    raise HTTPException(404, f"Can not delete {task_id}. There is no TODO item with this {task_id}")



# if __name__ == "__main__":
#     uvicorn.run(
#         "main:app",
#         host=settings.HOST,
#         reload=settings.DEBUG_MODE,
#         port=settings.PORT,
#     )