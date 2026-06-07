from dataclasses import dataclass
from src.detector import get_file_stats


@dataclass
class Plan:
    codec: str
    level: int
    reason: str


def choose_strategy(filepath):

    stats = get_file_stats(filepath)

    entropy = stats["entropy"]
    text_ratio = stats["text_ratio"]
    mime_type = stats["mime_type"]

    # Already compressed media
    if (
        mime_type.startswith("image/")
        or mime_type.startswith("video/")
        or mime_type.startswith("audio/")
    ):
        return Plan(
            codec="store",
            level=0,
            reason="Already compressed media"
        )

    # JSON / CSV
    if (
        "json" in mime_type
        or "csv" in mime_type
    ):
        return Plan(
            codec="zstd",
            level=8,
            reason="Structured text data"
        )

    # Plain text
    if text_ratio > 0.9:

        if entropy < 5:

            return Plan(
                codec="brotli",
                level=9,
                reason="Highly compressible text"
            )

        return Plan(
            codec="zstd",
            level=6,
            reason="General text file"
        )

    # Binary data
    if entropy > 7:

        return Plan(
            codec="lzma",
            level=7,
            reason="High entropy binary data"
        )

    # Default
    return Plan(
        codec="zstd",
        level=6,
        reason="Balanced compression"
    )