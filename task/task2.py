import os


def find_file_ext(directory, extension):

    for entry in os.listdir(directory):
        full_path=os.path.join(directory, entry)

    if os.path.isfile(full_path):
        if full_path.endswith(extension):
            return full_path
    elif os.path.isdir(full_path):
        result = find_file_ext(full_path, extension)
        if result:
            return result
    return None