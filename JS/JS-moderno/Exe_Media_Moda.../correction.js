//Simple Avarage

const avarage = (...numbers) => {
  const size = numbers.length;
  const sum = numbers.reduce((accum, num) => accum + num);
  return sum / size;
};

const avarageWeight = (...entries) => {
  const sum = entries.reduce((accum, { number, weight }) => {
    return accum + number * (weight ?? 1);
  }, 0);
  const sumWeight = entries.reduce(
    (accum, { weight }) => accum + (weight ?? 1),
    0
  );
  return sum / sumWeight;
};

console.log(
  avarageWeight(
    { number: 9, weight: 3 },
    { number: 7 },
    { number: 10, weight: 1 }
  )
);

const median = (...numbers) => {
  const orderedNumbers = [...numbers].sort((a, b) => a - b);
  const middle = Math.floor(orderedNumbers.length / 2);
  console.log(orderedNumbers);
  if (orderedNumbers.length % 2 !== 0) {
    return orderedNumbers[middle];
  }
  return (orderedNumbers[middle] + orderedNumbers[middle - 1]) / 2;
};

console.log(median(2, 1, 5, 5));

const mode = (...numbers) => {
  const quantities = numbers.map((num) => [
    num,
    numbers.filter((n) => num === n).length,
  ]);
  quantities.sort((a, b) => b[1] - a[1]);
  return quantities[0][0];
};

console.log(
  mode(
    2,
    99,
    99,
    99,
    1,
    3,
    99,
    99,
    99,
    4,
    99,
    99,
    99,
    2,
    3,
    3,
    3,
    3,
    5,
    3,
    2,
    99
  )
);
