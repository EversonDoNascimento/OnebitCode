import functionShutdown

timer = input("Digite o tempo que você deseja desligar o computador: ")
cond = input("Você tem certeza que quer desligar o computador? ")

functionShutdown.shutdown(timer,cond)

# Utilize o comando python3 -m http.server para criar um servidor http local na sua rede