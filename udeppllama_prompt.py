import json
import sys
from pathlib import Path


def format_prompts(records):
    prompts = [
        {
            "messages": [
                {"role": "system", "content": "Parse this sentence:"},
                {"role": "user", "content": input_text},
                {"role": "assistant", "content": target_text},
            ]
        } for id, prefix, input_text, target_text in records
    ]
    return prompts


def convert_to_jsonl(src_path, dst_path):
    with open(src_path, "r", encoding="utf8") as fin:
        records = [r.rstrip().split("\t") for r in fin]
    prompts = format_prompts(records)
    with open(dst_path, "w", encoding="utf8") as fout:
        for prompt in prompts:
            json.dump(prompt, fout, ensure_ascii=True)
            print(file=fout)


if __name__ == "__main__":
    for src in sys.argv[1:]:
        split, format = src.split("-ud-")[-1].split(".")
        src_path = Path(src)
        dst_path = src_path.parent / f"udeppllama-{format}.{split}.jsonl"
        convert_to_jsonl(src_path, dst_path)
