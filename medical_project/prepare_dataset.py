import json
from pathlib import Path

src = Path("medical_sample.jsonl")
out = Path("prepared_medical_dataset.jsonl")

with src.open("r", encoding="utf-8") as f_in, out.open("w", encoding="utf-8") as f_out:
    for line in f_in:
        row = json.loads(line)
        instruction = row["instruction"].strip()
        response = row["response"].strip()
        record = {
            "messages": [
                {"role": "system", "content": "Tu es un assistant médical expérimental prudent. Tu ne remplaces jamais un professionnel de santé."},
                {"role": "user", "content": instruction},
                {"role": "assistant", "content": response},
            ]
        }
        f_out.write(json.dumps(record, ensure_ascii=False) + "\n")

print(f"Dataset préparé : {out}")
