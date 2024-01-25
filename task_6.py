import os
import logging
from collections import namedtuple

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

FileInfo = namedtuple('FileInfo', ['name', 'extension', 'is_directory', 'parent_directory'])

def get_directory_info(directory_path, log_file='directory_info.log'):
    try:
        with open(log_file, 'w') as file:
            for item in os.listdir(directory_path):
                item_path = os.path.join(directory_path, item)
                is_directory = os.path.isdir(item_path)
                name, extension = os.path.splitext(item)

                file_info = FileInfo(name, extension[1:], is_directory, os.path.basename(directory_path))

                logging.info(f"Name: {file_info.name}, Extension: {file_info.extension}, "
                             f"Is Directory: {file_info.is_directory}, Parent Directory: {file_info.parent_directory}")

                file.write(f"Name: {file_info.name}, Extension: {file_info.extension}, "
                           f"Is Directory: {file_info.is_directory}, Parent Directory: {file_info.parent_directory}\n")

    except Exception as e:
        logging.error(f"Error: {str(e)}")

if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage: python script.py <directory_path> [log_file]")
        sys.exit(1)

    directory_path = sys.argv[1]
    log_file = 'directory_info.log'

    if len(sys.argv) == 3:
        log_file = sys.argv[2]

    if not os.path.exists(directory_path) or not os.path.isdir(directory_path):
        print("Invalid directory path.")
        sys.exit(1)

    get_directory_info(directory_path, log_file)
