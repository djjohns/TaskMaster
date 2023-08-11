import motor.motor_asyncio
from model import Task



client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://localhost:27017/')
database = client.TaskList
collection = database.task

async def fetch_one_task(task_id):
    document = await collection.find_one({"task_id": task_id})
    return document

async def fetch_all_tasks():
    tasks = []
    cursor = collection.find({})
    async for document in cursor:
        document["task_id"] = str(document["task_id"])
        tasks.append(Task(**document))
    return tasks

async def create_task(task):
    document = task
    result = await collection.insert_one(document)
    return document

async def update_task(task_id, complete):
    await collection.update_one({"task_id": task_id}, {"$set": {"complete": complete}})
    document = await collection.find_one({"task_id": task_id})
    return document

async def remove_task(task_id):
    await collection.delete_one({"task_id": task_id})
    return True
