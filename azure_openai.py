from openai import AzureOpenAI

from config import AZURE_OPENAI_KEY, AZURE_OPENAI_ENDPOINT, AZURE_OPENAI_DEPLOYMENT_ID

client = AzureOpenAI(
    api_key=AZURE_OPENAI_KEY,
    api_version="2024-02-01",
    azure_endpoint=AZURE_OPENAI_ENDPOINT,
)


async def generate_answer_with_openai(context: str, question: str) -> str:
    system_prompt = ("Ти — помічник, який відповідає на запитання на основі наданого контексту. "
                     "Не вигадуй інформацію.")

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": f"Контекст:\n{context}\n\nПитання: {question}"}
    ]

    try:
        response = client.chat.completions.create(
            model=AZURE_OPENAI_DEPLOYMENT_ID,
            messages=messages
        )
        return response.choices[0].message.content.strip()

    except Exception as e:
        return f"❌ Помилка під час звернення до Azure OpenAI: {str(e)}"
