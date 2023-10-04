//Calculando média simples

const media_simles = (...numbers) => {
  return numbers.reduce((acumulador, item, index, array) => {
    const quantityNumbers = array.length;
    let soma = item + acumulador;

    if (quantityNumbers - 1 === index) {
      return soma / quantityNumbers;
    }
    return soma;
  });
};

console.log(media_simles(2, 6, 3, 7, 4));

//Calculando média ponderada

const media_ponderada = (...args) => {
  let n_x_p = 0;
  let SumP = 0;

  for (const arg of args) {
    n_x_p += arg.n * arg.p;
    SumP += arg.p;
  }

  return n_x_p / SumP;
};

console.log(media_ponderada({ n: 7, p: 2 }, { n: 9, p: 5 }, { n: 3, p: 1 }));

const mediana = (...numbers) => {
  let n = numbers.sort((a, b) => a - b);

  const verify = n.length % 2 === 0;
  if (verify) {
    const position = n.length / 2;
    return (n[position - 1] + n[position]) / 2;
  } else {
    const position = Math.floor(n.length / 2);
    return n[position];
  }
};
console.log(mediana(2, 1, 5, 4, 2, 1, 7, 8, 2, 11, 2, 7, 3, 3));

const moda = (...numbers) => {
  let firstNumber = 0;
  let countFirst = 0;

  let count = 0;
  for (var i = 0; i < numbers.length; i++) {
    for (var j = 0; j < numbers.length; j++) {
      if (numbers[i] == numbers[j]) {
        count++;
      }
      if (count > countFirst) {
        firstNumber = numbers[i];

        //firstNumber.push(numbers[i]);
        countFirst = count;
      }
    }
    count = 0;
  }
  return firstNumber;
  // for (const number of numbers) {
  //   firstNumber = number;
  //   if (firstNumber === number) {
  //     countFirst++;
  //   }
  // }
};

console.log(moda(1, 1, 5, 4, 9, 7, 4, 3, 5, 2, 4, 0, 4));
