export const Generate = (size: number) => {
  let password = "";

  const letters = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "!",
    "@",
    "#",
    "$",
    "%",
    "&",
    "*",
    "_",
    "+",
    "-",
    "=",
    "?",
    "~",
    "(",
    ")",
    "[",
    "]",
    "{",
    "}",
    "<",
    ">",
    "|",
    "/",
  ];
  for (let i = 0; i <= size; i++) {
    const randomNumber: number = Math.floor(Math.random() * letters.length);
    const lettersOrNumbers: number = Math.floor(Math.random() * 4);
    password += letters[randomNumber];
    switch (lettersOrNumbers) {
      case 1:
        password += letters[randomNumber];
        break;
      case 2:
        password += letters[randomNumber].toUpperCase();
        break;
      case 3:
        password += Math.floor(Math.random() * 10);
        break;

      default:
        break;
    }
  }
  return password;
};
