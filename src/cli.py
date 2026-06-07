import argparse

from src.compress import compress_file
from src.verify import (
    decompress_file,
    verify_manifest
)
from src.benchmark import benchmark_file
from src.archive import compress_folder
from src.analytics import (
    save_compression_history,
    generate_chart
)


def main():

    parser = argparse.ArgumentParser(
        description="Dynamic File Compression Utility"
    )

    subparsers = parser.add_subparsers(
        dest="command"
    )

    # ==================================================
    # COMPRESS
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
    # DECOMPRESS
    # ==================================================
    decompress_parser = subparsers.add_parser(
        "decompress",
        help="Decompress a file"
    )

    decompress_parser.add_argument(
        "path",
        help="Compressed file path"
    )

    # ==================================================
    # BENCHMARK
    # ==================================================
    benchmark_parser = subparsers.add_parser(
        "benchmark",
        help="Benchmark all codecs"
    )

    benchmark_parser.add_argument(
        "path",
        help="Path of file"
    )

    # ==================================================
    # VERIFY
    # ==================================================
    verify_parser = subparsers.add_parser(
        "verify",
        help="Verify manifest"
    )

    verify_parser.add_argument(
        "manifest",
        help="Manifest JSON file"
    )

    # ==================================================
    # FOLDER
    # ==================================================
    folder_parser = subparsers.add_parser(
        "folder",
        help="Compress a folder"
    )

    folder_parser.add_argument(
        "path",
        help="Folder path"
    )

    # ==================================================
    # CHART
    # ==================================================
    subparsers.add_parser(
        "chart",
        help="Generate compression analytics chart"
    )

    args = parser.parse_args()

    # ==================================================
    # COMPRESS
    # ==================================================
    if args.command == "compress":

        result = compress_file(
            args.path
        )

        save_compression_history(
            result
        )

        print("\n" + "=" * 60)
        print("COMPRESSION SUCCESSFUL")
        print("=" * 60)

        print(
            f"Selected Codec     : {result['codec']}"
        )

        print(
            f"Output File        : {result['output']}"
        )

        print(
            f"Manifest File      : {result['manifest']}"
        )

        print(
            f"Original Size      : {result['original_size']} bytes"
        )

        print(
            f"Compressed Size    : {result['compressed_size']} bytes"
        )

        print(
            f"Compression Ratio  : {result['ratio']:.2f}%"
        )

        print(
            f"Saved Bytes        : {result['saved_bytes']} bytes"
        )

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

        print(
            f"Output File : {output_file}"
        )

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

        print(
            f"\nReport Saved : {report_file}"
        )

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

            print(
                "Integrity Check Passed"
            )

        else:

            print(
                "Integrity Check Failed"
            )

        print("=" * 60)

    # ==================================================
    # FOLDER
    # ==================================================
    elif args.command == "folder":

        archive_file = compress_folder(
            args.path
        )

        print("\n" + "=" * 60)
        print("FOLDER COMPRESSION SUCCESSFUL")
        print("=" * 60)

        print(
            f"Archive Created : {archive_file}"
        )

        print("=" * 60)

    # ==================================================
    # CHART
    # ==================================================
    elif args.command == "chart":

        generate_chart()

        print("\n" + "=" * 60)
        print("ANALYTICS CHART GENERATED")
        print("=" * 60)

        print(
            "Saved: outputs/compression_chart.png"
        )

        print("=" * 60)

    # ==================================================
    # HELP
    # ==================================================
    else:

        parser.print_help()


if __name__ == "__main__":
    main()