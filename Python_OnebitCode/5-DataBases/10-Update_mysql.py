from conn_mysql import connection

cursor = connection.cursor()


done = False

while not done:
    
    print("Hello, Welcome to your list of games!")
    print("1 - For add a new game: ")
    print("2 - To list all games")
    print("3 - For update a game")
    print("4 - Exit")
    
    choice = input("Type it your choice: ")
    
    if(choice == "1"):
        name_game = input("Type it the name of game: ")
        year_game = int(input("Type it the released year of game: "))
        score_game =  float(input("Type it a rating note for game: "))
        
        cursor.execute(
            """
                INSERT INTO games(name,year,score) VALUES(%s,%s,%s)
            
            """
        ,(name_game,year_game,score_game))
        print("Game insert with success!")
        
    elif(choice == "2"):
        cursor.execute("SELECT * FROM games")
        result = cursor.fetchall()
        print("Your games are: ")
        print(f"\n")
        for game in result:
            print(game)        
        print(f"\n")
        print("-"*30)
    
    elif(choice == "3"):
        id_game = int(input("Type it the id of game that you desire update: "))
        print("1 - For update the name of game")
        print("2 - For update the relased year of game")
        print("3 - For update the score of game")
        choice_update = input("Type it what you desire: ")
        if(choice_update == "1"):
            new_name = input("Type it a new name of game: ")
            cursor.execute("""
                           UPDATE games
                           SET name = %s
                           WHERE id = %s
                           """,(new_name, id_game))
            connection.commit()
            print("Game updated with success!")
            
        elif(choice_update == "2"):
            new_year = int(input("Type it a new relased year of game: "))
            cursor.execute("""
                           UPDATE games
                           SET year = %s
                           WHERE id = %s
                           """,(new_year, id_game))
            connection.commit()
            print("Game updated with success!")
        
        elif(choice_update == "3"):
            new_score = float(input("Type it a new score of game: "))
            cursor.execute("""
                           UPDATE games
                           SET score = %s
                           WHERE id = %s
                           """,(new_score, id_game))
            connection.commit()
            print("Game updated with success!")
        
        else:
            print("Invalid Operation!")
            
    elif(choice == "4"):
        done = True
        print("Close the list")
        
    else: 
        print("Invalid Operation")
    
connection.commit()
connection.close()