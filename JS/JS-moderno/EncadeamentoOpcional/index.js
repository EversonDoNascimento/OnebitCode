const pessoa = {
  nome: "Everson",
  idade: null,
  profissao: "Programador",
};

if (pessoa?.idade) {
  console.log(pessoa.idade);
} else {
  console.log(false);
}
