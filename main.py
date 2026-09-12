from fastapi import FastAPI

# Create the FastAPI application
app = FastAPI()

# Home route
@app.get("/")
def home():
    return {
        "message": "My FastAPI project is working"
    }

# Student route
@app.get("/student")
def student():
    return {
        "name": "Abdul Saboor",
        "course": "Python"
    }
