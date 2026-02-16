import zipfile

def extract_archive(archive_path,destination_directory):
    with zipfile.ZipFile(archive_path,'r') as archive:
        archive.extractall(destination_directory)

if __name__ == '__main__':
    extract_archive(r"\Users\marbl\PycharmProjects\ToDo_App\Bonus\compressed.zip",
        r"\Users\marbl\PycharmProjects\ToDo_App\Bonus\files")