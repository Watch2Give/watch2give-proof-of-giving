import os
import json
from datetime import datetime

PROOF_FOLDER = "proofs"
REGISTRY_FILE = "proof_registry.json"

def save_uploaded_file(file, file_bytes):
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = f"{timestamp}_{file.filename}"
    filepath = os.path.join(PROOF_FOLDER, filename)

    with open(filepath, "wb") as f:
        f.write(file_bytes)

    return filename, filepath, timestamp

def save_proof_to_registry(filename, file_hash, timestamp):
    proof_entry = {
        "filename": filename,
        "hash": file_hash,
        "timestamp": timestamp
    }

    try:
        with open(REGISTRY_FILE, "r") as f:
            registry = json.load(f)
    except FileNotFoundError:
        registry = []

    registry.append(proof_entry)

    with open(REGISTRY_FILE, "w") as f:
        json.dump(registry, f, indent=4)
