import csv

class Address_book:
    def __init__(self):
        self.list = []
    
    def get_contacts(self):
        print(f"\n\nTodos os seus contatos:")
        print("-"*40)
        with open('./data/contacts.csv', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for item in reader:
                print(f"{item['name']} - {item['phone']}")
        print("-"*40)
        print(f"\n\n")
        
    def add_contact(self, contact):
        with open("./data/contacts.csv", "a", encoding="utf-8") as file:
            writer = csv.writer(file, lineterminator='\n')
            writer.writerow([contact._name,contact._phone])
            print("Contato adicionado com sucesso!")
    
    def remove_contact(self, contact_to_remove):
        #Salvando contatos na lista temporária
        with open('./data/contacts.csv', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for item in reader:
                contact = {}
                contact['name'] = item['name'] 
                contact['phone'] = item['phone']
                self.list.append(contact)
        for i,item in enumerate(self.list):
            print(len(self.list))
            
            if contact_to_remove._name in item['name']:
                self.list.pop(i)
                print("Contato removido com sucesso!")
           
        with open('./data/contacts.csv','w',encoding='utf-8') as file:
            writer = csv.writer(file, lineterminator='\n')
            writer.writerow(['name','phone'])
            for item in self.list:
                writer = csv.writer(file, lineterminator='\n')
                writer.writerow([item['name'],item['phone']])

    
    def search_contact(self, contact):
        with open('./data/contacts.csv', 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            print("-"*40)
            print("O número do contato que você pesquisou é: ")
            print(f"\n")
            for c in reader:
                if contact._name in c['name']:
                    print(f"{c['name']} - {c['phone']}")
            print(f"\n")   
             
        


class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value_name):
        if not isinstance(value_name, str):
            raise TypeError("Not is a string")
        else:
            self._name = value_name
    @property
    def phone(self):
        return self._phone
    @name.setter
    def phone(self, value_phone):
        if not isinstance(value_phone, int):
            raise TypeError("Not is a number!")            
        else:
            self._phone = value_phone

