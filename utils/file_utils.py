import tempfile
import os
from uuid import uuid4

TMP_FOLDER_NAME = "mpcsj_voice_assistant"


def create_if_not_exists(path: str):
    if not os.path.exists(path):
        os.makedirs(path)


def get_tmp_folder_path():
    path = tempfile.gettempdir()
    path = os.path.join(path, TMP_FOLDER_NAME)
    create_if_not_exists(path)
    return path


def get_unique_tmp_file_path():
    filepath = os.path.join(get_tmp_folder_path(), str(uuid4()))
    return filepath


def create_unique_tmp_file(file_suffix: str):
    return f'{get_unique_tmp_file_path()}_{file_suffix}'


def persist_binary_file_locally(data:bytes, file_suffix: str) -> str:
    filepath = create_unique_tmp_file(file_suffix)
    with open(filepath, 'wb') as f:
        f.write(data)

    return filepath


if __name__ == "__main__":
    print(get_tmp_folder_path())