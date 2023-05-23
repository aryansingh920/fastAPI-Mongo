from fastapi import FastAPI
from pymongo import MongoClient
from models import Item
import os
app = FastAPI()

# MongoDB connection details
# Read the MongoDB URI from environment variable
MONGO_URI = os.getenv("MONGO_URI")



# Create a new client and connect to the server
client = MongoClient(MONGO_URI,tls=True)

collection = client["db"]["collection"]

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

@app.post("/items/")
def create_item(item: Item):
    item_data = {
        "name": item.name,
        "description": item.description
    }
    result = collection.insert_one(item_data)
    inserted_id = result.inserted_id
    return {"message": "Item created successfully", "item_id": str(inserted_id)}
