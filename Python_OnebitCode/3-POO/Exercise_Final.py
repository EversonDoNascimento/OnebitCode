from contact import Contact, ContactBook

done = False
contact_book = ContactBook()

while not done:
    print("What you desire make?")
    print("1 - Add a new contact in your list")
    print("2 - To List all contacts of list")
    print("3 - Search for one contact")
    print("4 - Remove a contact of list")
    print("5 - Exit")
    print("-" * 40)
    
    choice = int(input("Type it your choice: "))
    if choice == 5:
        done = True
        print("Come again!")
    
    elif choice == 1:
        contact_name = input("Type it the name of contact: ")
        contact_email = input("Type it the email of contact: ")
        contact_phone = int(input("Type it the phone of contact: "))
        contact = Contact(contact_name,contact_phone,contact_email)
        contact_book.add_contact(contact)

    elif choice == 2:
        contact_book.list_contacts()

    elif choice == 3:
        search_contact = input("Type it the name of contact that you desire search: ")
        contact_book.search_contact(search_contact)

    elif choice == 4:
        remove_contact = input("Type it the name of contact that you desire remove: ")
        contact_book.remove_contact(remove_contact)
    else: 
        print("Invalid Operation")