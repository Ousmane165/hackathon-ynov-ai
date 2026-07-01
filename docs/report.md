# Rapport de projet

## Membres du groupe
- BANCE Ousmane
- SELLIER Louis
- FANNY Mehita


# Rapport technique - Projet TechCorp AI Chat

## 1. Contexte

TechCorp Industries reprend un projet IA laissé par une équipe précédente. Le code et les données doivent être vérifiés, l'infrastructure finalisée et le modèle financier rendu accessible depuis une interface web.

Le sujet impose deux axes :

1. production : déployer Phi-3.5-Financial avec une interface chat web ;
2. expérimental : préparer un fine-tuning médical LoRA non destiné à la production.

## 2. Objectifs réalisés

| Objectif | Statut | Réalisation |
|---|---:|---|
| Serveur d'inférence | Réalisé | Ollama sur `localhost:11434` |
| Modèle financier | Réalisé | `phi35-financial` basé sur Phi-3.5 via Modelfile |
| Interface web | Réalisé | FastAPI + HTML/CSS/JS |
| API backend | Réalisé | Endpoint `/api/chat` |
| Documentation | Réalisé | README, rapport, déploiement, sécurité |
| Tests | Réalisé | scripts de test et tests pytest |
| Fine-tuning médical | Préparé | LoRA expérimental dans `medical_project/` |
| Alternative Triton | Fournie | config dans `tritton_server/` |

## 3. Architecture fonctionnelle

```text
Utilisateur
   |
   v
Interface Web Chat : http://localhost:8080
   |
   v
Backend FastAPI : /api/chat
   |
   v
Serveur Ollama : http://localhost:11434/api/chat
   |
   v
Modèle phi35-financial
```

## 4. Choix technique

La solution retenue est Ollama. Ce choix est adapté au contexte hackathon car il réduit le temps d'installation, facilite les tests et expose une API REST directement utilisable.

Triton est plus avancé mais demande davantage de configuration GPU, de packaging modèle et de gestion du backend Python. Il est donc conservé comme alternative dans le dossier `tritton_server/`.

## 5. Déploiement

### 5.1 Installation dépendances

```bash
python -m venv .venv
source .venv/Scripts/activate
pip install -r webapp/requirements.txt
```

### 5.2 Création modèle Ollama

```bash
ollama pull phi3.5
ollama create phi35-financial -f models/phi3_financial/Modelfile
```

### 5.3 Démarrage backend

```bash
cd webapp
uvicorn app:app --host 0.0.0.0 --port 8080
```

### 5.4 Accès interface

```text
http://localhost:8080
```

## 6. Interface web

L'interface web contient :

- une zone de discussion ;
- un champ de saisie ;
- un bouton d'envoi ;
- un statut de connexion au serveur Ollama ;
- un historique court envoyé au backend pour garder le contexte.

Le frontend appelle `/api/chat` avec le message utilisateur. Le backend transmet ensuite la requête à Ollama.

## 7. Backend API

Endpoints disponibles :

| Endpoint | Méthode | Rôle |
|---|---|---|
| `/` | GET | interface web |
| `/health` | GET | vérification FastAPI + Ollama |
| `/api/chat` | POST | conversation avec le modèle |

Le backend ajoute un system prompt pour cadrer le comportement financier du modèle.

## 8. Validation modèle financier

Exemples de prompts testés :

1. Explique la différence entre chiffre d'affaires et bénéfice.
2. Analyse les risques d'une entreprise avec forte croissance et faible trésorerie.
3. Propose des indicateurs pour suivre la santé financière d'une PME.
4. Explique le besoin en fonds de roulement.

Critères de validation :

- réponse en français ;
- réponse structurée ;
- pas d'invention de chiffres ;
- prudence dans les recommandations ;
- refus ou cadrage en cas de demande hors périmètre.

## 9. Sécurité et robustesse

Mesures mises en place :

- limitation de la longueur des prompts ;
- blocage simple de patterns dangereux ;
- logs applicatifs ;
- endpoint de santé ;
- non-exposition directe du modèle médical ;
- séparation webapp / inference server ;
- variable d'environnement pour l'URL Ollama.

Risques restants :

- hallucination du modèle ;
- prompt injection sophistiquée ;
- absence d'authentification utilisateur ;
- dépendance à la disponibilité locale d'Ollama ;
- absence de monitoring avancé.

Améliorations proposées :

- ajouter authentification ;
- ajouter rate limiting ;
- ajouter monitoring Prometheus/Grafana ;
- centraliser les logs ;
- ajouter reverse proxy Nginx ;
- effectuer un audit de dépendances.

## 10. Fine-tuning médical expérimental

Le dossier `medical_project/` prépare une expérimentation LoRA.

Étapes prévues :

1. récupérer le dataset médical ;
2. nettoyer les conversations ;
3. convertir au format instruction/réponse ;
4. lancer un entraînement LoRA/QLoRA ;
5. tester les réponses ;
6. documenter les limites.

Le modèle médical n'est pas déployé en production. Il est explicitement marqué comme expérimental.

## 11. Données

Le projet prévoit :

- dataset financier dans `datasets/financial_dataset_sample.json` ;
- dataset médical dans `medical_project/medical_sample.jsonl` ;
- scripts de préparation dans `medical_project/prepare_dataset.py`.

Les données sensibles ne doivent pas être commitées.

## 12. Résultats attendus

Lors du lancement correct :

- `/health` retourne `status: ok` si Ollama est actif ;
- l'interface web s'affiche sur `localhost:8080` ;
- une question financière reçoit une réponse structurée ;
- les tests scripts s'exécutent sans erreur si Ollama est lancé.

## 13. Conclusion

Le rendu final répond au sujet TechCorp : le modèle financier est accessible depuis une interface web, le serveur d'inférence est documenté, les tests et la sécurité sont traités, et la partie médicale LoRA est préparée comme expérimentation.
