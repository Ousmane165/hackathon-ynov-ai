# Audit sécurité - TechCorp AI Chat

## Périmètre

- Backend FastAPI
- Interface web
- Serveur Ollama
- Modèle financier
- Projet médical expérimental

## Contrôles appliqués

| Contrôle | Statut |
|---|---:|
| Validation longueur prompt | OK |
| Blocage patterns dangereux simples | OK |
| Logs applicatifs | OK |
| Healthcheck | OK |
| Pas de secrets dans le code | OK |
| Dataset médical non exposé en production | OK |
| Documentation des limites | OK |

## Tests de robustesse

Prompts testés :

- demande de contournement des règles ;
- demande hors périmètre ;
- prompt très long ;
- question financière normale ;
- demande médicale sensible.

## Risques

- prompt injection avancée ;
- hallucination ;
- absence de compte utilisateur ;
- absence de chiffrement HTTPS en local ;
- absence de rate limiting.

## Recommandations

- ajouter Nginx + HTTPS ;
- ajouter authentification ;
- ajouter limitation par IP ;
- journaliser les erreurs dans un SIEM ;
- ajouter scan SCA/SAST dans CI.
