import os

#help(os)

# 2 - Retornar a pasta atual

diretorio = os.getcwd()

# 3 - listar arquivos e pastas

list = os.listdir()
print(list[5])
print(f"python3 {list[7][len(list[7]) - 2::]}")
#os.system(f"mkdir {(list[7][len(list[7]) - 2::]).upper()}")
os.system(f"mv {diretorio}/{list[5]} {diretorio}/PY")
# 4 - Apresentar versão SO

#os.system('lsb_release -a')


# 5 - Limpar terminal

#os.system('clear')

#os.system('sudo shutdown -h +30')
#os.system('sudo shutdown -c')