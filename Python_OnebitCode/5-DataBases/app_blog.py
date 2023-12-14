from Blog import show_menu, add_post, add_user, query_all_posts_users

done = False

while not done:
    
    show_menu()
    option = input("Type it a option: ")
    
    if option == "1":
        add_user()
    elif option == "2":
        add_post()
    elif option == "3":
        query_all_posts_users()
    elif option == "4":
        done = True
    else:
        print("Invalid operation!")