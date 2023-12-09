from address_book import Address_book, Contact

done = False
address_book = Address_book()
while not done:
    print("O que você deseja fazer: ")
    print("1 - Adicionar um contato")
    print("2 - Listar contatos")
    print("3 - Remover um contato")
    print("4 - Pesquisar um contato")
    print("5 - Sair")
    
    choice = input("Digite o número da opção que você deseja: ")
    
    if choice == "1":
        name = input("Digite o nome do contato que você deseja adicionar: ")
        phone = int(input("Digite o número do telefone que você deseja adicionar: "))
        contact = Contact(name,phone)
        address_book.add_contact(contact)
    
    elif choice == "2":
        address_book.get_contacts()
    
    elif choice == "3":
        name = input("Digite o nome do contato que você deseja remover: ")
        contact = Contact(name,1)
        address_book.remove_contact(contact)
        
    elif choice == "4":
        name = input("Digite o nome do contato que você deseja remover: ")
        contact = Contact(name,1)
        address_book.search_contact(contact)
    elif choice == "5":
        done = True
        print("Saindo...")
        
    else:
        print("Opção inválida!")