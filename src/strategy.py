from dataclasses import dataclass
import os


@dataclass
class Plan:
    codec: str
    level: int


def choose_strategy(path):

    extension = os.path.splitext(path)[1].lower()

    text_extensions = [
        ".txt",
        ".csv",
        ".json",
        ".xml",
        ".html",
        ".css",
        ".js"
    ]

    if extension in text_extensions:

        return Plan(
            codec="zstd",
            level=8
        )

    elif extension in [".log"]:

        return Plan(
            codec="brotli",
            level=9
        )

    elif extension in [".bin"]:

        return Plan(
            codec="lzma",
            level=6
        )

    else:

        return Plan(
            codec="gzip",
            level=6
        )