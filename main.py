__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

import os
import shutil

cwd = os.getcwd()
cache_path = os.path.join(cwd, "files", "cache")
print(cwd)
print(cache_path)

# opdracht 1


def clean_cache():
    if os.path.exists(cache_path):
        for file_name in os.listdir(cache_path):
            # construct full file path
            file = os.path.join(cache_path, file_name)
            print(file)
            if os.path.isfile(file):
                print('Deleting file:', file)
                os.remove(file)
    else:
        os.mkdir(cache_path)


clean_cache()

# opdracht 2 klaar


def cache_zip(zip_file_path, cache_dir_path):
    filename = zip_file_path
    extract_dir = cache_dir_path
    shutil.unpack_archive(filename, extract_dir)


cache_zip(os.path.join(cwd, "files", "data.zip"),
          cache_path)


# opdracht 3 klaar

def cached_files():
    list_dir = []
    for file in os.listdir(cache_path):
        f = os.path.join(cache_path, file)
        list_dir.append(os.path.abspath(f))
    return list_dir


# opdracht 4

def find_password(lijst_pdracht_3):
    for file in lijst_pdracht_3:
        with open(file, "r") as read_file:
            for lines in read_file:
                if "password" in lines:
                    pw = lines[lines.find(" ")+1:lines.find("\\n")]
                    return pw


find_password(cached_files())
print(find_password(cached_files()))
