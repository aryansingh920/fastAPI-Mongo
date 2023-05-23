#!/bin/bash

# Set the MongoDB URI as an environment variable
export MONGO_URI="mongodb+srv://hmsteam3infosys:hmsteam3infosys@cluster0.ixtp3tq.mongodb.net/?retryWrites=true&w=majority"

pip install -r "requirements.txt"

# Run the FastAPI server with uvicorn
uvicorn main:app --host 0.0.0.0 --port 8000
