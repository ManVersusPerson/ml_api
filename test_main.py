from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "To translate text, go to /predict"}


def test_translate_t0_eng_1():
    response = client.post("/predict/",
        json={"text": "Привет. Как дела?"}
    )
    json_data = response.json() 
    assert response.status_code == 200
    assert json_data['translation_text'] == "Hey, how's it going?"

def test_translate_t0_eng_2():
    response = client.post("/predict/",
        json={"text": "Симфония «Жизнь» — неоконченное произведение Петра Чайковского, над которым он, предположительно, работал в 1890 или 1891 году. К Симфонии «Жизнь» принято относить два листка с текстовыми надписями и связанными с ними нотными набросками, сделанными композитором. Искусствоведы сходятся во мнении, что они соотносятся со временем создания секстета для струнных инструментов «Воспоминание о Флоренции» Чайковского."}
    )
    json_data = response.json() 
    assert response.status_code == 200
    assert json_data['translation_text'] == 'The \"Life\" symphony is an unfinished work by Peter Chaikovsky, on which he allegedly worked in 1890 or 1891. It is customary for the \"Life\" symphony to carry two leaves with text inscriptions and related notes by the composer, and the artists agree that they relate to the time of creating a sextete for the string tools \"Remembering Florence\" of Chaikovsky.'

def test_translate_t0_ru_1():
    response = client.post("/predict/",
        json={"text": "Science is fascinating!"}
    )
    json_data = response.json() 
    assert response.status_code == 200
    assert json_data['translation_text'] == "Наука очаровательна!"

def test_translate_t0_ru_2():
    response = client.post("/predict/",
        json={"text": "From the ancient world (at least since Aristotle) until the 19th century, natural philosophy was the common term for the study of physics (nature), a broad term that included botany, zoology, anthropology, and chemistry as well as what we now call physics."}
    )
    json_data = response.json() 
    assert response.status_code == 200
    assert json_data['translation_text'] == "С древних времен (по крайней мере с Аристотеля) до XIX века естественная философия была общим термином для изучения физики (природы), широким термином, который включал ботанику, зоологию, антропологию и химию, а также то, что мы сейчас называем физикой."