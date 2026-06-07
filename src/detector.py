import math
from collections import Counter
import mimetypes


def calculate_entropy(data):

    if not data:
        return 0

    counter = Counter(data)

    total = len(data)

    entropy = 0

    for count in counter.values():

        probability = count / total

        entropy -= probability * math.log2(probability)

    return entropy


def get_file_stats(filepath):

    with open(filepath, "rb") as file:

        sample = file.read(1024 * 256)

    entropy = calculate_entropy(sample)

    text_bytes = sum(
        32 <= b <= 126 or b in (9, 10, 13)
        for b in sample
    )

    text_ratio = text_bytes / len(sample) if sample else 0

    mime_type, _ = mimetypes.guess_type(filepath)

    return {
        "entropy": round(entropy, 2),
        "text_ratio": round(text_ratio, 2),
        "mime_type": mime_type or "unknown"
    }