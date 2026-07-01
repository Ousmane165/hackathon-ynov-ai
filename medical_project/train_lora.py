"""
Script expérimental de fine-tuning LoRA.
Il sert de base Colab/GPU. Les dépendances lourdes ne sont pas installées par défaut.
"""

import argparse
import yaml


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", default="config_lora.yaml")
    args = parser.parse_args()

    with open(args.config, "r", encoding="utf-8") as f:
        cfg = yaml.safe_load(f)

    print("Configuration LoRA chargée :")
    for key, value in cfg.items():
        print(f"- {key}: {value}")

    print("\nÉtapes prévues en environnement GPU :")
    print("1. Charger le modèle de base en 4-bit")
    print("2. Charger le dataset préparé")
    print("3. Appliquer PEFT LoRA")
    print("4. Entraîner")
    print("5. Sauvegarder les adaptateurs LoRA")


if __name__ == "__main__":
    main()
