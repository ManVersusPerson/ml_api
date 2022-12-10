from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def root():
    return {"title":"Здесь будет наше приложение"}
