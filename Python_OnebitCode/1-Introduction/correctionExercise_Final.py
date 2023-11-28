teams = {}
done = False

def print_teams():
    print("Times listados")
    for i, team in enumerate(teams.values()):
        print(f"{i+1}. {team['name']} ({len(team['players'])} jogadores)")

def print_team_players(team):
    print(f"Jogadores do time {team['name']}: ")
    for i, player in enumerate(team['players']):
        print(f"{i + 1}. {player}")

while not done:
    print("O que você deseja fazer?")
    print("1. Adicionar um time")
    print("2. Remover um time")
    print("3. Listar times")
    print("4. Adicionar jogador em um time")
    print("5. Remover jogador de um time")
    print("6. Listar jogadores de um time")
    print("7. Sair")
    
    choice = int(input(">"))
    if(choice == 1):
        team_name = input("Digite o nome do time")
        teams[team_name] = {'name': team_name, 'players': []}
        print("Time adicionado!!")
    elif(choice == 2):
        team_num = int(input("Digite o número do time que você deseja remover: "))
        if(team_num <= len(teams)):
            # O list tá colocando as keys dentro de uma lista
            team_name = list(teams.keys())[team_num -1]
            del teams[team_name]
            print("Time excluído com sucesso!!")
        else:
            print("Número inválido!!")
    elif(choice == 3):
        print_teams()
       
    elif(choice == 4):
        print_teams()
        team_num = int(input("Digite o número do time que você deseja adicionar o jogador: "))
        if team_num <= len(teams):
            team_name = list(teams.keys())[team_num -1]
            player_name = input("Digite o nome do jogador que você deseja adicionar: ")
            teams[team_name]['players'].append(player_name)
            print("Jogador adicionado com sucesso!")
        else:
            print("Número inválido!!")
    elif(choice == 5):
        print_teams()
        team_num = int(input("Informe o número do time que deseja remover jogador: "))
        if team_num <= len(teams):
            team_name = list(teams.keys())[team_num-1]
            print_team_players(teams[team_name])
            player_num = int(input("Informe o número do jogador para remover: "))
            if player_num <= len(teams[team_name]['players']):
                del teams[team_name]['players'][player_num-1]
                print("Jogador removido do time.")
            else:
                print("Número do jogador inválido.")
    elif(choice == 6):
        print_teams()
        team_num = int(input("Digite o número do time que você deseja ver os jogadores: "))
        if team_num <= len(teams):
            team_name = list(teams.keys())[team_num-1]
            print_team_players(teams[team_name])
        else:
            print("Número inválido!!")
    elif(choice == 7):
        done = True
    else:
        print("Opção inválida!!")

