from fastapi import FastAPI
from transformers import pipeline
from pydantic import BaseModel

class Item(BaseModel):
        text: str


app = FastAPI()
classifier = pipeline("translation_en_to_ru",
                        model = "Helsinki-NLP/opus-mt-en-ru")


@app.get("/")
def root():
    return {"title":"Here will be our application"}

@app.post("/predict/")
def predict(item: Item):
	return classifier(item.text)[0]

