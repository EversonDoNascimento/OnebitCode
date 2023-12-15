from pathlib import Path

root_dir = Path('files')
#files_path = root_dir.iterdir()

#for path in files_path:
    #print(path)
#    for file in path.iterdir:
#        print(file)

#file_paths = root_dir.glob("**/*")
#for path in file_paths:
#    print(path)

print(len(list(root_dir.iterdir())))
count_files = len(list(root_dir.iterdir()))
file_paths = root_dir.glob(f"{'*'*count_files}/*")
for path in file_paths:
    #print(path)
    if path.is_file():
        #print(path)
        #print(path.parts[-2])
        # parts lista o caminho em forma de tupla
        parent_folder = path.parts[-2]
        print(parent_folder)
        #Juntando o nome da pasta com o nome do arquivo
        new_filename = f"{parent_folder}-{path.name}"
        print(new_filename)
        #Pegando o caminho do diretorio para passar o caminho completo no rename
        #new_path_file = path.with_name(new_filename)
        #path.rename(new_path_file)
      