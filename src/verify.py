import gzip
import bz2
import lzma
import brotli
import zstandard as zstd
import hashlib
import json
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


def decompress_file(src):

    if src.endswith(".zst"):

        output_file = src[:-4]

        decompressor = zstd.ZstdDecompressor()

        with open(src, "rb") as fin:
            with open(output_file, "wb") as fout:

                with decompressor.stream_reader(fin) as reader:

                    while True:

                        chunk = reader.read(1024 * 1024)

                        if not chunk:
                            break

                        fout.write(chunk)

    elif src.endswith(".gz"):

        output_file = src[:-3]

        with gzip.open(src, "rb") as fin:
            with open(output_file, "wb") as fout:
                fout.write(fin.read())

    elif src.endswith(".bz2"):

        output_file = src[:-4]

        with bz2.open(src, "rb") as fin:
            with open(output_file, "wb") as fout:
                fout.write(fin.read())

    elif src.endswith(".xz"):

        output_file = src[:-3]

        with lzma.open(src, "rb") as fin:
            with open(output_file, "wb") as fout:
                fout.write(fin.read())

    elif src.endswith(".br"):

        output_file = src[:-3]

        with open(src, "rb") as fin:
            compressed_data = fin.read()

        decompressed_data = brotli.decompress(
            compressed_data
        )

        with open(output_file, "wb") as fout:
            fout.write(decompressed_data)

    else:

        raise ValueError(
            "Unsupported compressed file format"
        )

    return output_file


def verify_manifest(manifest_file):

    with open(manifest_file, "r") as file:
        manifest = json.load(file)

    original_hash = manifest["sha256"]

    current_hash = calculate_sha256(
        manifest["original_file"]
    )

    return original_hash == current_hash