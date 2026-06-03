import os
import csv
import gzip
import bz2
import lzma
import brotli
import zstandard as zstd


def benchmark_file(filepath):

    original_size = os.path.getsize(filepath)

    results = []

    # ZSTD
    zstd_file = filepath + ".zst"

    with open(filepath, "rb") as fin:
        with open(zstd_file, "wb") as fout:

            compressor = zstd.ZstdCompressor(level=6)

            with compressor.stream_writer(fout) as writer:
                writer.write(fin.read())

    size = os.path.getsize(zstd_file)

    results.append([
        "ZSTD",
        original_size,
        size,
        round((size / original_size) * 100, 2)
    ])

    # GZIP
    gzip_file = filepath + ".gz"

    with open(filepath, "rb") as fin:
        with gzip.open(gzip_file, "wb") as fout:
            fout.write(fin.read())

    size = os.path.getsize(gzip_file)

    results.append([
        "GZIP",
        original_size,
        size,
        round((size / original_size) * 100, 2)
    ])

    # BZIP2
    bz2_file = filepath + ".bz2"

    with open(filepath, "rb") as fin:
        with bz2.open(bz2_file, "wb") as fout:
            fout.write(fin.read())

    size = os.path.getsize(bz2_file)

    results.append([
        "BZIP2",
        original_size,
        size,
        round((size / original_size) * 100, 2)
    ])

    # LZMA
    lzma_file = filepath + ".xz"

    with open(filepath, "rb") as fin:
        with lzma.open(lzma_file, "wb") as fout:
            fout.write(fin.read())

    size = os.path.getsize(lzma_file)

    results.append([
        "LZMA",
        original_size,
        size,
        round((size / original_size) * 100, 2)
    ])

    # Brotli
    br_file = filepath + ".br"

    with open(filepath, "rb") as fin:
        compressed = brotli.compress(fin.read())

    with open(br_file, "wb") as fout:
        fout.write(compressed)

    size = os.path.getsize(br_file)

    results.append([
        "BROTLI",
        original_size,
        size,
        round((size / original_size) * 100, 2)
    ])

    os.makedirs("outputs", exist_ok=True)

    report_file = "outputs/benchmark_report.csv"

    with open(report_file, "w", newline="") as csvfile:

        writer = csv.writer(csvfile)

        writer.writerow([
            "Codec",
            "Original Size",
            "Compressed Size",
            "Compression Ratio (%)"
        ])

        writer.writerows(results)

    return report_file, results