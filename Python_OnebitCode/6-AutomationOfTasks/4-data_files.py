from pathlib import Path
from datetime import datetime

path = Path("files", "dados", "b.txt")
print(path)

# Getting the file metadata
stats = path.stat()

# Getting the info about data of file
second_create = stats.st_ctime

# Tranform metadata second_create in data
date_created = datetime.fromtimestamp(second_create)


#Formatting data 
date_created_str = date_created.strftime("%Y-%m-%d_%H_%M_%S")
print(date_created_str)
