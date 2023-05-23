#!/bin/bash

# Set the MongoDB URI as an environment variable
export MONGO_URI="mongodb+srv://<username>:<password>@<cluster>?retryWrites=true&w=majority"

pip install -r "requirements.txt"

# Run the FastAPI server with uvicorn
uvicorn main:app --host 0.0.0.0 --port 8000
