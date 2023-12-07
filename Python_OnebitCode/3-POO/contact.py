class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):

        if not isinstance(value, str):
            raise TypeError("Not is a type string!")
        else:
            self._name = value

    @property
    def phone(self):
        return self._phone
    
    @phone.setter
    def phone(self, value):

        if not isinstance(value, int):
           raise TypeError("Not is a type int")
        else:
            self._phone = value

    @property
    def email(self):
        return self._email
    @email.setter
    def email(self,value):

        if not isinstance(value, str):
            raise TypeError("Not is a type string")
        else:
            self._email = value

    def __str__(self) -> str:
        return f"- Name: {self.name}, Phone: {self.phone}, email: {self.email}"



class ContactBook:
    def __init__(self):
        self.contacts_list = []

  
    def list_contacts(self):
        print("All Contacts of your list:")
        if not len(self.contacts_list) == 0:
            for contato in self.contacts_list:
                print(contato)
        else:
            print("Not there is contact")
        print("-" * 30)

    def add_contact(self, contact):
        self.contacts_list.append(contact)
        print("Contact add with success!")

    def search_contact(self, contact_value):
        size = len(self.contacts_list)
        
        for i, contato in enumerate(self.contacts_list):
            found = False
            if contato.name.upper() == contact_value.upper():
                print(f"{i} The contact is: {contato}")
                break
            elif size - 1 == i:
                print("Usuário não existe")

    def remove_contact(self, contact_value):
        for i,contato in enumerate(self.contacts_list):
            if contato.name.upper() == contact_value.upper():
                self.contacts_list.pop(i)
                print("Contact removed with success!")
                
        
