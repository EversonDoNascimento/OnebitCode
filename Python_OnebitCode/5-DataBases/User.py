from conexao_post_ORM import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class User(Base):
    #Definindo o nome da tabela com o table name
    __tablename__ = "users"
    #Definindo que o id é uma coluna com o tipo inteiro e chave primária
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    posts = relationship("Post", back_populates="author")
    
    def __init__(self, name, email):
        self.name = name
        self.email = email