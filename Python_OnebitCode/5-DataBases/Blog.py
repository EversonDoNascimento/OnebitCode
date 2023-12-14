from conexao_post_ORM import Base, engine, session
from User import User
from Post import Post

#Criar as tabelas
Base.metadata.create_all(engine)

# Função para exibir o menu de opções

def show_menu():
    print("Options menu")
    print("1 - Add user")
    print("2 - Add Post")
    print("3 - Consult user and your posts ")
    print("4 - Exit")
    
# Função para adcionar usuários

def add_user():
    print("Add a new user")
    name = input("Name:\n")
    email = input("Email:\n")
    # criando a instância da minha classe User
    user = User(name,email)
    #Salvando dados na tabela user
    session.add(user)
    session.commit()
    print("User add with success!")

def add_post():
    print("Add a new post")
    title = input("Title:\n")
    content = input("Content:\n")
    author_id = input("Id of autor:\n")
    user = session.query(User).filter_by(id=author_id).first()
    if user:
        post = Post(title=title,content=content,author=user)
        session.add(post)
        session.commit()
        print("Post add with success!")
    else:
        print("Author not exist!")
    
# Função para consultar usuários e posts
def query_all_posts_users():
    users = session.query(User).join(User.posts).order_by(User.name).all()
    for user in users:
        print(f"User: {user.name} email {user.email} ")
        for post in user.posts:
            print(f"Posts: {post.title}, Content: {post.content}")
        
        