import json
import sys
from pathlib import Path


def convert_from_jsonl(src_path, dst_path):
    with open(src_path, "r", encoding="utf8") as fin:
        prompts = [json.loads(l) for l in fin]
    with open(dst_path, "w", encoding="utf8") as fout:
        for _, p in enumerate(prompts):
            sentence = p["messages"][-2]["content"].strip()
            output = p["messages"][-1]["content"].strip()
            if len(p["messages"]) == 2:
                sentence = sentence.split("\n")[-1]
            print(
                f"___{_}",
                "parse",
                sentence,
                output,
                sep="\t",
                file=fout,
            )


if __name__ == "__main__":
    for src in sys.argv[1:]:
        src_path = Path(src)
        dst_path = src_path.parent / (src_path.stem + ".txt")
        convert_from_jsonl(src_path, dst_path)
