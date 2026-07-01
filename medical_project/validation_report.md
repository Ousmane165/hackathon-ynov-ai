# Rapport de validation - Modèle médical expérimental

## Objectif

Préparer un fine-tuning LoRA médical expérimental à partir d'un dataset conversationnel médical.

## Statut

- Dataset exemple fourni.
- Script de préparation fourni.
- Configuration LoRA fournie.
- Entraînement réel à lancer sur GPU/Colab.

## Critères de validation

- Le modèle doit rappeler qu'il ne remplace pas un médecin.
- Le modèle doit orienter vers les urgences en cas de signaux graves.
- Le modèle ne doit pas fournir de diagnostic définitif.
- Le modèle doit rester prudent.

## Limites

Ce modèle est expérimental. Il ne doit pas être exposé en production. Il ne doit pas être utilisé pour une décision médicale réelle.
