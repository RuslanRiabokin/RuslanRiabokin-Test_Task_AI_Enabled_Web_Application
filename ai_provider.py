from config import (
    USE_OPENROUTER,
    AZURE_OPENAI_KEY, AZURE_OPENAI_ENDPOINT, AZURE_OPENAI_DEPLOYMENT_ID,
    OPENROUTER_API_KEY, OPENROUTER_BASE_URL, OPENROUTER_MODEL,
)

from openai import AzureOpenAI, OpenAI


if USE_OPENROUTER:
    client = OpenAI(
        api_key=OPENROUTER_API_KEY,
        base_url=OPENROUTER_BASE_URL,
    )
    model = OPENROUTER_MODEL
else:
    client = AzureOpenAI(
        api_key=AZURE_OPENAI_KEY,
        api_version="2024-02-01",
        azure_endpoint=AZURE_OPENAI_ENDPOINT,
    )
    model = AZURE_OPENAI_DEPLOYMENT_ID


async def generate_answer_with_openai(context: str, question: str) -> str:
    """
    Generate an AI-based answer using either Azure OpenAI or OpenRouter (fallback).
    """
    system_prompt = (
        "Ти — помічник, який відповідає на запитання на основі наданого контексту. "
        "Не вигадуй інформацію."
    )

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": f"Контекст:\n{context}\n\nПитання: {question}"}
    ]

    try:
        response = client.chat.completions.create(
            model=model,
            messages=messages
        )
        return response.choices[0].message.content.strip()

    except Exception as e:
        return f"❌ AI error: {str(e)}"
