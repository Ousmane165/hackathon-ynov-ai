import os
import requests

OLLAMA_URL = os.getenv("OLLAMA_URL", "http://localhost:11434")

try:
    response = requests.get(f"{OLLAMA_URL}/api/tags", timeout=5)
    response.raise_for_status()
    print("OK - Ollama est disponible")
    print(response.json())
except Exception as exc:
    print("ERREUR - Ollama indisponible")
    print(exc)
    raise SystemExit(1)
