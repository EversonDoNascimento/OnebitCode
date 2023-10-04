const array = [1, 2, 3, 4, 5];

const soma = array.reduce((acumulador, elementoAtual) => {
  return acumulador + elementoAtual;
}, 0);

console.log(soma); // Saída: 15 (1 + 2 + 3 + 4 + 5)

const alturas = [1.81, 1.9, 2, 1.65];

const mediaAlturas = alturas.reduce(
  (acumulador, elementoAtual, index, array) => {
    let somaAlturas = acumulador + elementoAtual;
    if (index === array.length - 1) {
      return somaAlturas / array.length;
    }
    return somaAlturas;
  }
);

//console.log(mediaAlturas);

console.log(mediaAlturas);

const sum = (...params) => {
  return params.reduce((acumulador, elementoAtual, indice) => {
    return acumulador + elementoAtual;
  }, 0);
};

console.log(sum(8, 4, 6, 7, 85, 2, 5));
