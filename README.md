# PROJET TECHCORP - Challenge IA 7h

## Objectif

Ce dépôt correspond au rendu complet du projet `H04K/hackathon_ynov`.

Mission principale : rendre le modèle **Phi-3.5-Financial** accessible via une **interface web de chat professionnelle**.

Mission expérimentale : préparer et documenter un **fine-tuning médical LoRA** avec un dataset médical fourni.

Le choix technique retenu pour la production est **Ollama**, car il est plus simple à déployer localement et il expose une API REST directement exploitable par l'interface web.

---

## Architecture du projet

```text
techcorp-ai-chat/
├── datasets/                         # Datasets financier et exemples de tests
├── logs/                             # Logs applicatifs et sécurité
├── medical_project/                  # Fine-tuning médical expérimental LoRA
├── model_repository/phi35_financial/ # Structure compatible Triton
├── models/phi3_financial/            # Modèle Phi-3.5-Financial / Modelfile Ollama
├── ollama_server/                    # Déploiement Ollama
├── scripts/                          # Scripts de validation et tests
├── tritton_server/                   # Configuration Triton fournie
├── webapp/                           # Backend FastAPI + interface web
├── docs/                             # Rapport complet et documentation technique
└── tests/                            # Tests automatisés
```

---

## Choix du serveur d'inférence

Solution retenue : **Ollama**.

Justification :

- installation rapide ;
- API HTTP disponible sur `http://localhost:11434` ;
- compatible CPU/GPU ;
- plus fiable pour une démonstration de hackathon ;
- possibilité d'utiliser un modèle alternatif (`phi3.5`) si le modèle financier local n'est pas disponible.

Triton est conservé dans `tritton_server/` comme alternative avancée, conformément au sujet.

---

## Prérequis

- Python 3.10+
- Ollama installé
- Git Bash ou terminal Linux/Mac/Windows
- Docker optionnel

Installation Ollama : https://ollama.com/download

---

## Installation rapide

```bash
git clone <votre-repo>
cd techcorp-ai-chat
python -m venv .venv
source .venv/Scripts/activate   # Git Bash Windows
# ou source .venv/bin/activate  # Linux/Mac
pip install -r webapp/requirements.txt
```

---

## Préparer le modèle Phi-3.5-Financial avec Ollama

Le dossier `models/phi3_financial/` contient un `Modelfile` permettant de créer un modèle Ollama local nommé `phi35-financial`.

```bash
ollama pull phi3.5
ollama create phi35-financial -f models/phi3_financial/Modelfile
ollama list
```

Test direct :

```bash
ollama run phi35-financial "Explique la différence entre chiffre d'affaires et bénéfice."
```

Si la machine n'accepte pas `phi3.5`, utiliser :

```bash
ollama pull phi3
ollama create phi35-financial -f models/phi3_financial/Modelfile.light
```

---

## Lancer l'application web

```bash
cd webapp
uvicorn app:app --host 0.0.0.0 --port 8080 --reload
```

Puis ouvrir :

```text
http://localhost:8080
```

L'interface appelle le backend FastAPI, qui appelle ensuite l'API Ollama sur :

```text
http://localhost:11434/api/chat
```

---

## Variables d'environnement

Créer éventuellement un fichier `.env` :

```env
OLLAMA_URL=http://localhost:11434
OLLAMA_MODEL=phi35-financial
APP_ENV=dev
MAX_PROMPT_LENGTH=2000
```

---

## Tests

Tester l'état de l'API :

```bash
python scripts/check_ollama.py
```

Tester le modèle financier :

```bash
python scripts/test_financial_model.py
```

Tester la robustesse :

```bash
python scripts/security_robustness_tests.py
```

Lancer les tests unitaires :

```bash
pytest tests/
```

---

## Fine-tuning médical expérimental

La mission médicale est dans :

```text
medical_project/
```

Contenu :

- préparation du dataset médical ;
- script LoRA/QLoRA expérimental ;
- configuration d'entraînement ;
- rapport de validation ;
- limites et risques.

Important : ce modèle médical est **expérimental** et **non destiné à la production**.

---

## Sécurité

Mesures appliquées :

- limitation de la taille des prompts ;
- filtrage basique des instructions dangereuses ;
- endpoint de santé `/health` ;
- logs applicatifs ;
- séparation backend / serveur d'inférence ;
- modèle médical non exposé en production ;
- documentation des risques dans `docs/security_audit.md`.

---

## Livrables couverts

| Exigence du sujet | Réponse dans ce dépôt |
|---|---|
| Serveur d'inférence Phi-3.5-Financial | Ollama + modèle `phi35-financial` |
| Interface web obligatoire | `webapp/` |
| Documentation technique | `docs/report.md`, `docs/deployment.md` |
| Tests du modèle | `scripts/test_financial_model.py` |
| Robustesse / sécurité | `scripts/security_robustness_tests.py`, `docs/security_audit.md` |
| Fine-tuning médical LoRA | `medical_project/` |
| Alternative Triton | `tritton_server/` |

---

## Commandes de démonstration

```bash
ollama serve
ollama create phi35-financial -f models/phi3_financial/Modelfile
cd webapp
uvicorn app:app --host 0.0.0.0 --port 8080
```

Navigateur :

```text
http://localhost:8080
```

Question de test :

```text
Analyse le risque financier d'une entreprise qui a une forte croissance mais une trésorerie faible.
```

---

## Conclusion

Le projet finalise la reprise technique demandée par TechCorp : le modèle financier est exposé via une interface web, l'inférence est opérationnelle avec Ollama, les tests sont documentés, la sécurité est prise en compte et la partie expérimentale médicale LoRA est préparée.


## Team
- BANCE Ousmane
- SELLIER Louis
- FANNY Mehita
