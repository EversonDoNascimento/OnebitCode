from pathlib import Path

p1 = Path("dados",'teste.txt')
print(type(p1))

# Full name
print(p1.name)

# File name
print(p1.stem)

# Extension file name
print(p1.suffix)

# Verify if file exist
if p1.exists():
    with open(p1, 'r', encoding='utf-8') as file:
        print(file.read())

# Verify all files in directory
p2 = Path('dados')
print(list(p2.iterdir()))

for file in list(p2.iterdir()):
    print(file)