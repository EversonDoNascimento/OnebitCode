from pathlib import Path
import os
#current_dir = Path.cwd()
#print(current_dir)
dir_input = input("Digite o nome do diretório: ")
def creationDir(path):
    for file in path.glob("**/*"):
        if file.is_file():
            extension_name = file.suffix
            path_file = file.parts 
            origem_str = '/'.join(list(path_file)[:-1])           
            new_dict = Path(f"{origem_str}/{extension_name[1:]}")
           
            if new_dict.exists():
                pass
            else:
                if len(path_file) <= 2:
                    if f"{file.parts[-2]}" == f"{extension_name[1:]}":
                        pass
                    else:
                     
                        new_dict.mkdir()
            

def moveFiles(path):   
    for file in path.glob("**/*"):
        if file.is_file():
            extension_file = file.suffix
            file_origin = file
        
            if f"{str(file_origin.parts[-2])}" == file.suffix[1:] :
                pass
            else:
                 if len(file_origin.parts) <= 2:
                    if file.name != "Exercise1.py":
                        file_destiny_current = "/".join(list(file.parts[:-1])) 
                        file_destiny= f"{file_destiny_current}/{extension_file[1:]}/{file.name}"
                        file_origin.replace(file_destiny)
         
         
#path = Path("./")
#for file in path.glob("**/*"):
#    print(file)

       
creationDir(Path(f"{dir_input}"))
moveFiles(Path(f"{dir_input}"))


#"/".join(list(file.parts[:-1]))


