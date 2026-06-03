import argparse

from src.compress import compress_file
from src.verify import (
    decompress_file,
    verify_manifest
)
from src.benchmark import benchmark_file
from src.archive import compress_folder


def main():

    parser = argparse.ArgumentParser(
        description="Dynamic File Compression Utility"
    )

    subparsers = parser.add_subparsers(
        dest="command"
    )

    # ==================================================
    # COMPRESS COMMAND
    # ==================================================
    compress_parser = subparsers.add_parser(
        "compress",
        help="Compress a file"
    )

    compress_parser.add_argument(
        "path",
        help="Path of file to compress"
    )

    # ==================================================
    # DECOMPRESS COMMAND
    # ==================================================
    decompress_parser = subparsers.add_parser(
        "decompress",
        help="Decompress a compressed file"
    )

    decompress_parser.add_argument(
        "path",
        help="Path of compressed file"
    )

    # ==================================================
    # BENCHMARK COMMAND
    # ==================================================
    benchmark_parser = subparsers.add_parser(
        "benchmark",
        help="Compare all compression codecs"
    )

    benchmark_parser.add_argument(
        "path",
        help="Path of file to benchmark"
    )

    # ==================================================
    # VERIFY COMMAND
    # ==================================================
    verify_parser = subparsers.add_parser(
        "verify",
        help="Verify manifest integrity"
    )

    verify_parser.add_argument(
        "manifest",
        help="Path of manifest JSON file"
    )

    # ==================================================
    # FOLDER COMMAND
    # ==================================================
    folder_parser = subparsers.add_parser(
        "folder",
        help="Compress an entire folder"
    )

    folder_parser.add_argument(
        "path",
        help="Path of folder to compress"
    )

    args = parser.parse_args()

    # ==================================================
    # COMPRESS
    # ==================================================
    if args.command == "compress":

        result = compress_file(args.path)

        print("\n" + "=" * 60)
        print("COMPRESSION SUCCESSFUL")
        print("=" * 60)

        print(f"Selected Codec     : {result['codec']}")
        print(f"Output File        : {result['output']}")
        print(f"Manifest File      : {result['manifest']}")
        print(f"Original Size      : {result['original_size']} bytes")
        print(f"Compressed Size    : {result['compressed_size']} bytes")
        print(f"Compression Ratio  : {result['ratio']:.2f}%")

        print("=" * 60)

    # ==================================================
    # DECOMPRESS
    # ==================================================
    elif args.command == "decompress":

        output_file = decompress_file(
            args.path
        )

        print("\n" + "=" * 60)
        print("DECOMPRESSION SUCCESSFUL")
        print("=" * 60)

        print(f"Output File : {output_file}")

        print("=" * 60)

    # ==================================================
    # BENCHMARK
    # ==================================================
    elif args.command == "benchmark":

        report_file, results = benchmark_file(
            args.path
        )

        print("\n" + "=" * 60)
        print("BENCHMARK REPORT")
        print("=" * 60)

        print(
            f"{'Codec':<12}"
            f"{'Compressed Size':<20}"
            f"{'Ratio (%)'}"
        )

        print("-" * 60)

        for row in results:

            print(
                f"{row[0]:<12}"
                f"{str(row[2]) + ' bytes':<20}"
                f"{row[3]}"
            )

        print("\nReport Saved:", report_file)

        print("=" * 60)

    # ==================================================
    # VERIFY
    # ==================================================
    elif args.command == "verify":

        result = verify_manifest(
            args.manifest
        )

        print("\n" + "=" * 60)
        print("VERIFICATION RESULT")
        print("=" * 60)

        if result:
            print("Integrity Check Passed")
        else:
            print("Integrity Check Failed")

        print("=" * 60)

    # ==================================================
    # FOLDER COMPRESSION
    # ==================================================
    elif args.command == "folder":

        archive_file = compress_folder(
            args.path
        )

        print("\n" + "=" * 60)
        print("FOLDER COMPRESSION SUCCESSFUL")
        print("=" * 60)

        print(f"Archive Created : {archive_file}")

        print("=" * 60)

    # ==================================================
    # HELP
    # ==================================================
    else:

        parser.print_help()


if __name__ == "__main__":
    main()