with open("data/names.txt",'r', encoding='utf-8') as file:
    for line in file:
        print(f"Olá, {line.strip()}")