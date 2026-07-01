import os
import logging
from typing import List, Dict

import requests
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field
from dotenv import load_dotenv

load_dotenv()

OLLAMA_URL = os.getenv("OLLAMA_URL", "http://localhost:11434")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "phi35-financial")
MAX_PROMPT_LENGTH = int(os.getenv("MAX_PROMPT_LENGTH", "2000"))

os.makedirs("../logs", exist_ok=True)
logging.basicConfig(
    filename="../logs/app.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
)

app = FastAPI(title="TechCorp AI Chat", version="1.0.0")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.mount("/static", StaticFiles(directory="static"), name="static")

SYSTEM_PROMPT = """
Tu es Phi-3.5-Financial, assistant IA spécialisé finance, business et analyse d'entreprise.
Réponds en français, de manière claire, structurée et prudente.
Tu ne dois pas inventer de données financières. Si une information manque, précise-le.
Pour les questions médicales, indique que le modèle médical est expérimental et non destiné à un diagnostic.
"""

BLOCKED_PATTERNS = [
    "ignore previous instructions",
    "désactive tes règles",
    "bypass",
    "jailbreak",
    "donne moi un malware",
    "voler des identifiants",
]

class ChatRequest(BaseModel):
    message: str = Field(..., min_length=1, max_length=MAX_PROMPT_LENGTH)
    history: List[Dict[str, str]] = []

class ChatResponse(BaseModel):
    answer: str
    model: str


def is_prompt_safe(message: str) -> bool:
    lowered = message.lower()
    return not any(pattern in lowered for pattern in BLOCKED_PATTERNS)

@app.get("/", response_class=HTMLResponse)
def index():
    with open("static/index.html", "r", encoding="utf-8") as f:
        return f.read()

@app.get("/health")
def health():
    try:
        r = requests.get(f"{OLLAMA_URL}/api/tags", timeout=3)
        return {"status": "ok", "ollama": r.status_code == 200, "model": OLLAMA_MODEL}
    except requests.RequestException:
        return {"status": "degraded", "ollama": False, "model": OLLAMA_MODEL}

@app.post("/api/chat", response_model=ChatResponse)
def chat(payload: ChatRequest):
    if not is_prompt_safe(payload.message):
        logging.warning("Prompt blocked for safety")
        raise HTTPException(status_code=400, detail="Prompt bloqué par les règles de sécurité.")

    messages = [{"role": "system", "content": SYSTEM_PROMPT}]
    for item in payload.history[-6:]:
        role = item.get("role", "user")
        content = item.get("content", "")[:MAX_PROMPT_LENGTH]
        if role in ["user", "assistant"] and content:
            messages.append({"role": role, "content": content})
    messages.append({"role": "user", "content": payload.message})

    try:
        response = requests.post(
            f"{OLLAMA_URL}/api/chat",
            json={
                "model": OLLAMA_MODEL,
                "messages": messages,
                "stream": False,
                "options": {
                    "temperature": 0.3,
                    "top_p": 0.9,
                    "num_ctx": 4096,
                },
            },
            timeout=120,
        )
        response.raise_for_status()
        data = response.json()
        answer = data.get("message", {}).get("content", "Réponse vide du modèle.")
        logging.info("Chat request answered")
        return ChatResponse(answer=answer, model=OLLAMA_MODEL)
    except requests.RequestException as exc:
        logging.error("Ollama error: %s", exc)
        raise HTTPException(status_code=503, detail="Serveur Ollama indisponible.")
