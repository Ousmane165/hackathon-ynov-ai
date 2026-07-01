import os
import requests

OLLAMA_URL = os.getenv("OLLAMA_URL", "http://localhost:11434")
MODEL = os.getenv("OLLAMA_MODEL", "phi35-financial")

prompts = [
    "Explique la différence entre chiffre d'affaires et bénéfice.",
    "Analyse le risque d'une forte croissance avec faible trésorerie.",
    "Quels KPI financiers suivre pour une PME ?",
]

for prompt in prompts:
    response = requests.post(
        f"{OLLAMA_URL}/api/chat",
        json={
            "model": MODEL,
            "messages": [{"role": "user", "content": prompt}],
            "stream": False,
            "options": {"temperature": 0.3},
        },
        timeout=120,
    )
    response.raise_for_status()
    data = response.json()
    print("PROMPT:", prompt)
    print("REPONSE:", data.get("message", {}).get("content", ""))
    print("-" * 80)
