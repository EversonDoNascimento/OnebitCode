import pprint

'''
Exercise Final

- Write a python program to manage soccer players

1 - The option of list all teams and show your index, the name and the quantity of
    soccer players.

2 - The option of add a new team, must request a name for the team that will registered

3 - The option of remove a team must request an index of team that will removed

4 - The option to add a new footballer to a team. Request an index of registered teams 
    and link it to the name of the footballer you want to add.

5 - The option of remove a footballer of a team. Request an index of team of soccer player
    and use that of index for remove the soccer player

6 - The option of list a player soccer of a team. Request an index of team and list all the
    soccer player.

Note - This is a final exercise. Then take the opportunity to use all the resources you've
       learned so far, with functions, conditions, loops...

'''

data = []

cond = True
def create_new_team(name):
     data.append({"team_name": name, "Soccers": []})
  
    
def create_new_soccer_player(name,index_team):
    if(len(data) == 0):
         print("Please create a team before!")
    else:
        #data[team]["soccers"].append(name)
        if(index_team <= len(data) - 1):
            data[index_team]["Soccers"].append(name)
            print("Soccer player add with success!")
        else:
            print("Index not exist! Soccer player not add.")

def detele_team (index_team):
    if(index_team <= len(data) - 1):
        data.pop(index_team)
        print("Team removed with success!")
    else:
        print("Index not exist! Team not removed.")

def delete_soccer_player(index_team, name_soccer):
    if(index_team <= len(data) - 1):
        if(name_soccer in data[index_team]["Soccers"]):
            data[index_team]["Soccers"].remove(name_soccer)
            print("Team removed with success!")
        else:
            print("The soccer player not exist!!")
    else:
        print("Index not exist! Team not removed.")

def list_soccers_players_team(index_team):
    
        print(f"The team {data[index_team]['team_name']} has the soccers players: {data[index_team]['Soccers']}")

while cond:
    teamOrSoccer = int(input("Type it:\n 1 - for add a new Team\n 2 - for add a new Soccer player \n" +
                              " 3 - Remove a Team\n 4 - Remove a Soccer player\n"+
                              " 5 - List the all teams\n 6 - List all soccer players\n"+
                              " 7 - Exit: \n"))
    if(teamOrSoccer == 1):
        name_team = input("Type it the name of team")
        create_new_team(name_team)
    elif(teamOrSoccer == 2):
        name_soccer = input("Type it the name of soccer player: ")
        index_team = int(input("Type it the index of team that you desire add the soccer player: "))
        create_new_soccer_player(name_soccer, index_team)
    elif(teamOrSoccer == 3):
        index_team = int(input("Type it the index of team that you desire remove: "))
        detele_team(index_team)
    elif(teamOrSoccer == 4):
        index_team = int(input("Type it the index of team that you desire remove a soccer player: "))
        name_soccer = input("Type it the name of soccer player that you desire remove: ")
        delete_soccer_player(index_team, name_soccer)
    elif(teamOrSoccer == 5):
        index = 0
        for team in data:
            
            print(f"Index of team {index}\nThe name of team is: {team['team_name']}"+
                  f"\nThe quantity of soccers players is: {len(team['Soccers'])}")
            index += 1
            print("-"*30)
    elif(teamOrSoccer == 6):
        index_team = int(input("Type it the index of team that you desire list the soccers players: "))
        list_soccers_players_team(index_team)
    elif(teamOrSoccer == 7):        
        cond = False
