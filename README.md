# Dynamic File Compression Utility

## Overview

Dynamic File Compression Utility is a Python-based compression system that automatically selects the most suitable compression algorithm based on file type and content characteristics.

The project supports multiple compression codecs, benchmark analysis, integrity verification, folder compression, and compression reporting.

It demonstrates practical applications of Data Structures & Algorithms, file handling, compression techniques, and system design concepts.

---

## Features

* Dynamic codec selection
* Zstandard (ZSTD) compression
* GZIP compression
* BZIP2 compression
* LZMA/XZ compression
* Brotli compression
* Universal decompression
* SHA-256 integrity verification
* Manifest file generation
* Compression ratio analysis
* Benchmark comparison across codecs
* CSV benchmark report generation
* Folder compression support
* Command Line Interface (CLI)

---

## Technologies Used

* Python 3.x
* Zstandard
* Brotli
* GZIP
* BZIP2
* LZMA
* Argparse
* JSON
* CSV
* Hashlib

---

## Project Structure

```text
Dynamic-File-Compression-Utility/
│
├── input_files/
├── compressed_files/
├── decompressed_files/
├── outputs/
│   └── benchmark_report.csv
│
├── images/
├── docs/
├── tests/
│
├── src/
│   ├── archive.py
│   ├── benchmark.py
│   ├── cli.py
│   ├── compress.py
│   ├── manifest.py
│   ├── strategy.py
│   ├── verify.py
│   └── __init__.py
│
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## How It Works

### Compression Workflow

Input File
↓
File Analysis
↓
Codec Selection
↓
Compression
↓
Manifest Generation
↓
Compressed Output

### Decompression Workflow

Compressed File
↓
Codec Detection
↓
Decompression
↓
Original File Recovery

---

## Supported Compression Algorithms

| Codec  | Extension |
| ------ | --------- |
| ZSTD   | .zst      |
| GZIP   | .gz       |
| BZIP2  | .bz2      |
| LZMA   | .xz       |
| Brotli | .br       |

---

## Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/Dynamic-File-Compression-Utility.git
cd Dynamic-File-Compression-Utility
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows

```bash
venv\Scripts\activate
```

Linux / Mac

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Usage

### Compress File

```bash
python main.py compress input_files/sample.txt
```

### Decompress File

```bash
python main.py decompress input_files/sample.txt.zst
```

### Benchmark All Codecs

```bash
python main.py benchmark input_files/sample.txt
```

### Verify Integrity

```bash
python main.py verify input_files/sample.txt.zst.json
```

### Compress Folder

```bash
python main.py folder input_files
```

---

## Sample Output

```text
============================================================
COMPRESSION SUCCESSFUL
============================================================

Selected Codec : zstd

Output File : input_files/sample.txt.zst

Manifest File : input_files/sample.txt.zst.json

Compression Ratio : 43.52%
```

---

## Benchmark Report

Generated CSV:

```text
outputs/benchmark_report.csv
```

Example:

| Codec  | Original Size | Compressed Size | Ratio (%) |
| ------ | ------------- | --------------- | --------- |
| ZSTD   | 1000          | 430             | 43.0      |
| GZIP   | 1000          | 480             | 48.0      |
| BZIP2  | 1000          | 510             | 51.0      |
| LZMA   | 1000          | 420             | 42.0      |
| Brotli | 1000          | 400             | 40.0      |

---

## DSA Concepts Used

* Greedy Compression Strategy Selection
* Hash Tables (Dictionary-based metadata)
* File Chunk Processing
* Data Encoding Techniques
* Performance Analysis
* Benchmarking Algorithms
* Integrity Verification using Hashing

---

## Learning Outcomes

* File Compression Techniques
* Compression Algorithm Comparison
* Data Integrity Verification
* System Design Concepts
* CLI Application Development
* Python File Handling
* Performance Benchmarking

---

## Future Enhancements

* Parallel Compression
* Multi-threaded Processing
* Cloud Storage Integration
* Encryption Support
* Dictionary-Based Compression
* Web Dashboard
* GUI Application

---

## Author

Aarthi Kole

Electrical and Electronics Engineering Student

Aspiring Software Developer | DSA Enthusiast | Full Stack Learner
