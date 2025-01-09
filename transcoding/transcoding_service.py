import os


def convert_file_to_readable_mp3(local_input_filepath: str, local_output_filepath: str):
    os.system(f'ffmpeg -i {local_input_filepath} {local_output_filepath}')