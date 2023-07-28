from create_files import create_files


def create_files_2(extensions: dict) -> object:
    for extension, count in extensions.items():
        create_files(extension=extension, count=count)
