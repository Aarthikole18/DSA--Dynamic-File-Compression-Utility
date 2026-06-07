import os
import csv
import pandas as pd
import matplotlib.pyplot as plt


CSV_FILE = "outputs/compression_history.csv"


def save_compression_history(result):

    os.makedirs("outputs", exist_ok=True)

    file_exists = os.path.exists(CSV_FILE)

    with open(CSV_FILE, "a", newline="") as file:

        writer = csv.writer(file)

        if not file_exists:

            writer.writerow([
                "codec",
                "original_size",
                "compressed_size",
                "ratio",
                "saved_bytes"
            ])

        writer.writerow([
            result["codec"],
            result["original_size"],
            result["compressed_size"],
            round(result["ratio"], 2),
            result["saved_bytes"]
        ])


def generate_chart():

    if not os.path.exists(CSV_FILE):

        print("No benchmark history found.")
        return

    df = pd.read_csv(CSV_FILE)

    plt.figure(figsize=(8, 5))

    plt.bar(
        df["codec"],
        df["ratio"]
    )

    plt.title("Compression Ratio by Codec")

    plt.xlabel("Codec")

    plt.ylabel("Compression Ratio (%)")

    plt.tight_layout()

    os.makedirs("outputs", exist_ok=True)

    plt.savefig(
        "outputs/compression_chart.png"
    )

    plt.close()

    print(
        "Chart saved to outputs/compression_chart.png"
    )