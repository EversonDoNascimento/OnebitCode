from pathlib import Path

root_dir = Path('dados')
files = root_dir.iterdir()


for file in list(files):
    #print(file.stem)
    #print(file.suffix)
    new_file_name = f"{root_dir}_{file.stem}{file.suffix}"
    new_filepath = file.with_name(new_file_name)
    print(new_filepath)
    #file.rename(new_filepath)
    #file.rename(f"./dados/{new_file_name}")
