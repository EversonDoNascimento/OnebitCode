const a = 0;
const b = 23;
const c = null;
console.log(a || b);

console.log(a ?? b);

console.log(c ?? b);

console.log(b || (c && b));

const lista = [12, 31, 414, 3];

const newArray = [...lista, 2];
console.log(newArray, lista);

let person = {
  name: "John Doe",
  email: "doejohn@email.com",
  birthay: "1990-03-14",
  age: 32,
};

let x = 0;
x = person.data?.age;
console.log(x);

const f = ({ n, p }) => {
  return { n, p };
};

console.log(f({ n: 2, p: 3 }));
