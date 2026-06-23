import json
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator


ROOT = Path(__file__).resolve().parents[1]


VALIDATION_TARGETS = [
    {
        "name": "Usage Policy",
        "schema": ROOT / "schemas" / "usage-policy.schema.json",
        "example": ROOT / "examples" / "usage-policy.example.yaml",
    },
    {
        "name": "License Template",
        "schema": ROOT / "schemas" / "license-template.schema.json",
        "example": ROOT / "examples" / "license-template.example.yaml",
    },
]


def load_json(path: Path):
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def load_yaml(path: Path):
    with path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def validate_target(target):
    print(f"[validate] {target['name']}")
    print(f"  schema : {target['schema'].relative_to(ROOT)}")
    print(f"  example: {target['example'].relative_to(ROOT)}")

    schema = load_json(target["schema"])
    example = load_yaml(target["example"])

    validator = Draft202012Validator(schema)
    errors = sorted(validator.iter_errors(example), key=lambda e: e.path)

    if errors:
        print(f"[error] {target['name']} validation failed")
        for error in errors:
            path = ".".join(str(part) for part in error.path) or "<root>"
            print(f"  - path: {path}")
            print(f"    message: {error.message}")
        raise SystemExit(1)

    print(f"[ok] {target['example'].name} is valid")


def main():
    for target in VALIDATION_TARGETS:
        validate_target(target)


if __name__ == "__main__":
    main()
