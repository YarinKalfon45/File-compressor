import zipfile
import pathlib
def create_dircetory(filepaths,destination):
    destination_path = pathlib.Path(destination,"Compressed.zip")
    with zipfile.ZipFile(destination_path,'w') as archive:
        for filepath in filepaths:
            filepath = pathlib.Path(filepath)
            archive.write(filepath,arcname=filepath.name)
