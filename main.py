from fastapi import FastAPI
from pydantic import BaseModel
from faq_loader import load_faq_csv, search_faq
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os
from azure_openai import generate_answer_with_openai


app = FastAPI()
faq_list = load_faq_csv()


# Модель запиту від користувача
class QuestionRequest(BaseModel):
    """
        Request model representing a user question.
        """
    question: str


# Модель відповіді
class AnswerResponse(BaseModel):
    """
        Response model containing the AI-generated answer.
        """
    answer: str


@app.post("/api/ask", response_model=AnswerResponse)
async def ask_question(request: QuestionRequest):
    """
        Handle POST request to /api/ask.

        Performs a search in the FAQ list for related answers,
        uses matched entries as context for Azure OpenAI,
        and returns the generated answer.

        Args:
            request (QuestionRequest): The incoming user question.

        Returns:
            dict: A dictionary with a single key 'answer'.
        """
    matches = search_faq(request.question, faq_list)

    # Формуємо контекст: або відповіді з бази, або заглушку
    if matches:
        context = "\n".join(f"• {entry.question} — {entry.answer}" for entry in matches)
    else:
        context = "Немає відповідного запису в базі знань."

    # Отримуємо відповідь від OpenAI
    answer = await generate_answer_with_openai(context, request.question)
    return {"answer": answer}


# Підключення папки зі статичними файлами
app.mount("/static", StaticFiles(directory="static"), name="static")


# Віддавати index.html при заході на корінь
@app.get("/")
async def read_index():
    """
        Serve the HTML user interface from /static/index.html when accessing the root URL.
        """
    return FileResponse(os.path.join("static", "index.html"))
