import os
import gzip
import bz2
import lzma
import brotli
import zstandard as zstd

from src.strategy import choose_strategy
from src.manifest import create_manifest


def compress_file(src):

    plan = choose_strategy(src)

    codec = plan.codec

    if codec == "zstd":

        output_file = src + ".zst"

        compressor = zstd.ZstdCompressor(
            level=plan.level
        )

        with open(src, "rb") as fin:
            with open(output_file, "wb") as fout:

                with compressor.stream_writer(fout) as writer:

                    while True:

                        chunk = fin.read(1024 * 1024)

                        if not chunk:
                            break

                        writer.write(chunk)

    elif codec == "gzip":

        output_file = src + ".gz"

        with open(src, "rb") as fin:
            with gzip.open(
                output_file,
                "wb",
                compresslevel=plan.level
            ) as fout:

                fout.write(fin.read())

    elif codec == "bz2":

        output_file = src + ".bz2"

        with open(src, "rb") as fin:
            with bz2.open(
                output_file,
                "wb"
            ) as fout:

                fout.write(fin.read())

    elif codec == "lzma":

        output_file = src + ".xz"

        with open(src, "rb") as fin:
            with lzma.open(
                output_file,
                "wb"
            ) as fout:

                fout.write(fin.read())

    elif codec == "brotli":

        output_file = src + ".br"

        with open(src, "rb") as fin:

            compressed = brotli.compress(
                fin.read(),
                quality=plan.level
            )

        with open(output_file, "wb") as fout:

            fout.write(compressed)

    else:

        raise ValueError("Unsupported codec")

    original_size = os.path.getsize(src)

    compressed_size = os.path.getsize(output_file)

    ratio = (
        compressed_size /
        original_size
    ) * 100

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
        "ratio": ratio
    }