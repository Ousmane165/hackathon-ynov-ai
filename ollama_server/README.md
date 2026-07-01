# Serveur Ollama

## Démarrage

```bash
ollama serve
```

## Création du modèle financier

```bash
ollama pull phi3.5
ollama create phi35-financial -f ../models/phi3_financial/Modelfile
```

## Test API

```bash
curl http://localhost:11434/api/tags
```

## Test chat

```bash
curl http://localhost:11434/api/chat \
  -H "Content-Type: application/json" \
  -d '{"model":"phi35-financial","messages":[{"role":"user","content":"Explique le besoin en fonds de roulement."}],"stream":false}'
```


## Team
- BANCE Ousmane
- SELLIER Louis
- FANNY Mehita
