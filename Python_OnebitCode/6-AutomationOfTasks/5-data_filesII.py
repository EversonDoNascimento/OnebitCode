from pathlib import Path
from datetime import datetime

def convertData(path):
    stats = path.stat()
    second_create = stats.st_ctime
    date_created = datetime.fromtimestamp(second_create)
    date_created_str = date_created.strftime("%Y-%m-%d_%H_%M_%S")
    return date_created_str

root_dir = Path('files')
file_paths = root_dir.glob(f"**/*")

for file in file_paths:
    if file.is_file():
        #parent_folder = file.parts[-2]
        #print(parent_folder)
        new_filename = f"{convertData(file)}-{file.name}"
        path_full = file.with_name(new_filename)
        file.rename(path_full)
        print(new_filename)