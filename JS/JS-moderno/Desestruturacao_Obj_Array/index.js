const pessoa = {
  nome: "Everson",
  idade: 24,
  profissao: "Programador",
  numeros: [232, 2345],
};

const { nome, idade, profissao, numeros } = pessoa;

console.log(nome, idade, profissao);

const list = ["banana", "uva", "morango"];

const [numero1, numero2] = numeros;

console.log(numeros);

const house = {
  color: "Black",
  doors: 5,
  rooms: 10,
  bathrooms: 4,
  telephones: [3212234242, 42354345464, 464646464],
};

const { color, badrooms, telephones } = house;

const [num1, num2, num3] = telephones;

console.log(num1);

const createHouse = ({ color, doors, rooms, bathrooms, telephones }) => {
  const number = Math.floor(Math.random() * 1000);

  return {
    number,
    color,
    doors,
    rooms,
    bathrooms,
    telephones,
  };
};

console.log(createHouse(house));

const user = {
  name: "Jhon Doe",
  age: 53,
  nacionality: "Portuguese",
};

const createUser = ({ name, nacionality }) => {
  return { name, nacionality };
};
console.log(createUser(user));

const users = [
  { name: "Augusto", age: 52 },
  { name: "Maria", age: 32 },
  { name: "Carlos", age: 23 },
];

const [user1, user2, user3] = users;
const { name } = user1;

console.log(name);
