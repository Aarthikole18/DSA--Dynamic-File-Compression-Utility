import json
import hashlib
import os


def calculate_sha256(filepath):
    sha256 = hashlib.sha256()

    with open(filepath, "rb") as file:
        while True:
            chunk = file.read(4096)

            if not chunk:
                break

            sha256.update(chunk)

    return sha256.hexdigest()


def create_manifest(original_file, compressed_file):

    data = {
        "original_file": original_file,
        "compressed_file": compressed_file,
        "original_size": os.path.getsize(original_file),
        "compressed_size": os.path.getsize(compressed_file),
        "sha256": calculate_sha256(original_file)
    }

    manifest_file = compressed_file + ".json"

    with open(manifest_file, "w") as file:
        json.dump(data, file, indent=4)

    return manifest_file