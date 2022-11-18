__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"
__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

import os
import shutil

cwd = os.getcwd()
print(cwd)


dir = os.path.join("T:\\", "Winc_Academy")
print(dir)

if os.path.exists(dir) or os.path.isdir(dir):
    print(f'The {dir} is a directory')


# opdracht 1 klaar


def clean_cache():
    path = r"T:\Winc_Academy\files\cache\\"
    try:
        os.mkdir(path)
    except Exception:
        pass
    for file_name in os.listdir(path):
        # construct full file path
        file = path + file_name
        if os.path.isfile(file):
            print('Deleting file:', file)
            os.remove(file)
        elif os.path.isdir(file):
            os.rmdir(file)


clean_cache()


# opdracht 2 klaar


def cache_zip(zip_file_path, cache_dir_path):
    filename = zip_file_path
    extract_dir = cache_dir_path
    archive_format = "zip"
    shutil.unpack_archive(filename, extract_dir, archive_format)


cache_zip(r"T:\Winc_Academy\files\data.zip\\",
          r"T:\Winc_Academy\files\cache\\")


# opdracht 3 klaar

def cached_files():
    my_path = r"T:\Winc_Academy\files\cache"
    list_dir = []
    for file in os.listdir(my_path):
        f = os.path.join(my_path, file)
        list_dir.append(os.path.abspath(f))
    return list_dir


outlist = cached_files()


# opdracht 4

def find_password(lijst_pdracht_3):
    for file in lijst_pdracht_3:
        with open(file, "r") as read_file:
            for lines in read_file:
                if "password" in lines:
                    return lines[10:38]


find_password(cached_files())
print(find_password(cached_files()))
