
# 🧠 AI-Powered Q&A Web App

This is a simple question–answer web application that demonstrates Full-Stack development skills with integration of generative AI via Azure OpenAI or a free alternative.

---

## 🚀 Technologies Used

* Python 3.11
* FastAPI
* Azure OpenAI (via `openai` SDK)
* HTML + JS (via `StaticFiles`)
* CSV as a knowledge base
* pytest / flake8
* Optional: Docker

---

## ⚙️ Installation

1. Clone the repository:

```bash
git clone https://github.com/RuslanRiabokin/RuslanRiabokin-Test_Task_AI_Enabled_Web_Application
````

2. Create and activate a virtual environment:

```bash
python -m venv venv
venv\Scripts\activate     # Windows
source venv/bin/activate  # Linux/macOS
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🧠 AI Provider Setup

This app supports two AI backends:

* **Azure OpenAI** – production-grade provider
* **OpenRouter.ai** – free and OpenAI-compatible

You can switch between them using the `.env` file.

---

### 🔷 Option 1 — Azure OpenAI

1. Set the following in your `.env` file:

```
USE_OPENROUTER=False

AZURE_OPENAI_KEY=your-azure-key
AZURE_OPENAI_ENDPOINT=https://your-azure-endpoint.openai.azure.com
AZURE_OPENAI_DEPLOYMENT_ID=your-deployment-id
```

> Requires Azure OpenAI access (paid)

---

### 🟢 Option 2 — OpenRouter (Free)

1. Get your free API key at:
   👉 [https://openrouter.ai/settings](https://openrouter.ai/settings)

2. Set the following in your `.env` file:

```
USE_OPENROUTER=True

OPENROUTER_API_KEY=your-openrouter-key
OPENROUTER_BASE_URL=https://openrouter.ai/api/v1
OPENROUTER_MODEL=mistralai/mistral-7b-instruct:free
```

> ✅ No credit card required
> ⚠️ May be rate-limited during high load

---

### 🔄 Switching Providers

To switch between AI providers:

* `USE_OPENROUTER=True` → OpenRouter (free)
* `USE_OPENROUTER=False` → Azure OpenAI

No code changes needed — just restart the app after editing `.env`.

---

## ▶️ Running the Application

### Backend:

```bash
uvicorn main:app --reload
```

The API will be available at:
[http://127.0.0.1:8000](http://127.0.0.1:8000)

### UI:

The simple HTML interface is accessible directly at:
[http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## 🧪 Testing

```bash
# Run tests from project root
python -m pytest
```

The following components are tested:

* The knowledge base search function (`search_faq`)
* The `/api/ask` API endpoint

---

## 🧠 How It Works

1. The user enters a question.
2. A phrase-based search is performed against the knowledge base (`faq.csv`).
3. Matched entries are used as context for the selected AI provider.
4. The model generates an answer based on the context.
5. The answer is returned and displayed in the UI.

---

## 🐳 Docker Deployment

You can also run the application inside a Docker container.

### 1. Build the Docker image

```bash
docker build -t qa-app .
```

### 2. Run the container

```bash
docker run --name qa-app-container -p 8000:8000 --env-file .env qa-app
```

Then visit:
[http://localhost:8000](http://localhost:8000)

---

## 📄 License

MIT — Free to use for educational and demo purposes.

```

