//Spread Operator

const lista = ["Banana", "Maçã", "Uva"];
//Apontando a variavel listaCopy para pegar o valor de referência da lista
const listaCopy = lista;

listaCopy.push("Melão");
listaCopy.push("Abacaxi");
console.log(listaCopy, lista);
//Fazendo de fato a clonagem de um array
const listaClone = [...lista];

listaClone.push("Laranja");
listaClone.push("Pêra");

console.log(lista, listaCopy, listaClone);
