from fastapi import FastAPI
from transformers import pipeline
from pydantic import BaseModel
import uvicorn


class Item(BaseModel):
        text: str


app = FastAPI()
classifier_en_ru = pipeline("translation_en_to_ru",
                        model = "Helsinki-NLP/opus-mt-en-ru")

classifier_ru_en = pipeline("translation_ru_to_en",
                        model = "Helsinki-NLP/opus-mt-ru-en")


@app.get("/")
def root():
	return {"message":"To translate text, go to /predict"}

@app.post("/predict/")
def predict(item: Item):
	count = 0
	dict = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
	for it in item.text:
		if it in dict:
			count += 1
			
	if count / (len(str(item.text))) * 100 > 65:
		return classifier_en_ru(item.text)[0]
	else:
		return classifier_ru_en(item.text)[0]

if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=8080, log_level="info")
