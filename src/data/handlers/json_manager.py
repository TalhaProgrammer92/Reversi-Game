from pathlib import Path
import json

def load_json(path: Path) -> dict:
    """
    This function load configuration
    """
    # makedirs(path, exist_ok=True)

    if not path.exists():
        raise RuntimeError("Config file missing")

    with path.open("r", encoding="utf-8") as f:
        return json.load(f)
