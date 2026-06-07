import os
import shutil
import gzip
import bz2
import lzma
import brotli
import zstandard as zstd

from src.strategy import choose_strategy
from src.manifest import create_manifest


CHUNK_SIZE = 1024 * 1024


def compress_file(src):

    plan = choose_strategy(src)

    codec = plan.codec

    print("\nSelected Strategy")
    print("----------------------------")
    print(f"Codec  : {codec}")
    print(f"Level  : {plan.level}")
    print(f"Reason : {plan.reason}")
    print("----------------------------")

    # ==========================
    # STORE MODE
    # ==========================
    if codec == "store":

        output_file = src + ".store"

        shutil.copy2(
            src,
            output_file
        )

    # ==========================
    # ZSTD
    # ==========================
    elif codec == "zstd":

        output_file = src + ".zst"

        compressor = zstd.ZstdCompressor(
            level=plan.level
        )

        with open(src, "rb") as fin:
            with open(output_file, "wb") as fout:

                with compressor.stream_writer(
                    fout
                ) as writer:

                    while True:

                        chunk = fin.read(
                            CHUNK_SIZE
                        )

                        if not chunk:
                            break

                        writer.write(chunk)

    # ==========================
    # GZIP
    # ==========================
    elif codec == "gzip":

        output_file = src + ".gz"

        with open(src, "rb") as fin:

            with gzip.open(
                output_file,
                "wb",
                compresslevel=plan.level
            ) as fout:

                while True:

                    chunk = fin.read(
                        CHUNK_SIZE
                    )

                    if not chunk:
                        break

                    fout.write(chunk)

    # ==========================
    # BZIP2
    # ==========================
    elif codec == "bz2":

        output_file = src + ".bz2"

        with open(src, "rb") as fin:

            with bz2.open(
                output_file,
                "wb"
            ) as fout:

                while True:

                    chunk = fin.read(
                        CHUNK_SIZE
                    )

                    if not chunk:
                        break

                    fout.write(chunk)

    # ==========================
    # LZMA
    # ==========================
    elif codec == "lzma":

        output_file = src + ".xz"

        with open(src, "rb") as fin:

            with lzma.open(
                output_file,
                "wb",
                preset=min(plan.level, 9)
            ) as fout:

                while True:

                    chunk = fin.read(
                        CHUNK_SIZE
                    )

                    if not chunk:
                        break

                    fout.write(chunk)

    # ==========================
    # BROTLI
    # ==========================
    elif codec == "brotli":

        output_file = src + ".br"

        compressor = brotli.Compressor(
            quality=plan.level
        )

        with open(src, "rb") as fin:
            with open(output_file, "wb") as fout:

                while True:

                    chunk = fin.read(
                        CHUNK_SIZE
                    )

                    if not chunk:
                        break

                    fout.write(
                        compressor.process(
                            chunk
                        )
                    )

                fout.write(
                    compressor.finish()
                )

    else:

        raise ValueError(
            f"Unsupported codec: {codec}"
        )

    # ==========================
    # REPORT
    # ==========================
    original_size = os.path.getsize(
        src
    )

    compressed_size = os.path.getsize(
        output_file
    )

    ratio = (
        compressed_size /
        original_size
    ) * 100

    saved = (
        original_size -
        compressed_size
    )

    manifest = create_manifest(
        src,
        output_file
    )

    return {
        "codec": codec,
        "output": output_file,
        "manifest": manifest,
        "original_size": original_size,
        "compressed_size": compressed_size,
        "ratio": ratio,
        "saved_bytes": saved,
        "reason": plan.reason
    }