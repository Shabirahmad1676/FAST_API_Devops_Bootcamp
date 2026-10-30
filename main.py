from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI on EC2!"}

@app.get("/f4")
def feature_four():
    return {"message": "FastAPI Feature-4 endpoint working!"}


    