import json
import os

def test_config_json_valid():
    """Ensure config.json is valid JSON and contains required keys."""
    root = os.path.dirname(os.path.dirname(__file__))
    config_path = os.path.join(root, "config.json")
    assert os.path.isfile(config_path), "config.json is missing"
    with open(config_path, "r") as f:
        config = json.load(f)
    for key in ["model", "temperature", "max_tokens", "system_prompt", "context_lines"]:
        assert key in config, f"Missing key {key} in config.json"

def test_review_script_exists():
    """Ensure review.py exists."""
    root = os.path.dirname(os.path.dirname(__file__))
    script_path = os.path.join(root, "review.py")
    assert os.path.isfile(script_path), "review.py is missing"