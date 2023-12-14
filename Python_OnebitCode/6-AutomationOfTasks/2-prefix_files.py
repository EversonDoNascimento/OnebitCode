from pathlib import Path

root_dir = Path('dados')
files = root_dir.iterdir()
print(list(files))

for file in list(files):
    print(file)