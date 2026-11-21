
import json

def parse_model_json(reply):
    """Return the first JSON object in a model's reply, or None."""
    decoder = json.JSONDecoder()

    for i in range(len(reply)):
        if reply[i] == "{":
            try:
                obj, end = decoder.raw_decode(reply, i)
                if isinstance(obj, dict):
                    return obj
            except json.JSONDecodeError:
                continue

    return None
