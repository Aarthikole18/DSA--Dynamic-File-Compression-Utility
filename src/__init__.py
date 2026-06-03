from dataclasses import dataclass

@dataclass
class Plan:
    codec: str
    level: int

def choose_strategy(path):
    return Plan(
        codec="zstd",
        level=6
    )