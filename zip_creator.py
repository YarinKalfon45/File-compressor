import zipfile
import pathlib


def create_dircetory(filepaths, destination, name):
    destination_path = pathlib.Path(destination, f"{name}.zip")
    with zipfile.ZipFile(destination_path, 'w') as archive:
        for filepath in filepaths:
            filepath = pathlib.Path(filepath)
            archive.write(filepath, arcname=filepath.name)
