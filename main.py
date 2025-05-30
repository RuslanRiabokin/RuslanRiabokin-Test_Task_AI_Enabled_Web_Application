from fastapi import FastAPI
from pydantic import BaseModel
from faq_loader import load_faq_csv, search_faq
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os


app = FastAPI()
faq_list = load_faq_csv()

# Модель запиту від користувача
class QuestionRequest(BaseModel):
    question: str

# Модель відповіді
class AnswerResponse(BaseModel):
    answer: str

@app.post("/api/ask", response_model=AnswerResponse)
async def ask_question(request: QuestionRequest):
    matches = search_faq(request.question, faq_list)
    if matches:
        # Повертаємо першу знайдену відповідь
        return {"answer": matches[0].answer}
    else:
        return {"answer": "Вибач, я не знайшов відповіді у базі знань."}


# Підключення папки зі статичними файлами
app.mount("/static", StaticFiles(directory="static"), name="static")

# Віддавати index.html при заході на корінь
@app.get("/")
async def read_index():
    return FileResponse(os.path.join("static", "index.html"))
