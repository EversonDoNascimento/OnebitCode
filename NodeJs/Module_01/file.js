const fs = require("fs");
//Criando nono arquivo no servidor
// Utilizando fs.appendFile você irá adicionar um novo texto ao antigo que está escrito no documento
fs.unlink("test.txt", (err) => {
  console.log(err);
});
