import json
from pathlib import Path

def load_rules():
    with open(Path(__file__).parent.parent/"config"/"rules.json", "r") as f:
        rules = json.load(f)
    return rules


def build_extension_map(rules: dict):
    extension_map ={}
    for category, extensions in rules.items():
        for extension in extensions:
            extension_map[extension.lower()] = category
    return extension_map

def prepare_extension_map():
    loaded_rules =load_rules()
    created_extension_map =build_extension_map(loaded_rules)
    return created_extension_map