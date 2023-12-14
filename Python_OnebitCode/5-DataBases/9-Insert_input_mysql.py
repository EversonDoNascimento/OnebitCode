from conn_mysql import connection

cursor = connection.cursor()


done = False

while not done:
    
    print("Hello, Welcome to your list of games!")
    print("1 - For add a new game: ")
    print("2 - To list all games")
    print("3 - Exit")
    
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
        done = True
        print("Close the list")
        
    else: 
        print("Invalid Operation")
    
connection.commit()
connection.close()