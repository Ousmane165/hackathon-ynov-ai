# Documentation de déploiement

## Déploiement local recommandé

1. Installer Ollama.
2. Créer le modèle `phi35-financial`.
3. Installer les dépendances Python.
4. Lancer FastAPI.
5. Ouvrir l'interface web.

```bash
ollama pull phi3.5
ollama create phi35-financial -f models/phi3_financial/Modelfile
cd webapp
pip install -r requirements.txt
uvicorn app:app --host 0.0.0.0 --port 8080
```

## Ports

| Service | Port |
|---|---:|
| Interface web / FastAPI | 8080 |
| Ollama | 11434 |
| Triton HTTP optionnel | 8000 |

## Variables

| Variable | Exemple | Rôle |
|---|---|---|
| OLLAMA_URL | http://localhost:11434 | URL serveur Ollama |
| OLLAMA_MODEL | phi35-financial | nom du modèle |
| MAX_PROMPT_LENGTH | 2000 | limite prompt |
