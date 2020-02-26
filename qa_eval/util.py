import json
import re

import json_lines



def load_json(file_path, encoding='utf-8'):
    with open(file_path, encoding=encoding) as f:
        data = json.load(f)

        return data


def load_jsonl(file_path, encoding='utf-8'):
    with open(file_path, encoding=encoding) as f:
        data = json_lines.reader(f)


        return list(data)
def any_sep_contained(text, seps):
    return any(sep in text for sep in seps)


def split_multi_seps(text, seps):
    pattern = "|".join(seps)

    return re.split(pattern, text)
