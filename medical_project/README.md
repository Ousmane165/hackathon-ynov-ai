# Projet médical expérimental - Fine-tuning LoRA

Ce dossier couvre la mission R&D du sujet : fine-tuner un modèle médical expérimental.

Ce modèle n'est pas destiné à la production et ne doit pas être utilisé pour établir un diagnostic.

## Contenu

- `medical_sample.jsonl` : exemple de dataset conversationnel.
- `prepare_dataset.py` : nettoyage et conversion instruction/réponse.
- `train_lora.py` : script expérimental LoRA/QLoRA.
- `config_lora.yaml` : paramètres d'entraînement.
- `validation_report.md` : rapport de validation et limites.

## Commandes

```bash
python prepare_dataset.py
python train_lora.py --config config_lora.yaml
```

L'entraînement réel nécessite un GPU et des dépendances Hugging Face/PEFT.


## Team
- BANCE Ousmane
- SELLIER Louis
- FANNY Mehita
