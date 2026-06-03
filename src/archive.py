import shutil
import os


def compress_folder(folder_path):

    if not os.path.exists(folder_path):
        raise FileNotFoundError(
            f"Folder not found: {folder_path}"
        )

    archive_path = shutil.make_archive(
        folder_path,
        "zip",
        folder_path
    )

    return archive_path